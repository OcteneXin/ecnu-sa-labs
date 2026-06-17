## LLVM 框架

理解 LLVM 框架：IR、API 和工具链。

### 目标

本实验的目标有三：
+ 理解一种名为 [LLVM IR][llvm-lang] 的 C 程序表示形式，我们将在实验中使用它。
它是 [LLVM][llvm]（一个流行的多语言编译器框架）使用的中间表示。
+ 通过使用 [LLVM API][llvm-api] 编写一个 [LLVM pass][llvm-pass] 并运行它，以静态方式查找程序中的所有二元运算符并对其进行插桩，从而理解该 API。
+ 通过执行插桩后的代码，理解程序的静态性质与动态性质之间的区别。

### 前置要求

+ 阅读关于 LLVM 入门：第一部分（LLVM 概述）和第二部分（LLVM IR 结构）的课程幻灯片。
这是完成本实验第一部分以及后续课程内容所必需的，以便能够阅读 LLVM IR 进行调试。
+ 将 [LLVM 入门][llvm-primer]：第三部分（LLVM API）放在手边，作为本实验以及整个课程中用到的大部分 LLVM API 的快速参考。

### 环境设置

+ 在 VS Code 中，使用“打开文件夹”选项打开 `lab2` 文件夹。
+ 确保 Docker 正在你的机器上运行。
+ 按 F1 键打开 VS Code [命令面板][command-palette]；搜索并选择 `Reopen in Container`。
+ 这将在 VS Code 中为本实验设置开发环境。
+ 在开发环境中，Lab 2 的骨架代码将位于 `/lab2` 目录下。
+ 之后，如果 VS Code 提示你为实验选择一个工具包，请选择 Clang 19。

### Lab2 的项目结构：
```
- lib
  |
  -- runtime.c: 一些辅助函数，例如 `__binop_op__` 等，你将通过你的 pass 注入这些函数。

- src
  |
  -- DynamicAnalysisPass.cpp: 报告二元运算符执行时的位置、类型以及操作数的运行时值。
  ｜
  -- StaticAnalysisPass.cpp: 报告每个二元运算符未执行时的位置、类型和操作数。
  ｜
  -- Utils.cpp: 一些辅助函数，例如 `getBinOpSymbol` 和 `getBinOpName` 等。
```

### 第一部分：理解 LLVM IR

#### 步骤 1

学习 LLVM 入门指南，以理解 LLVM IR 的结构。
该指南展示了如何在示例 C 程序上运行 `clang` 以生成相应的 LLVM IR 程序。
你可以使用 `/lab2/test` 目录下的 C 程序来尝试：

```sh
/lab2$ cd test
/lab2/test$ clang-19 -emit-llvm -S -O0 -fno-discard-value-names -Xclang -disable-O0-optnone -c simple0.c
```

`clang` 是一个 C 语言编译器前端，它使用 LLVM 作为后端。
clang 的用户手册中有一个关于其[命令行选项][clang-cli-opts]的有用参考。
简要说明：
+ `-emit-llvm` 指示编译器生成 LLVM IR（将保存到 simple0.ll 文件中）
+ `-S` 指示 clang 仅执行预处理和编译步骤
+ `-g` 指示 clang 在生成的输出中包含调试信息
+ `-fno-discard-value-names` 保留生成的 LLVM 中值的名称，以提高可读性。
+ `-Xclang -disable-O0-optnone` 阻止 clang 在 -O0 级别添加 optnone 属性，这样生成的 IR 保持简单，但仍可以被 LLVM passes 优化或分析。

#### 步骤 2

通过填写 `/lab2/c_programs` 目录下提供的模板代码，手动编写与 `/lab2/ir_programs` 目录下 LLVM IR 程序相对应的 C 程序。
确保在你手写的 C 程序上运行上述命令，能够生成完全相同的 LLVM IR 程序，因为我们将进行自动评分。
你可以使用 diff[^1] 命令行工具来检查你的文件是否相同。

```sh
/lab2$ cd c_programs
/lab2/c_programs$ clang-19 -emit-llvm -S -O0 -fno-discard-value-names -Xclang -disable-O0-optnone -c test1.c
/lab2/c_programs$ diff -y --suppress-common-lines --report-identical-files --ignore-all-space test1.ll ../ir_programs/test1.ll
```

请注意，你可以使用 `diff --strip-trailing-cr` 或 `diff -w`（`-w` 忽略空白字符的差异，“空白”字符包括制表符、垂直制表符、换页符、回车符和空格）来忽略回车和空格方面的差异。

或者，你可以让提供的 Makefile 自动为你完成此操作：

```sh
/lab2/c_programs$ make test1 # 仅自动运行 test1
/lab2/c_programs$ make all   # 自动运行所有测试
/lab2/c_programs$ make clean # 删除所有输出文件
```

请提交 `/lab2/c_programs` 目录下的程序用于自动评分。

### 第二部分：理解 LLVM API

#### 步骤 1

在本实验及未来的实验中，我们将使用 `CMake`，这是一个用于管理构建过程的现代工具。
如果你不熟悉 `CMake`，强烈建议你先阅读 [CMake 教程][cmake-tutorial]（特别是教程中的步骤 1 和步骤 2）。
运行 `cmake` 会生成一个你可能更熟悉的 Makefile。
如果不熟悉，请在继续之前阅读 [Makefile 教程][makefile-tutorial]。
*一旦生成了 Makefile，编辑源文件后，你只需调用 `make` 即可重新构建项目。*
运行以下命令来设置本实验的这一部分：

```sh
/lab2$ mkdir -p build && cd build
/lab2/build$ cmake ..
/lab2/build$ make
```

你应该会看到在 `lab2/build` 目录中创建了几个文件。
除其他文件外，这会从我们在 `lab2/src/DynamicAnalysisPass.cpp` 和 `lab2/src/StaticAnalysisPass.cpp` 中提供的代码构建两个名为 `DynamicAnalysisPass.so` 和 `StaticAnalysisPass.so` 的 LLVM pass（你将在本实验中修改这两个文件），以及一个名为 `libruntime.so` 的运行时库，它提供了一些本实验中会用到的函数。
接下来的步骤遵循从左到右描绘的工作流程：

<img src="../images/flowchart.png"
  style="height: auto; width: 100%">

#### 步骤 2

如步骤 1 所述，你将把本实验的功能实现为两个 LLVM pass，分别称为 `StaticAnalysisPass` 和 `DynamicAnalysisPass`。
LLVM passes 是 LLVM 框架的子进程。
它们通常对程序执行转换、优化或分析。
每个 pass 都作用于输入程序的 LLVM IR 表示。
因此，要在一个输入 C 程序上练习本实验，你必须首先像在第一部分中那样，将程序编译为 LLVM IR：

```sh
/lab2$ cd test
/lab2/test$ clang-19 -emit-llvm -S -O0 -fno-discard-value-names -Xclang -disable-O0-optnone -c -o simple0.ll simple0.c -g
```

#### 步骤 3

接下来，我们使用 opt 在编译后的 C 程序上运行提供的 StaticAnalysisPass：

```sh
/lab2/test$ opt-19 -load-pass-plugin ../build/StaticAnalysisPass.so -passes='function(static-analysis)' -S simple0.ll -o simple0.static.ll
```

`opt` 是一个 LLVM 工具，用于对 LLVM IR 执行分析和优化。
选项 `-load-pass-plugin` 加载我们的 LLVM pass 库，而 `-passes='function(static-analysis)'` 指示 opt 在 `simple0.ll` 上运行该 pass。
（库可以并且通常包含多个 LLVM passes。）
查阅 [opt 的文档][opt-doc] 以了解使用该工具的可能方式；它可能有助于你构建和调试解决方案。
类似地，我们使用 `opt` 在编译后的 C 程序上运行提供的 `DynamicAnalysisPass`：

```sh
/lab2/test$ opt-19 -load-pass-plugin ../build/DynamicAnalysisPass.so -passes='function(dynamic-analysis)' -S simple0.ll -o simple0.dynamic.ll
```

`simple0.static.ll` 中生成的程序应与 `simple0.ll` 相同，而 `simple0.dynamic.ll` 中的程序在本实验中则不会相同。
你可以使用 `diff`[^1] 来验证这一点：

```sh
# clang 中的 -g 参数会输出调试信息。使用 diff 时，只关注代码内容的一致性。
/lab2/test$ diff simple0.static.ll simple0.ll
1c1
< ; ModuleID = 'simple0.ll'
---
> ; ModuleID = 'simple0.c'
/lab2/test$ diff simple0.dynamic.ll simple0.ll
...
```

#### 步骤 4

接下来，编译插桩后的程序，并将其与提供的运行时库链接，以生成一个名为 `simple0` 的可独立执行文件：

```sh
/lab2/test$ clang-19 -o simple0 -L../build -lruntime simple0.dynamic.ll
```

#### 步骤 5

最后，在空输入上运行该可执行文件；请注意，对于期望非空输入的程序，你可能需要手动提供测试输入：

```sh
/lab2/test$ ./simple0
```

在本实验中，你将把你的代码添加到 `src/StaticAnalysisPass.cpp` 和 `src/DynamicAnalysisPass.cpp` 中。
提供的 `StaticAnalysisPass` 报告程序中所有指令的位置，你将实现功能来报告程序中每个二元运算符的位置、类型和操作数。
提供的 `DynamicAnalysisPass` 以这样一种方式修改程序：当执行程序时，它会通过将指令的行号和列号打印到覆盖文件中来报告指令何时被执行。
你将实现额外的功能，修改程序以在二元运算符执行时也报告其位置、类型以及操作数的运行时值。
我们将在下一节中指定确切的输出格式，但在完成后，你对 `simple0.c` 的 `StaticAnalysisPass` 输出应该如下所示：

```
Running Static Analysis Pass on function main
Locating Instructions
2, 7
3, 7
4, 11
4, 15
4, 13
Division on Line 4, Column 13 with first operand %0 and second operand %1
4, 7
5, 3
```

完成 `DynamicAnalysisPass` 后，执行 `simple0` 应创建两个文件：`simple0.cov` 和 `simple0.binops`，内容如下：

```
# simple0.cov
2, 7
3, 7
4, 11
4, 15
4, 13
4, 7
5, 3
# simple0.binops
Division on Line 4, Column 13 with first operand=3 and second operand=2
```

你可以让提供的 Makefile 自动为你完成此操作：

```sh
/lab2/test$ make all   # 自动运行所有 simples
/lab2/test$ make clean # 删除所有输出文件
```

### 实验说明

#### 静态分析
如前所述，我们提供了 `src/StaticAnalysisPass.cpp`，其中包含一个静态分析，用于报告程序中所有指令的位置，你将向其中添加另一个分析。
首先花些时间理解提供的分析，它打印出所有指令的位置；LLVM 入门指南将有助于理解此处使用的 API。
接下来，你将实现一个静态分析，打印出每个类型为 BinaryOperator 的指令的种类、位置和操作数，并按照以下格式打印：

```sh
Division on Line 4, Column 13 with first operand %0 and second operand %1
<Operator> on Line <Line>, Column <Col> with first operand <OP1> and second
operand <OP2>
```

你会发现 `Utils.h` 中的 `getBinOpSymbol` 和 `getBinOpName` 函数对此很有帮助，建议你查看一下 `getBinOpSymbol` 的实现。
你可以使用 `Utils.h` 中的 `variable` 函数从其对应的 LLVM Value 中获取操作数的名称。

#### 动态分析

它涉及检查正在运行的程序以获取其在运行时的状态和行为信息；这与静态分析（分析代码独立于任何执行的属性）形成对比。
检查程序运行时行为的一种方法是在编译时将代码注入到程序中；这种技术属于[插桩][instrumentation-def]的范畴。
对于 `src/StaticAnalysisPass.cpp` 中的每个静态分析，我们将在 `src/DynamicAnalysisPass.cpp` 中有一个相应的动态分析插桩。
我们为你提供了第一个分析的实现，它在每条指令之前注入对 `__coverage__` 函数的调用，该函数将正在执行的指令的行号和列号存储到覆盖文件中。
研究该实现以理解用于注入函数的 API。
你将实现一个动态分析，跟踪二元运算符的种类、位置以及操作数的运行时值。
为此，你需要检查一条指令是否是 `BinaryOperator`，并使用 `instrumentBinOpOperands` 函数对其进行插桩，接下来你将实现该函数。
`instrumentBinOpOperands` 函数必须在每个二元运算符之前注入对 `__binop_op__` 的调用。
你可以看到 `__binop_op__` 接受 5 个参数，即：运算符的符号、操作的行号和列号以及两个操作数的运行时值。
你可以使用 `getBinOpSymbol` 函数来获取与运算符对应的符号。
为了获取操作数的运行时值，需要记住在 LLVM 中，**由指令定义的变量由指令本身表示**。

#### 代码覆盖率入门

代码覆盖率是衡量在特定运行中执行了多少程序代码的指标。
有许多不同的标准来描述覆盖率。
在本实验中，我们提供了行覆盖率，你将使用与现代代码覆盖率工具（如 LLVM 的基于源代码的代码覆盖率工具和 gcov）相同的机制，实现一个跟踪程序执行期间二元运算符的人工标准。
它在编译时对程序的 LLVM IR 指令进行插桩，以记录在运行时执行的程序源代码级指令的行号和列号。
这个看似原始的信息能够实现强大的软件分析用例。
在下一个实验中，你将使用行覆盖率信息来指导自动化测试输入生成器，从而实现现代工业级模糊测试器的架构。

<img src="../images/example-coverage-report.png"
  style="height: auto; width: 100%">

#### 调试位置入门

当你使用 `-g` 选项编译 C 程序时，LLVM 将为 LLVM IR 指令包含调试信息。
使用上述插桩技术，你的 LLVM pass 可以收集 `Instruction` 的调试信息，并在你的分析中使用它。
我们将在以下部分讨论此接口的具体细节。

##### 插桩 Pass

我们提供了一个框架，你可以在此基础上构建你的 LLVM pass。
你需要编辑 `src/DynamicAnalysisPass.cpp` 文件，为你的 LLVM Pass 实现功能。
文件 `lib/runtime.c` 包含你将使用你的 pass 注入的函数：

```c
void __binop_op__(char c, int line, int col, int op1, int op2);
```

由于你将创建一个动态分析，你的 pass 应该使用对这些函数的调用来插桩代码。
简而言之，要完成本实验中的 `DynamicAnalysisPass`，你有以下高级任务：

+ 检查二元运算符并使用 `instrumentBinOpOperands` 对其进行插桩。
+ 实现 `instrumentBinOpOperands` 以插入对 `__binop_op__` 的调用。

#### 向 LLVM 代码中插入指令

在完成第一部分并完成静态分析后，一旦你熟悉了 LLVM IR 的组织结构、LLVM 指令和 `Instruction` 类，你就可以开始处理 `DynamicAnalysisPass`，为此你将需要使用 LLVM API 向程序中插入额外的指令。
在 LLVM 中有[多种方法可以做到这一点][llvm-insert-inst]。
使用 LLVM 时的一种常见模式是创建一条新指令，并将其直接插入到某条指令**_之前_**。
例如，考虑以下代码片段：

```cpp
Instruction* ExistingInstruction = ...;
auto *NewInst = new Instruction(..., ExistingInstruction);
```

创建了一条新指令 (`NewInst`)，并将其插入到现有指令 `ExistingInstruction` _之前_。
`Instruction` 的子类有类似的方法来做到这一点。
特别是，对于本实验，你可以使用这种模式来创建和插入调用指令 (`CallInst`)，如下所述。
你还应该查看 `instrumentCoverage` 函数中如何将调用指令插入到程序中，作为下面指令的示例。

#### 将 C 函数加载到 LLVM 代码中

我们已经在 `runtime.c` 文件中为你提供了 C 函数的定义，但你必须注入 LLVM 指令以从插桩代码中调用它们。
在可以在 Module 中调用函数之前，必须使用适当的 LLVM API [Module::getOrInsertFunction][llvm-insert-function] 将其加载到 Module 中。
一种方法如下所示：

```cpp
M->getOrInsertFunction(FunctionName, return_type, arg1_type, ..., argN_type);
```

这里，`return_type`、`arg1_type`、... `argN_type` 是描述函数参数的 LLVM Type 的变量。
例如，C 类型 `int` 通常是 LLVM 类型 `i32`，`char` 是 `i8`，`boolean` 是 `i1`。
这一步类似于在 C 或 C++ 中声明函数。

接下来，假设你希望该函数在某个指令 I 之前被调用。
为此，你将需要使用 [CallInst::Create][callinst-create] 创建一条调用指令，如下所示：

```cpp
Instruction I = ...;
auto *NewFunction = M->getFunction(FunctionName);
CallInst::Create(NewFunction, Args, "", &I);
```

在这里，你应该用适当的函数参数值填充 `std::vector<Value *> Args`。
此外，如前所述，在 LLVM 中，由指令定义的变量由指令本身表示。
此外，`Instruction` 类是 `Value` 的子类；这使得将由 Instruction 定义的变量作为参数传递给函数相对简单。

#### 调试位置

正如我们之前提到的，当使用 `-g` 编译时，LLVM 将为 LLVM 指令存储原始 C 程序的代码位置信息。
这是通过 DebugLoc 类完成的：

```cpp
Instruction* I = ...;
DebugLoc Debug = I->getDebugLoc();
printf("Line No: %d\n", Debug.getLine());
```

你需要收集这些信息并将其转发给适当的函数。
并非每条 LLVM 指令都对应于其 C 源代码中的特定行。
因此，在使用调试信息之前，你通常需要检查一条指令是否确实拥有它。

### 理解代码的静态和动态性质

代码有两种类型的性质：静态性质和动态性质。
静态性质是可以从代码的源代码表示中推断出来的，并且独立于程序的任何特定运行。
另一方面，代码在运行时的行为由其动态性质捕获。
在第二部分中，你实现了一个 LLVM pass，它静态地查找所有二元运算符及其操作数；你还实现了一个 LLVM pass，它对所有二元运算符进行插桩，以收集描述在程序的给定运行中哪些二元运算符被执行、以什么顺序执行以及使用什么操作数执行的动态性质。
静态和动态性质都告诉我们关于程序的有趣事实，这些事实可以以各种方式加以利用。
特别是，在本课程中，我们将使用它们来查找程序中的错误。

### 提交

完成实验后，通过提交并推送 `lab2/` 目录下的更改来提交你的代码。具体来说，你需要提交对 `src/DynamicAnalysisPass.cpp` 和 `src/StaticAnalysisPass.cpp` 的更改。

```
   lab2$ git add src/DynamicAnalysisPass.cpp src/StaticAnalysisPass.cpp
   lab2$ git commit -m "你的提交信息"
   lab2$ git push
```

<!--
完成实验后，你可以使用以下命令创建一个 `submission.zip` 文件：

```sh
/lab2$ make submit
...
submission.zip created successfully.
```

然后将 `submission.zip` 文件上传到助教的邮箱。
-->

[llvm-primer]: https://tingsu.github.io/files/courses/llvm-framework-primer.pdf
[llvm-lang]: https://llvm.org/docs/LangRef.html
[llvm-api]: https://llvm.org/docs/index.html
[llvm-pass]: https://llvm.org/docs/WritingAnLLVMNewPMPass.html
[llvm]: https://llvm.org
[command-palette]: https://code.visualstudio.com/docs/getstarted/tips-and-tricks#_command-palette
[clang-cli-opts]:https://releases.llvm.org/19.1.0/tools/clang/docs/UsersManual.html#command-line-options
[cmake-tutorial]: https://cmake.org/cmake/help/latest/guide/tutorial/index.html
[makefile-tutorial]: https://www.gnu.org/software/make/manual/html_node/Simple-Makefile.html#Simple-Makefile
[opt-doc]: https://llvm.org/docs/CommandGuide/opt.html
[instrumentation-def]: https://en.wikipedia.org/wiki/Instrumentation_(computer_programming)
[llvm-insert-inst]: https://releases.llvm.org/8.0.0/docs/ProgrammersManual.html#creating-and-inserting-new-instructions
[llvm-insert-function]: https://llvm.org/doxygen/classllvm_1_1Module.html#a89b5f89041a0375f7ece431f29421bee
[callinst-create]: https://llvm.org/doxygen/classllvm_1_1CallInst.html#a850d8262cd900958b3153c4aa080b2bb