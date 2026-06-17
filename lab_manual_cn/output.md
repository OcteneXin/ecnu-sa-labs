---
title: "软件分析与测试实验手册"
author: [ecnu-sa-labs]
date: "2026-06-01"
lang: "zh"
toc: true
toc-own-page: true
titlepage: true
book: true
classoption: [oneside]
...

## 设置课程实验环境

我们的实验使用 VScode 和 Docker 容器来构建一个灵活、一致且开箱即用的开发环境。您可以查看下图来了解我们实验环境的架构（即 VS Code 的远程开发模式）。从概念上讲，您的本地操作系统运行 VS Code，而 VS Code 连接到运行在 Docker 容器中的远程操作系统。这样，您就可以通过本地操作系统上的 VS Code 编辑远程操作系统中的文件，并在远程操作系统上运行所有实验。在 Docker 容器中，我们已经为您设置好了一切（所有必要的工具和依赖项）。请注意，Docker 运行在您的本地操作系统上。

![](../images/principle_of_vscode_remote_development.png)

### Docker 容器

- Ubuntu 22.04, LLVM 19

:star: 您的本地机器需要至少有 15GB 的磁盘空间和 8GB 的内存才能运行 Docker 容器。

### 您需要安装什么？

- [Docker](https://www.docker.com/)
- [VS code](https://code.visualstudio.com/Download)

### 设置实验环境的说明

#### 第一步
对于本课程，我们将使用带有 VS Code 的 Docker 容器，以确保每个人在实验中使用一致的开发环境。因此，您需要在本地机器上安装 <a href="https://www.docker.com/">docker</a>[^1]。

![](../images/course-vm-d.jpg)

#### 第二步
之后，安装 <a href="https://code.visualstudio.com/Download">VS Code</a>，并在 VS Code 中从 `Extensions` 安装 `Remote Development`。

![](../images/remote_development.png)

在 VS Code 中，我们还建议您从 `Extensions` 安装 `GitHub Repositories`。它让您可以直接在 Visual Studio Code 中快速浏览、搜索、编辑和提交到任何远程 GitHub 仓库。

![alt text](../images/github_repositories.png)

#### 第三步
在您的本地机器上克隆我们的仓库（[ecnu-sa-labs](https://github.com/ecnu-sa-labs/ecnu-sa-labs)）。
在这个仓库中，我们在 `lab1`、`lab2` 等文件夹中提供了实验。
在每个实验中，我们提供了一个配置文件 `.devcontainer/devcontainer.json`[^2]，该文件指示 VS Code 使用适当的 Docker 镜像和各种其他配置选项来设置开发环境。

以下是一个例子：`.devcontainer/devcontainer.json`，
```
"name": "ECNUA SA Lab Container",
"image": "ecnusa/ecnu-sa-labs:latest",
"runArgs": [
	"--cap-add=SYS_PTRACE",
	"--security-opt",`
	"seccomp=unconfined",
	"--privileged"
],

// 为容器设置环境变量。
"remoteEnv": {
	"LD_LIBRARY_PATH": "${containerWorkspaceFolder}/build:${containerEnv:LD_LIBRARY_PATH}"
},
...
```

<!-- 在开始某个实验之前，请打开 Docker。 -->

<!-- ![](../images/course-vm-f.jpg) -->

#### 第四步
要开始进行某个实验，请在一个**新的** VS Code 窗口中打开该实验。

:star: 注意：您需要在一个新的 VS Code 窗口中打开实验文件夹（例如 `lab1`）。
在 VS Code 中，转到 `File`，选择 `New Window`，找到并选择要打开的实验文件夹（例如 `lab1`）。您应该能够像下图一样打开实验。

![](../images/course-vm-lab1-folder.jpg)

在 VS Code 中打开命令面板[^3]，搜索并选择 `Dev Containers:Rebuild and Reopen in Container` 来设置实验环境（即构建并打开容器，并将您的本地机器连接到包含实验的容器）。这个过程可能需要几分钟，因为它需要下载我们的 Docker 镜像。

:star: 注意：如果在构建和打开容器时遇到错误，另一种方法是直接在终端中执行 `docker pull ecnusa/ecnu-sa-labs`，从 <a href="https://hub.docker.com/">docker hub</a> 拉取 <a href="https://hub.docker.com/r/ecnusa/ecnu-sa-labs">ecnusa/ecnu-sa-labs</a> 镜像。

:star: 如果您无法访问 Docker 页面，请参考 <a href="https://pan.baidu.com/s/1B7W2EeSUts_k2lzoTnJhDg?pwd=yebz">此链接</a> 下载 Docker 镜像。解压后，在容器中构建之前，使用 `docker load -i <path to image tar file>` 加载镜像。

![](../images/course-vm-lab1-rebuild-and-reopen-container.jpg)

这将重新加载 VS Code 并设置开发环境。您现在可以在 VS Code 中编辑、运行和调试您的实验。您可以在 VS Code 中打开终端：

![](../images/course-vm-lab1.jpg)

要检查您是否已成功在容器中打开实验，可以在终端中运行 `clang --version`，您应该能够看到 clang 版本：

![](../images/course-vm-lab1-clang.jpg)

如果您关闭了这个新窗口中的实验（即您的本地机器与容器断开了连接），并希望继续实验。
您可以再次在 VS Code 中打开实验文件夹，打开命令面板，搜索并选择 `Reopen in Container`。

:star: 注意：您在实验文件夹（容器内）所做的任何更改都将在您的 ecnu-sa-labs 文件夹（本地机器上）中可用。

[^1]: 注意：对于 Windows 用户，请选择 `Download for Windows-AMD64`；对于 Mac 用户，请选择 `Download for Mac`。如果您无法直接访问 <a href="https://www.docker.com/">docker</a>，请参考 <a href="https://pan.quark.cn/s/6fc0c0d8ccf6">此链接</a> 进行下载。

[^2]: `devcontainer.json` 文件是一个 JSON 格式的配置文件，通常存放在项目根目录下的 `.devcontainer` 文件夹中。它定义了开发容器的配置信息，包括容器的基础镜像、需要安装的工具和扩展、环境变量等。通过这个文件，开发者可以确保项目在不同的开发环境中都能保持一致的运行状态。

[^3]: 在 VS Code 中，命令面板是一个功能强大且用途广泛的工具，可以快速访问各种命令。在 Windows 和 Linux 上，您可以通过按 `Ctrl + Shift + P` 打开命令面板。在 macOS 上，使用 `Command + Shift + P`。

## 理解静态分析与动态分析

理解软件分析的基本概念以及用于评估分析有效性的度量指标。

### 目标

本实验的目标是使用标准的静态与动态分析工具对 C 程序进行分析，发现除零错误，并解读分析结果，从而更好地理解不同技术之间的权衡。具体来说，我们将使用 <a href="https://github.com/google/AFL">AFL</a>（American Fuzzy Lop，一种动态分析器/模糊测试器）和 <a href="https://clang-analyzer.llvm.org/">CSA</a>（Clang Static Analyzer，一种静态分析器）。

### 前置要求

课程讲座中介绍了本实验使用的各种术语，例如：静态分析与动态分析、可靠性（Soundness）、完备性（Completeness）、精确率（Precision）、召回率（Recall）等。

### 环境配置

##### 步骤 1.
Lab 1 的骨架代码位于 `/lab1` 目录下。
在描述本实验的文件位置时，我们将 Lab 1 的这个顶层目录简称为 `lab1`。

##### 步骤 2.
在整个实验过程中，我们将使用 `CMake`，这是一个用于管理构建过程的现代工具。
如果你不熟悉 `CMake`，我们建议阅读 [CMake 教程][cmake-tutorial]
（请特别注意教程中的步骤 1 和步骤 2）。
运行 `cmake` 会生成一个你可能更熟悉的 `Makefile`。
如果你不熟悉 `Make`，请先阅读 [Makefile 教程][makefile-tutorial]
或 [在 Y 分钟内学会 Make][learn-make-in-y-minutes]，
然后仔细阅读 `lab1/Makefile` 文件。
请确保你能够熟练地在本次实验中使用 `Makefile`。

##### 步骤 3.

查看 Makefile，了解用于运行 <a href="https://github.com/google/AFL">AFL</a> 和 <a href="https://clang-analyzer.llvm.org/">CSA</a> 的命令。

```sh
# 使用 AFL 编译程序
AFL_DONT_OPTIMIZE=1 afl-gcc c_programs/test1.c -o test1
# 设置内核将崩溃信息转储到 AFL 的 "core" 文件中
echo core >/proc/sys/kernel/core_pattern
# 在 test1 上运行 AFL 30 秒
timeout 30s afl-fuzz -i afl_input -o afl_output -- ./test1

# 在 test1.c 上运行 CSA
clang -v --analyze c_programs/test1.c
```

### 实验指导

在本实验中，你将在一系列 C 程序上运行 AFL 和 CSA，
研究这两个工具的输出结果，并报告你的发现。

##### 步骤 1.

在 `lab1/c_programs` 目录下的所有 C 程序上运行提供的分析工具 AFL 和 CSA。
为此，只需运行以下命令，
该命令首先对每个程序运行 AFL（超时时间为 30 秒），
然后运行 CSA。

```sh
/lab1$ make check_versions && make all
```

运行上述命令后，你将看到类似如下的输出：

```
AFL_DONT_OPTIMIZE=1 afl-gcc c_programs/test1.c -o ...
timeout 30s afl-fuzz -i afl_input -o ...
Makefile:8: recipe for target 'results/afl_logs/test1/out.txt' failed
make: [results/afl_logs/test1/out.txt] Error 124 (ignored)
clang -v --analyze c_programs/test1.c ...
...
```

请忽略上面 Make 报告的错误；这是正常的，因为
AFL 会一直运行，直到被 timeout 命令强制终止。
你可以随意尝试更改当前设置为 30 秒的超时时间。
我们不期望每个人都报告相同的结果，因为
AFL 本身是非确定性的。

运行 make 命令后，应在 `lab1/results` 目录下生成以下文件和目录：

```
   ├── afl_logs/
   │   ├── test0/
   │   │   ├── out.txt
   │   │   ├── afl_output/
   │   │   └── test0
   │   ├── ... // test1 类似
   │   ...
   │
   └── csa_logs/
       ├── test0_out.txt
       ├── ... // test1 类似
       ...
```

##### 步骤 2.

确定这些 C 程序在除零错误方面的真实情况（`正确` vs. `错误`）。
具体来说，对于每个程序中的每条除法指令，通过检查程序来确定
是否存在某些程序输入会导致除零错误。
将你的答案填写在文件 `lab1/answers.txt` 中每个测试表格的“真实情况”列。

##### 步骤 3.

研究 AFL 和 CSA 的输出，确定它们对每个程序是接受还是拒绝。
将你的答案填写在文件 `lab1/answers.txt` 中每个测试程序表格的相应列。

AFL 发现的导致崩溃的输入存储在 `lab1/results/afl_logs/<test-name>/afl_output/crashes/` 目录下的单独文件中。
这些文件具有独特的名称，形式如 `id:000000,sig:08,src:000000,op:arith8,pos:2,val:-8`[^1]。
这些文件的内容正是 AFL 在遇到崩溃时用作测试程序输入的数据。

检查 CSA 的输出时，如果出现 `core.DivideZero` 警告，则表示 CSA 检测到了除零错误。

例如：

```c
c_programs/test9.c:10:17: warning: Division by zero [core.DivideZero]
   10 |   int avg = sum / len;
      |             ~~~~^~~~~
```

##### 步骤 4.

使用你在步骤 2 和步骤 3 中填写的内容，计算每一列的
精确率（Precision）、召回率（Recall）和 F1 分数（F1 Score）。
将它们填入 `lab1/answers.txt` 的相应行中。

##### 步骤 5.

借助你填写的表格，回答 `answers.txt` 中的问题。

### 提交

完成实验后，通过提交并推送 `lab1/` 下的更改来提交你的结果。
请注意，请在*你的本地机器*上提交结果，而不是在 Docker 中的远程机器上。
具体来说，你需要提交 CSA 和 AFL 在 `lab1/results` 中生成的结果以及你的答案表 `answers.txt`。

```
   lab1$ git add results/ answers.txt
   lab1$ git commit -m "你的提交信息"
   lab1$ git push
```

[^1]: 文件名编码了多种信息，例如崩溃输入的 ID、崩溃信号、产生此崩溃输入的非崩溃种子输入（在我们的例子中始终是文件 lab1/afl_input/seed.txt），以及将非崩溃种子输入转换为该崩溃输入所执行的操作。

[cmake-tutorial]: https://cmake.org/cmake/help/latest/guide/tutorial/index.html
[makefile-tutorial]: https://www.gnu.org/software/make/manual/html_node/Simple-Makefile.html
[learn-make-in-y-minutes]: https://learnxinyminutes.com/docs/make

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

## 构建一个模糊测试器

构建一个覆盖引导的随机输入生成器（即"模糊测试器"），用于测试 C 程序。

### 目标

在本实验中，你将开发一个用于测试 C 程序的_模糊测试器_。
模糊测试是一种流行的软件测试技术，它会向被测程序输入随机生成的输入。
这类输入有助于发现程序中各种与安全相关和导致崩溃的 bug。
为此，你的模糊测试器将从种子输入开始，并通过变异之前的输入来生成新输入。
它将使用前几轮测试的输出作为_反馈_，来指导后续的测试生成。
你将使用在 `lab2` 中看到的代码覆盖率指标，来帮助选择供模糊测试器变异的_有趣_输入。

### 环境搭建

Lab3 的代码位于 `/lab3` 目录下。
在描述实验的文件位置时，我们会经常将 Lab 3 的顶级目录称为 `lab3`。
请在 VSCode 中打开 `lab3` 目录。

本实验建立在 `lab2` 的代码覆盖率插桩基础之上。
我们在 `lab3/src` 中提供了一个 `Instrument.cpp` 文件；
它包含两个插桩功能，即覆盖率插桩和 sanitize 插桩。
你在上一个实验中已经见过代码覆盖率插桩，这里的实现与它完全相同。
在 `lab1` 中，你已经看到，当程序遇到除零错误时，会引发浮点异常并导致核心转储。
sanitizer 插桩会在每个除法指令之前插入对 `__sanitize__` 函数的调用。
如果分母为零，该函数会以返回码 `1` 优雅地退出程序，否则程序继续正常运行。

##### 步骤 1.

模糊测试器和插桩功能是使用 CMake 构建的，你可以运行以下命令来构建它们：

```sh
lab3$ mkdir build && cd build
lab3/build$ cmake ..
lab3/build$ make
```

运行 `make` 后，你应该会在 `lab3/build` 中看到 `InstrumentPass.so` 和 `fuzzer`。
`fuzzer` 是一个工具，它会将（你将生成的）随机化输入提供给一个经过插桩的 C 程序，该程序在遇到除零错误时会优雅退出，并在执行期间报告代码覆盖率。

##### 步骤 2.

接下来，我们想要准备一个测试程序，用 `fuzzer` 对其进行模糊测试。
这需要先对程序进行插桩，类似于 `lab2`。
因此，要对程序 `sanity1.c` 进行插桩和构建，你可以运行：

```sh
lab3/test$ clang-19 -emit-llvm -S -fno-discard-value-names -O0 -Xclang -disable-O0-optnone -c -o sanity1.ll sanity1.c -g
lab3/test$ opt-19 -load-pass-plugin ../build/InstrumentPass.so -passes="InstrumentPass" -S sanity1.ll -o sanity1.instrumented.ll
lab3/test$ clang-19 -o sanity1 -L${PWD}/../build -lruntime -lm sanity1.instrumented.ll
```

或者，你也可以使用提供的 `Makefile` 来完成同样的操作：

```sh
lab3/test$ make sanity1  # 仅对 sanity1 进行插桩和构建。
lab3/test$ make all      # 对所有程序进行插桩和构建。
```

##### 步骤 3.

现在，要运行 `fuzzer`，你需要创建输出目录，模糊测试器将把结果存储在其中。

```sh
lab3/test$ mkdir fuzz_output_sanity1
```

你可能还记得 `lab1` 中，AFL 可以永远生成新输入，永不停止运行。
你的模糊测试器也是如此。
因此，我们将使用 `timeout` 在指定时间后停止模糊测试器。

之后，你可以运行模糊测试器对 sanity 进行 10 秒的测试：

```sh
lab3/test$ timeout 10s ../build/fuzzer ./sanity1 fuzz_input fuzz_output_sanity1
```

**注意：** `sanity1` 前面的 `./` 是必需的，以便让模糊测试器找到可执行文件。

你也可以使用 Makefile 来设置输出目录并为你运行模糊测试器：

```sh
lab3/test$ make fuzz-sanity1
```

这将在 `sanity1` 上运行 `fuzzer` 十秒钟，并将结果存储到 `lab3/test/fuzz_output_sanity1`。
此外，它将使用 `lab3/config.txt` 来设置 `seed`（用于生成随机数）和 `freq`（决定我们将非崩溃输入写入输出的频率，值越大频率越低）。
由于我们预计会看到更多非崩溃输入，因此使用 `freq` 来控制记录非崩溃输入的频率。

一旦你运行了 `fuzzer`，你应该会看到 `failure` 目录中填充了几个随机生成的、会导致 `sanity1.c` 崩溃的输入。
你可能还会在 `success` 目录下看到一些不会导致崩溃的随机生成输入。

```
fuzz_output_sanity1
├── success         # 部分生成的、未导致崩溃的输入。
│   ├── input0
│   └──  ...
├── randomSeed.txt  # 用于生成随机数的种子。
└── failure         # 所有生成的、导致崩溃的输入。
    ├── input0
    ├── input1
    │    ...
    └── inputN
```

这里 `N` 是在超时前最后一个导致崩溃的案例。

### 实验说明

一个功能完备的模糊测试器包含三个关键特性：

1.  生成符合程序输入语法的测试用例，
2.  变异测试输入以增加代码覆盖率的策略，
3.  帮助驱动所用变异类型的反馈机制。

##### 基于变异的模糊测试入门

考虑以下从命令行读取字符串输入的代码：

```c
int main() {
  char input[65536];
  fgets(input, sizeof(input), stdin);
  int x = 13;
  int z = 21;

  if (strlen(input) % 13 == 0) {
    z = x / 0;
  }

  if (strlen(input) > 100 && input[25] == 'a') {
    z = x / 0;
  }

  return 0;
}
```

程序中有两个非常明显的导致除零错误的情况：

+   如果程序输入的长度能被 13 整除，或者
+   如果输入长度大于 100 且字符串中的第 25 个字符是 `a`。

现在，让我们假设这个程序是一个黑盒，我们只能通过使用不同输入运行代码来搜索错误。

我们可能会尝试一个随机字符串，比如 `"abcdef"`，这会使程序成功运行。
然后，我们可以将第一个字符串作为起点，添加一些新字符，比如 `"ghi"`，得到 `"abcdefghi"`。
这里我们变异了原始输入字符串以生成一个新的测试用例。
我们可能会重复这个过程，最终偶然发现 `"abcdefghijklm"`，它长度能被 13 整除，导致程序崩溃。

第二个情况呢？
我们可以不断在字符串末尾插入字符，最终会得到一个满足 if 语句第一个条件（输入长度大于 100）的大字符串，但我们需要执行另一种类型的变异——随机改变字符串中的字符——才能最终满足 if 语句中的第二个条件。

通过对输入字符串使用各种变异，我们能够穷尽所有程序执行路径，也就是说，输入中更多样化的变异增加了我们的代码覆盖率。
在最简单的形式中，这正是模糊测试器所做的。
你可以查阅《模糊测试手册》中的[基于变异的模糊测试][fuzzing-book-mutaion]章节。

##### 反馈引导的模糊测试

我们已经看到随机化测试如何能够发现 bug，并且是一种有用的软件分析工具。
上一节描述了一种暴力生成测试用例的方法；我们只是执行随机变异，希望找到 bug。
这导致许多测试用例是冗余的，因此是不必要的。

我们可以收集关于程序执行的额外信息，并将其作为_反馈_提供给我们的模糊测试器。
下图从高层次展示了这个过程：

<img src="../images/feedback.png"
  alt="反馈引导的模糊测试"
  style="width: 45vw;min-width: 600px;margin: 10px auto 20px; display: block;">

生成新的、有趣的种子是反馈引导模糊测试的目标。
_有趣_是什么意思？
我们可能会考虑一个测试是否增加了代码覆盖率。
如果是这样，我们就发现了想要继续探索的新执行路径。
另一个测试可能会显著增加程序运行时间，在这种情况下，我们可能会发现一些潜在的性能 bug。
在这两种情况下，测试都增加了我们对程序的了解；
因此，我们将这些测试插入到种子集合中，并将它们用作未来测试生成的起点。

**注意：** 对于反馈机制设计，如果新变异的输入增强了覆盖率，你可以将原始输入和新变异的输入都添加到种子输入池中，用于后续的变异周期。

```python
# 反馈机制
for input in seed_pool:
    mutated_input = mutate(input)
    if enhances_coverage(mutated_input):
        # 将原始输入和变异输入都添加到种子池
        seed_pool.extend([input, mutated_input])
```

##### 构建模糊测试器

在本实验中，你将修改 `src/Fuzzer.cpp` 来构建一个覆盖引导的模糊测试器。
你需要实现一些不同的变异函数，变异函数接收一个字符串，对其执行一些变异，并返回变异后的字符串。
你必须决定选择哪些变异策略，并在 `selectMutationFn` 中实现你的逻辑。
查看 `src/test/` 中的测试程序可能有助于了解你的模糊测试器需要探索哪些类型的程序才能找到 bug，以及你可能想要执行哪些类型的变异。

模糊测试器将从读取命令行指定的输入目录中的输入文件开始，以初始化 `SeedInputs` 向量。
之后，它需要从 `SeedInputs` 向量中选择一个特定的输入，以及一个将用于变异它的变异函数。
为此，你需要分别为 `selectInput` 和 `selectMutationFn` 实现你的逻辑。
一旦模糊测试器选择了一个输入和一个变异函数，它就会变异该输入。
变异后的输入将在目标程序上运行，并根据该次运行的覆盖率提供反馈。
利用这个覆盖率，你将决定这是否是一个_有趣_的种子，如果是，则将其插入到 `SeedInput` 向量中。
这使得变异后的输入可以在以后被选中并进一步变异。
这个过程一直持续，直到模糊测试器被中断（通过超时，或在终端上按 Ctrl+C）。

以下伪代码说明了这个逻辑：

```
readSeedInputs(SeedInputs)  // 初始化 SeedInputs

while (true) {
  input <- selectInput()                  // 选择种子输入
  mutation <- selectMutationFn()          // 选择变异函数
  mutatedInput <- mutation(input)         // 变异输入
  test(Target, MutatedInput)              // 使用变异后的输入运行目标程序
  feedBack(Target, MutatedInput);         // 从运行中获取反馈
}
```

请参考 `src/Fuzzer.cpp` 中的 `fuzz` 函数来了解此逻辑的实现。

##### 可能的变异

以下是你的变异的一些潜在建议列表：

+   用随机值替换字节。
+   交换相邻字节。
+   遍历每个字节的所有可能值。
+   删除一个随机字节。
+   插入一个随机字节。

随意尝试其他变异，看看是否能加快在二进制文件上搜索 bug 的速度。
你可以使用 C++ 函数 `rand()` 来生成随机整数。

**注意：** 为了使变异函数更通用，你可以从一个临时版本开始。例如，一个专门插入换行符的版本。最初，这个仅限于添加换行符的函数是临时性的。要使其通用化，从仅插入换行符过渡到包含一系列随机字符。

你会注意到，不同的程序需要不同的策略，或者在某些情况下，你甚至可能需要在模糊测试过程中切换不同的变异策略。
我们期望你包含一种机制，该机制将尝试根据覆盖率反馈为输入程序选择最佳策略。

##### 任务概览

本实验在 `Fuzzer.cpp` 中包含以下任务：

1.  为 `selectInput` 函数实现你的逻辑，该函数从 `SeedInputs` 向量中选择一个变异字符串。
2.  实现你认为有助于你的模糊测试器生成丰富多样字符串的变异函数。
    从前面提到的变异列表中获取灵感。
3.  为 `selectMutationFn` 实现你的逻辑，以决定选择哪个变异函数。
4.  在 `feedback` 中，根据程序的成功或失败以及代码覆盖率，决定变异是否有趣。
    同样，你可以遵循我们的基础框架并填写 `feedback`。
5.  将一个有趣的变异插入到 `SeedInput` 池中，以驱动进一步的变异。

需要记住的一点是，这些任务都不是强制要求的，你的模糊测试器可以使用我们为其中一些任务提供的默认实现，只要它满足评分要求，仍然可以获得满分。

##### 代码覆盖率指标

回想一下，你有一种方法可以使用插桩输出的覆盖率信息来检查特定程序的执行程度。
在被模糊测试的程序的工作目录中会生成一个 `.cov` 文件。这个文件会被读取，并通过 `feedback` 函数内部的 `RawCoverageData` 变量提供给你。
然后你可以使用它来决定某个特定的变异是否有趣。

##### 一些小贴士

在开始之前，请通读 `Fuzzer.cpp` 文件中的注释、提示和说明，以便更好地理解各部分是如何组合在一起的。

从小处着手。
一次实现一种变异策略，先尝试让较简单的测试用例崩溃，然后再处理较难的。
一旦成功，你就可以继续实现更多策略，以及基于你获得的反馈在它们之间进行选择的更复杂方法。

不要害怕在模糊测试的轮次之间跟踪任何状态。

你可能想先尝试每种变异策略，看看哪一种能生成增加代码覆盖率的测试，然后利用该策略。

##### 评分

我们期望你的模糊测试器能够为我们在 `lab3/test` 中提供的所有程序生成崩溃输入。

除此之外，我们还将对十个隐藏的测试程序测试你的模糊测试器。
这些程序为你的模糊测试器提供了更具挑战性的测试用例。
要在隐藏测试中获得满分，你的模糊测试器应该能够在其中至少七个中找到崩溃输入。

### 提交

完成实验后，通过提交并推送 `lab3/` 下的更改来提交你的代码。具体来说，你需要提交对 `src/Fuzzer.cpp` 的更改。

```sh
lab3$ git add src/Fuzzer.cpp
lab3$ git commit -m "你的提交信息"
lab3$ git push
```

如果你希望我们在评分时为你的模糊测试器使用特定的种子值，请使用你希望我们使用的种子值更新 `lab3/config.txt`。所有测试用例将使用相同的种子值。如果你这样做，你需要提交对 `lab3/config.txt` 的更改。


[fuzzing-book-mutaion]: https://fuzzingbook.org/html/MutationFuzzer.html

# 基于性质的测试

使用基于性质的测试来验证二叉搜索树的实现。

## 目标

在本实验中，你将应用基于性质的测试，基于 [Hypothesis](https://github.com/HypothesisWorks/hypothesis) 来验证二叉搜索树的实现。Hypothesis 是 Python 中一个流行的基于性质的测试工具。通过本实验，你将学习如何定义不同形式的性质以进行有效的测试。

## 环境配置

请在你的实验环境中安装 Python 包 `pytest` 和 `hypothesis`：

```bash
lab4$ pip install -r requirements.txt  # 安装所需的包
```

## 前置知识

### 二叉搜索树 (BST)

二叉搜索树是一种具有特定排序性质的带根二叉树，这些性质使其能够高效地执行插入、删除和搜索操作。

对于树中的每个节点：

1. 其左子树中所有节点的键都小于该节点自身的键。
2. 其右子树中所有节点的键都大于该节点自身的键。
3. 键通常是唯一的。

因此，中序遍历——按照左、根、右的顺序访问节点——总是会产生严格升序的键序列，如下例所示。

<div align="center">
<img src="../images/lab4-bst-example1.png"
  style="height: auto; width: 50%">
</div>

在本实验中，`lab4/src/BST.py` 给出了二叉搜索树的实现。该 BST 实现支持任何可比较类型的键和任何类型的值，以及四个核心操作 `insert`、`delete`、`find` 和 `union`。请仔细阅读代码以理解其实现。

### Hypothesis

Hypothesis 是一个实现了基于性质的测试的 Python 库。基于性质的测试根据给定的某些性质来验证函数（或模块，甚至系统）的正确性。它使用大量自动生成的测试用例，而不是单个测试用例，来有效地对函数进行压力测试。如果发现某些性质被违反，它会缩小并返回反例输入。

在下面的代码中，我们展示了如何使用经典的*基于示例的测试*来测试一个 `sort` 函数（参见 `test_sort_by_example`），以及如何使用*基于性质的测试*（基于 Hypothesis，参见 `test_sort_by_property`）来测试这个 `sort` 函数。这里，这个 `sort` 函数按升序对数字进行排序。

```python
# 基于示例的测试
def test_sort_by_example():
    input_list = [3, 1, -1] # 输入单个测试用例
    output = sort(input_list)
    expected_output = [-1, 1, 3]
    assert output == expected_output # 检查单个输出
    
# 基于 Hypothesis 的基于性质的测试
# 自动生成包含 0 到 1000 个元素的随机整数列表。
@given(st.lists(st.integers(), min_size=0, max_size=1000))
def test_sort_by_property(input_list):
    # 前置条件
    assume(len(input_list) > 1)
    
	sorted_list = sort(input_list)
    # 后置条件：验证排序性质成立
    for i in range(len(sorted_list) - 1):
        assert sorted_list[i] <= sorted_list[i + 1]
```

#### 策略

Hypothesis 中的策略是数据生成器，它们自动为你的基于性质的测试创建多样化的测试输入（具有不同的类型和形式）。

```python
from hypothesis import strategies as st

# 基本类型
st.integers()           # 整数
st.floats()             # 浮点数  
st.text()               # 文本
st.booleans()           # 布尔值

# 复杂类型
st.lists(st.integers()) # 整数列表
st.dictionaries(st.text(), st.integers())  # 字典
st.tuples(st.integers(), st.text())        # 元组

# 自定义策略
st.one_of(st.integers(), st.text())        # 多种类型中的一种
```

在本实验中，`lab4/src/test_strategies.py` 已经实现了两个策略，即 `keys_strategy` 和 `trees_strategy`：

```python
keys_strategy = st.one_of(st.integers(min_value = -25, max_value = 25), st.integers())

def build_bst_from_tuples(kv_list: List[Tuple[int,int]]) -> BST[int,int]:
    bst: BST[int,int] = BST.nil()
    for k, v in kv_list:
        bst = bst.insert(k, v)
    return bst

trees_strategy = st.lists(
    st.tuples(keys_strategy, st.integers()),
    min_size = 0,
    max_size = 50,
    unique_by = lambda kv: kv[0]
).map(build_bst_from_tuples)
```

+ `keys_strategy`：它从受限范围 [-25, 25] 或完整的整数范围内随机选择一个键。

> 设计目的是：(1) 受限范围 (-25 到 25) 增加了键冲突（同一个键出现多次）的概率，以模拟 BST 的真实使用场景；(2) 完整范围确保你也能用多样化、间隔大的键进行测试。这种设计通过在冲突场景和一般情况之间取得平衡，使测试更有效。

+ `trees_strategy`：它生成最多包含 50 个 (键, 值) 对的随机 BST 对象，并且键是唯一的。

> 在内部，此策略使用 `insert` 操作添加带有 (键, 值) 的节点并构建 BST。

#### 缩小

Hypothesis 的一个关键特性是缩小。如果一个测试用例失败，它不会仅仅报告原始的复杂输入。相反，它会智能地将该输入简化为仍然导致失败的最小形式，从而更容易识别根本问题。

### Pytest

Pytest 是一个强大的 Python 测试框架，它简化了测试的创建和执行。它具有自动测试发现、全面的错误报告和丰富的插件生态系统。

为了让你熟悉 Pytest，你可以在 `lab4/tests` 目录下运行 `lab4/tests/simple_test.py`，它测试了 BST 的一个有 bug 的版本（对应于 `lab4/bugs/bug1.py`）：

```bash
lab4/tests$ pytest simple_test.py -q --tb=no # 简洁的输出结果
```

你将获得以下测试结果，表明 3 个测试失败，8 个测试通过：

```tex
$ pytest simple_test.py -q --tb=no
...F..F..F.                                                                        [100%]
================================ short test summary info =================================
FAILED simple_test.py::test_three_inserted_values_can_be_found - AssertionError: assert None == 'twenty'
FAILED simple_test.py::test_a_deleted_value_can_no_longer_be_found - AssertionError: assert None == 'twenty'
FAILED simple_test.py::test_union_of_two_bsts_contains_keys_of_both - AssertionError: assert {(1, 'one'), ..., (5, 'five')} == {(1, 'one'), ..., (5, 'five')}
3 failed, 8 passed in 0.09s
```

如果你想获得详细结果，可以运行：

```bash
lab4/tests$ pytest simple_test.py -v --tb=short # 详细的输出结果
```

## 实验说明

### 项目结构

```tex
.
|-- bugs
|   |-- __init__.py
|   |-- bug1.py     # 在 find 和 union 中植入了 bug，旨在被 test1.py 发现
|   |-- bug2.py     # 在 delete 和 union 中植入了 bug，旨在被 test2.py 发现
|   |-- bug3.py     # 在 delete 中植入了 bug，旨在被 test3.py 发现
|   `-- bug4.py     # 在 delete 和 union 中植入了 bug，旨在被 test4.py 发现
|-- requirements.txt
|-- src
|   |-- BST.py               # BST 数据结构的正确实现
|   |-- BSTUtils.py          # 工具函数
|   |-- __init__.py
|   `-- test_strategies.py   # Hypothesis 的测试策略
`-- tests
    |-- conftest.py      # 运行时环境配置和测试报告生成
    |-- hypothesis.ini   # Hypothesis 配置
    |-- makefile         # 运行脚本，包括 all, clean, test1, test2, test3, test4
    |-- simple_test.py   # BST 的简单测试
    |-- test1.py         # TODO1：为测试 find 和 delete 定义有效性性质。
    |-- test2.py         # TODO2：为测试 delete 和 union 定义后置条件性质。
    |-- test3.py         # TODO3：为测试 delete 和 union 定义蜕变性质。
    `-- test4.py         # TODO4：为测试 delete 和 union 定义基于模型的性质。
```

### BST 中的性质与植入的 Bug

在本实验中，你将在验证 BST 的背景下学习并定义以下四种类型的性质。你需要定义不同的性质来捕获我们植入到 BST 中的 bug。玩得开心！

| 性质类型           | 目标方法       | 要识别的 Bug | Bug 描述                                                     |
| :----------------- | :------------- | :------------ | :----------------------------------------------------------- |
| 有效性性质         | `find`, `union`   | bug1.py - BUG(1) | 在 `find(key)` 中：错误地将左子树赋给了右子树 |
|                    |                | bug1.py - BUG(2) | 在 `union(bst1, bst2)` 中：错误地将 bst1 作为 bst2 的左子树 |
| 后置条件性质       | `delete`, `union` | bug2.py - BUG(1) | 在 `delete(key)` 中：错误地选择了搜索方向。      |
|                    |                | bug2.py - BUG(2) | 在 `union` 中：当 bst1 和 bst2 的键相同时，错误地优先考虑 bst2 |
| 蜕变性质           | `delete`, `union` | bug3.py - BUG(1) | 在 `delete(key)` 中：错误地选择了搜索方向。      |
| 基于模型的性质     | `delete`, `union` | bug4.py - BUG(1) | 在 `delete(key)` 中：错误地选择了要删除的子树 |
|                    |                | bug4.py - BUG(2) | 在 `union(bst1, bst2)` 中：当 bst1 和 bst2 的键相同时，错误地优先考虑 bst2 |

### 有效性性质

无论执行了哪个操作（`insert`、`delete`、`find` 和 `union`），二叉搜索树都应始终满足一个有效性性质：*树中的键应该是有序的*——对于树中的每个节点，(1) 其左子树中所有节点的键都小于该节点自身的键，(2) 其右子树中所有节点的键都大于该节点自身的键。

例如，我们可以使用此有效性性质来检查执行 `insert` 和 `delete` 操作后 BST 的有效性。

```python
# 空树是一棵有效的二叉搜索树。
def test_nil_valid() -> None:
    assert is_valid(BST.nil())

# 插入一个键值对后，结果仍然是一棵有效的 BST。
@given(keys_strategy, st.integers(), trees_strategy)
def test_insert_valid(key: int, value: int, bst: BST[int,int]) -> None:
    assert is_valid(bst.insert(key, value))

# 删除一个键后，结果仍然是一棵有效的 BST。
@given(keys_strategy, trees_strategy)
def test_delete_valid(key: int, bst: BST[int,int]) -> None:
    assert is_valid(bst.delete(key))
```

#### TODO1

(1) 在本节中，你需要在 `lab4/src/BSTUtils.py` 中定义上述有效性性质，该性质检查 BST 中的键是否始终有序。你可以在代码注释中找到一些提示。

(2) 基于你定义的有效性性质，你需要在 `lab4/tests/test1.py` 中编写相关代码，分别检查两个核心操作 `find` 和 `union` 是否遵守有效性性质。你可以在代码注释中找到一些提示。

之后，你可以运行以下命令来确认有效性性质是否能成功找到 `lab4/bugs/bug1.py` 中植入的两个 bug。

```bash
lab4/tests$ make test1

# 如果你想要更详细的输出结果
lab4/tests$ pytest -v test1.py --tb=short
```

你应该获得以下测试结果，并可以在 `lab4/tests/report/test1` 中找到缩小的测试：

```tex
Run Validity Testing (test1.py)...
....FF
FAILED test1.py::test_find_valid - assert False
FAILED test1.py::test_union_valid - assert False
2 failed, 4 passed in 1.38s
```

### 后置条件性质

后置条件是在函数/操作完成执行后必须为真的性质或条件。它描述了函数完成时的保证状态或结果。例如，在执行 `insert` 操作后，刚刚插入的键应该存在，并且任何原始键应该保持不变。

```python
# 插入操作不应影响其他键（包括自身）的搜索结果。
@given(keys_strategy, st.integers(), trees_strategy, keys_strategy)
def test_insert_post(key: int, value: int, bst: BST[int,int], search_key:int) -> None:
    found = bst.insert(key, value).find(search_key)
    expected = value if key == search_key else bst.find(search_key)
    assert found == expected
```

对于 `find` 操作，我们也可以提出一些后置条件性质。我们知道，如果我们刚刚插入了一个键，那么树中必须包含该键。同样，如果我们刚刚删除了一个键，那么树中不应该包含该键。因此，我们可以为 `find` 编写两个后置条件性质：

```python
# 插入后，查找应返回插入的值。
@given(st.integers(), st.integers(), trees_strategy)
def test_find_post_present(key: int, value: int, bst: BST[int,int]) -> None:
    assert bst.insert(key, value).find(key) == value

# 删除后，查找应返回 None。
@given(st.integers(), trees_strategy)
def test_find_post_absent(key: int, bst: BST[int,int]) -> None:
    assert bst.delete(key).find(key) is None
```

#### TODO2

你需要在 `lab4/tests/test2.py` 中分别为两个核心操作 `delete` 和 `union` 定义一些后置条件性质。你可以在代码注释中找到一些提示。

之后，你可以运行以下命令来确认你的性质是否能成功找到 `lab4/bugs/bug2.py` 中植入的两个 bug。

```bash
lab4/tests$ make test2

# 如果你想要更详细的输出结果
lab4/tests$ pytest -v test2.py --tb=short
```

你应该获得以下测试结果，并可以在 `lab4/tests/report/test2` 中找到缩小的测试：

```bash
Run Postconditions Testing (test2.py)...
.F.FF                                                                                       
FAILED test2.py::test_find_post_absent - assert 0 is None
FAILED test2.py::test_delete_post - assert 0 == None
FAILED test2.py::test_union_post - assert 1 == 0
3 failed, 2 passed in 4.10s
```

### 蜕变性质

蜕变测试是在许多上下文中解决 Oracle 问题的一种成功方法。基本思想是：即使可能难以预测函数调用（如 `insert(key, value)`）的预期结果，我们仍然可以表达此结果与相关调用的结果之间的预期关系。例如，如果在调用 `insert(key, value)` 之前向 BST 中插入一个额外的键，我们期望该额外的键也出现在最终的 BST 中。我们将这种蜕变关系形式化为以下蜕变性质：

```python
# 在 (key1, value1) 和 (key2, value2) 上的两个 insert 操作与其预期结果之间的蜕变关系
# 如果键相同，则插入 value2（而不是 value1）；否则，同时插入 value1 和 value2。
# 等效函数，判断两个 BST 在包含的 (键, 值) 对方面是否等效，忽略树结构之间的差异。
@given(keys_strategy, st.integers(), keys_strategy, st.integers(), trees_strategy)
def test_insert_metamorph_by_insert(key1: int, value1: int, key2: int, value2: int, bst: BST[int,int]) -> None:
    inserted = bst.insert(key1, value1).insert(key2, value2)
    expected = bst.insert(key2, value2) if key1 == key2 else bst.insert(key2, value2).insert(key1, value1)
    assert equivalent(inserted, expected)
```

你可能想知道为什么我们需要在前面的性质中检查 key1 和 key2 是否相同。原因是 `insert` 操作遵循*后插入者获胜*的原则。因此，以下蜕变关系是有 bug 的，可能会导致测试中的误报。

```python
@given(keys_strategy, st.integers(), keys_strategy, st.integers(), trees_strategy)
def test_insert_metamorph_by_insert(key1: int, value1: int, key2: int, value2: int, bst: BST[int,int]) -> None:
    inserted = bst.insert(key1, value1).insert(key2, value2)
    # 未考虑 value1 和 value2 的优先级。
    expected = bst.insert(key2, value2).insert(key1, value1)
    assert equivalent(inserted, expected)
```

#### TODO3

(1) 在本节中，你需要在 `lab4/src/BSTUtils.py` 中定义 `equivalent` 函数，该函数检查两个 BST 在包含的 (键, 值) 对方面是否等效，忽略树结构之间的差异。你可以在代码注释中找到一些提示。

(2) 基于你实现的 `equivalent` 函数，你需要在 `lab4/tests/test3.py` 中分别为操作 `delete` 和 `union` 提出一些蜕变性质，以识别 `lab4/bugs/bug3.py` 中植入的一个 bug。你可以在代码注释中找到一些提示。

之后，你可以运行以下命令来确认你的性质是否能成功找到 `lab4/bugs/bug3.py` 中植入的一个 bug。请注意，我们只在 `delete` 中植入了一个 bug，`union` 是正确的，没有 bug。如果你的性质在 `union` 中发现了 bug，你可能需要仔细检查你的性质定义是否正确。

```python
lab4/tests$ make test3

# 如果你想要更详细的输出结果
lab4/tests$ pytest -v test3.py --tb=short
```

你应该获得以下结果，并可以在 `lab4/tests/report/test3` 中找到缩小的测试：

```tex
Run Metamorphic Testing (test3.py)...
.F.                                                                                         
FAILED test3.py::test_delete_metamorph_by_insert - assert False
1 failed, 2 passed in 2.62s
```

### 基于模型的性质

1972 年，Tony Hoare 提出了一种证明*数据表示*正确性的方法（参考 *C. A. Hoare. Proof of correctness of data representations. Acta Inf., 1(4):271–281, December 1972*），通过使用*抽象函数*将它们与*抽象数据*联系起来。

在本实验中：

+ 数据表示：BST
+ 抽象函数：`BST::to_list()`
+ 抽象数据：List[Tuple[K,V]]

基于模型的性质通过单次调用来测试单个函数，并将其结果与应用于相关抽象参数的相关*抽象操作*的结果进行比较。*抽象函数*将真实的、具体的参数和结果映射到抽象值，我们也称之为*模型*。

```python
def to_list(self) -> List[Tuple[K,V]]:
        if self.is_leaf():
            return []
        return [self._entry] + self.get_left().to_list()  + self.get_right().to_list()
```

以 `insert` 操作为例：

<div align="center">
<img src="../images/lab4-model-based-property-example.png"
  style="height: auto; width: 50%">
</div>

向 BST 中插入数据应该产生一个与向抽象数据中插入数据等效的集合。

```python
@given(keys_strategy, st.integers(), trees_strategy)
def test_insert_model(key: int, value: int, bst: BST[int,int]) -> None:
    abstract_data = bst.to_list()
    inserted_abstract_data = abstract_data.copy()
    flag = False
    for i, (k, v) in enumerate(inserted_abstract_data):
        if k == key:
            True
            inserted_abstract_data[i] = (key, value)
            break
    if flag is False:
        inserted_abstract_data += [(key, value)]
    inserted_bst = bst.insert(key, value)
    assert set(inserted_bst.to_list()) == set(inserted_abstract_data)
```

#### TODO4

按照上面关于 `insert` 的示例，你需要分别为操作 `delete` 和 `union` 定义一些基于模型的性质，以识别 `lab4/bugs/bug4.py` 中植入的两个 bug：

+ 对于 `delete`，你可以对 BST 和一个抽象数据结构（例如，一个 `list`）执行 `delete` 操作，以确定最终的集合是否等效。

+ 对于 `union`，你可以对两个 BST 及其对应的抽象数据结构（例如，两个 `list`）执行 `union` 操作，以确定最终的集合是否等效。

之后，你可以运行以下命令来确认你的性质是否能成功找到 `lab4/bugs/bug4.py` 中植入的两个 bug。

```python
lab4/tests$ make test4

# 如果你想要更详细的输出结果
lab4/tests$ pytest -v test4.py --tb=short
```

你应该获得以下结果，并可以在 `lab4/tests/report/test4` 中找到缩小的测试：

```bash
Run Model-based Properties Testing (test4.py)...
..FF                                                                                      
FAILED test4.py::test_delete_model - assert {(0, 0), (1, 0)} == {(1, 0)}
FAILED test4.py::test_union_model - assert {(0, 1)} == {(0, 0)}
2 failed, 2 passed in 0.99s
```

## 提交

*注意：我们将验证你提交的代码是否针对 bug。如果你的代码是针对 bug 的，你的分数可能会相应地被扣减。*

完成实验后，通过提交并推送 `lab4/` 下的更改来提交你的代码。具体来说，你需要提交对 `lab4/src/BSTUtils.py`、`lab4/tests/test1.py`、`lab4/tests/test2.py`、`lab4/tests/test3.py`、`lab4/tests/test4.py` 的更改。

```bash
   lab4$ git add src/BSTUtils.py tests/test1.py tests/test2.py tests/test3.py tests/test4.py
   lab4$ git commit -m "你的提交信息"
   lab4$ git push
```

## Delta Debugging

构建一个 delta debugger，用于最小化导致程序崩溃的输入——让用户更容易理解 bug。

### 目标

在本实验中，你将构建一个 delta debugger，实现一种高效算法，用于在给定一个较大的崩溃输入时，找到 1-minimal 的崩溃输入。
你将把这个工具与一个模糊测试器（比如你在 `lab3` 中构建的那个）结合起来，以最小化模糊测试器找到的崩溃输入。

### 环境设置

Lab 4 的代码位于 `/lab5/` 目录下。

本实验建立在之前实验的基础上。
我们为你提供了 `runtime` 库、用于 `coverage` 和 `sanitize` 的 `InstrumentPass` 以及一个 `fuzzer` 可执行文件的预编译二进制文件；你可以在 `lab5/lib` 目录下找到它们。
它们的实现与 `lab3` 中的实现完全相同。

##### 步骤 1.

本实验使用 Python 来实现 delta debugger。
我们通过构建一个名为 `delta_debugger` 的 Python 包来实现。

要构建并安装该包，请运行：

```sh
/lab5$ make install
```

与 `c++` 不同，修改代码后你无需重新运行此命令。
此外，你将能够使用终端中的 `delta-debugger` 命令来使用你的 delta debugger。

`delta-debugger` 工具执行 delta 调试，以将程序的崩溃输入缩小。

##### 步骤 2.

要将 `delta-debugger` 与某个程序一起使用，你首先需要找到一些会导致该程序崩溃的输入。
为了找到这样的输入，我们将使用一个模糊测试器。

和 lab3 一样，要运行 `fuzzer`，你首先需要插桩该程序，并设置合适的输出目录，以便模糊测试器存储其结果。

```sh
/lab5/test$ make sanity1               # 插桩并构建 sanity1。
/lab5/test$ mkdir fuzz_output_sanity1  # 创建输出目录。
# 在 sanity1 上运行模糊测试器，超时时间为 6 秒。
/lab5/test$ timeout 6s ../lib/fuzzer ./sanity1 fuzz_input fuzz_output_sanity1
```

你也可以使用 Makefile 来为你完成插桩、构建、设置输出目录和运行模糊测试器：

```sh
/lab5/test$ make sanity1               # 插桩并构建 sanity1。
/lab5/test$ make fuzz-sanity1          # 在 sanity1 上运行模糊测试器。
```

##### 步骤 3.

运行模糊测试器后，你会在 `test/fuzz_output_sanity1/failure` 目录下找到导致程序崩溃的输入。

```
fuzz_output_sanity1
├── success
├── randomSeed.txt
└── failure                            # 导致崩溃的输入。
    ├── input0
    ├── input1
    │    ...
    └── inputN
```

现在你可以使用 `delta-debugger` 来最小化模糊测试器找到的崩溃输入。

```
/lab5/test$ delta-debugger ./sanity1 fuzz_output_sanity1/failure/input1
```

最后一个参数是崩溃输入的路径，具体取决于你想要最小化哪个输入。
在这个例子中，精简后的输入存储在 `fuzz_output/failure/input1.delta` 中。
此外，在再次调用 `delta-debugger` 之前，请确保清理 `fuzz_output` 目录。

你可以通过运行以下命令来执行清理：

```sh
/lab5/test$ rm -rf fuzz_output_sanity1 && mkdir fuzz_output_sanity1
```

### 实验说明

你需要编辑 `lab5/delta_debugger/delta.py` 文件来构建一个 delta 调试工具。
我们为你提供了一个模板函数——`delta_debug`——用于实现你的最小化逻辑。
`delta_debug` 函数接收一个 `target` 程序，以及一个导致 `target` 崩溃的 `input`，并且应该返回一个仍然会导致 `target` 程序崩溃的 1-minimal 输入。

为了执行 delta 调试，你需要用不同的 `input` 字符串反复运行 `target` 程序。
我们提供了一个 `run_target` 函数来帮助你用某个 `input` 运行 `target` 程序。
如果目标程序没有崩溃，它会返回 0。

```py
def run_target(target: str, input: Union[str, bytes]) -> int:
    """
    使用输入到其标准输入的方式运行目标程序。
    :param target: 要运行的目标程序。
    :param input: 要传递给目标程序的输入。
    :return: 目标程序的返回码。
    """
    ...
```

在本实验中，你将修改 `delta_debug` 函数，以实现你在课堂上学到的算法，从而找到 1-minimal 的崩溃输入。

你可能想要添加一个辅助函数，例如命名为 `_delta_debug`，它接收一个 `target`、一个 `input` 和一个参数 `n`（对应搜索粒度），并执行一次 delta 调试算法的迭代，以返回下一个 `input` 和 `n`。

### 示例输入和输出

你的 delta debugger 应该能够在任何接受来自 `stdin` 输入的可执行文件上运行。

你可以通过传入以下参数来在测试程序上运行 delta debugger：

```sh
delta-debugger ./test crashing-input
```

然后 delta debugger 会将其结果存储在 `crashing-input.delta` 文件中。

举一个具体的例子，考虑字符串："This is theh) "，它会导致 `test2` 失败：

```sh
/lab5/test$ echo -n "This is theh) " > tmp
/lab5/test$ delta-debugger ./test2 tmp
/lab5/test$ cat tmp.delta
This is
```

### 需要提交的内容

完成实验后，通过提交并推送 `lab5/` 目录下的更改来提交你的代码。具体来说，你需要提交对 `delta_debugger/delta.py` 的更改。

```sh
lab5$ git add delta_debugger/delta.py
lab5$ git commit -m "在此处填写你的提交信息"
lab5$ git push
```

## 构建静态分析器（数据流分析）

为包含分支和循环的 C 语言子集构建一个"除零"静态分析器。

### 目标

在本实验中，你将构建一个静态分析器，能够在编译时检测 C 程序中潜在的除零错误。你将通过编写一个 LLVM pass 来实现这一点。由于为像 C 这样的成熟语言开发静态分析器并非易事，本实验将分为两部分。

##### 第一部分

1.  实现 `DivZeroAnalysis::check`，用于检查给定指令是否可能导致错误。
2.  实现 `src/Transfer.cpp` 中的 `DivZeroAnalysis::transfer`。
3.  通过完成 `src/Transfer.cpp` 中提供的函数存根，实现其中的 `eval` 函数。

##### 第二部分

在本实验的第二部分，你将在 `src/ChaoticIteration` 中实现各种函数。

1.  实现 `doAnalysis` 函数，该函数为你的分析执行混沌迭代算法。
2.  实现 `flowIn` 函数，该函数合并所有传入流的 out 内存。
3.  实现 `flowOut` 函数，该函数更新 out 内存，并根据需要将所有传出流加入 `WorkSet`。
4.  实现 `join` 函数，该函数计算两个 Memory 对象的并集，并考虑 Domain 值。
5.  实现 `equal` 函数，该函数检查两个 Memory 对象是否相等，并考虑 Domain 值。

### 设置

实验6的骨架代码位于 `lab6/` 目录下。

##### 步骤 1

以下命令使用之前见过的 [Cmake][Cmake ref]/[Makefile][Make ref] 模式来设置实验环境。

需要注意的一点是使用了 `-DUSE_REFERENCE=ON` 标志：本实验包含两部分，此标志允许你独立于第二部分，专注于第一部分所需的功能。

```sh
/lab6$ mkdir build && cd build
/lab6/build$ cmake -DUSE_REFERENCE=ON ..
/lab6/build$ make
```

在生成的文件中，你现在应该在 `lab6/build` 目录下看到 `DivZeroPass.so`。

我们现在准备在一个示例输入 C 程序上运行我们的基础实验。

##### 步骤 2

在测试程序上运行 pass 之前，我们需要为其生成 LLVM IR 代码。

`clang` 命令从输入 C 程序 `test04.c` 生成 LLVM IR 程序。

`opt` 命令优化该 LLVM IR 程序，并生成一个等效的、更易于你将在本实验中构建的分析器处理的 LLVM IR 程序。特别是，`-mem2reg` 选项将每个 [AllocaInst][LLVM AllocaInst] 提升为寄存器，使你的分析器在本实验中可以忽略指针处理。

```sh
/lab6/test$ clang-19 -emit-llvm -S -fno-discard-value-names -Xclang -disable-O0-optnone -c -o test04.ll test04.c
/lab6/test$ opt-19 -passes="mem2reg" -S test04.ll -o test04.opt.ll
```

##### 步骤 3

与之前的实验类似，你将把你的分析器实现为一个名为 `DivZeroPass` 的 LLVM pass。

**如果你尚未完成代码，运行以下命令将导致段错误，这没关系。完成代码后再运行测试。**

然后，你将使用 `opt` 命令在优化后的 LLVM IR 程序上运行此 pass，如下所示：

```sh
/lab6/test$ opt-19 -load-pass-plugin ../build/DivZeroPass.so -passes="DivZero" -disable-output test04.opt.ll > test04.out 2> test04.err
```

成功完成本实验后，`test/test04.out` 中的输出应如下所示：

```
Running DivZero on f
Potential Instructions by DivZero:
  %div1 = sdiv i32 %div, %div
```

程序的调试输出（使用 `errs()` 打印）将在 `test/test04.err` 文件中提供。

### 输入程序的格式

为降低实验复杂度，我们限制了你的分析必须处理的指令集。我们假设本实验的输入程序只能使用 C 语言的以下子集：

*   所有值都是整数（即没有浮点数、指针、结构体、枚举、数组等）。你可以忽略其他类型的值。
*   程序可以有赋值、有符号和无符号算术运算（+、-、*、/）以及比较运算（<、<=、>、>=、==、!=）。所有其他指令都被视为 nop。
*   程序可以有 if 语句和循环。
*   用户输入仅通过提供的 `isInput` 函数返回 `True` 的函数集引入。你可以忽略对其他函数的调用指令。

### 实验说明

一个成熟的静态分析器包含三个组件：
1.  抽象域
2.  针对单个指令的转移函数，使用抽象域评估指令。
3.  组合单个指令的分析结果，以获得整个函数或程序的分析结果。

在实验的第一部分，我们将只专注于实现第2项，并且仅针对上述描述的有限指令子集。

更具体地说，你的任务是在提供的抽象域（定义在 `Domain.h` 中）的抽象值上，实现分析如何评估不同的 LLVM IR 指令。

在实验的第二部分，我们将专注于实现第3项，即组合单个转移函数的结果，以获得一个过程内、流敏感、路径不敏感的除零分析。

我们提供了一个框架来构建你的除零静态分析器。该框架由 `lab6/src/` 下的 `Domain.cpp`、`Transfer.cpp`、`ChaoticIteration.cpp` 和 `DivZeroAnalysis.cpp` 文件组成。

此外，我们还提供了 `src/Utils.cpp`，其中定义了一些有用的函数：

+   `variable` 接受一个 `Value` 并返回字符串。此字符串用作存储在 `InMap` 和 `OutMap` 中的 Memory 映射的键。
+   `getOrExtract` 接受一个 `Memory` 和一个 `Value`，并返回 `Memory` 中对应于 `Value` 的 `Domain`，如果未找到，则尝试从指令本身提取 `Domain`。
+   `printMemory`、`printInstructionTransfer` 和 `printMap` 会将各种调试信息打印到 `stderr`。

##### **第一部分：检查与转移函数**

##### 步骤 1

通过阅读文章 [A Menagerie of Program Abstractions][Menagerie Link] 来刷新你对程序抽象的理解。

一旦你对抽象域有了很好的理解，就研究 `Domain` 类，以理解我们为你定义的、在本实验中使用的抽象域。文件 `include/Domain.h` 和 `src/Domain.cpp` 包含了抽象值及其上的操作。这些操作将执行抽象评估，**而无需运行程序**。如文章所述，我们为加法、减法、乘法和除法定义了抽象运算符。

此分析的一个重要部分是认识到你实际上从未运行程序。这意味着当你评估像这样的指令时：

```llvm
%cmp = icmp slt i32 %x, %y
```

`%cmp` 的 Domain 不是由 `%x` 和 `%y` 的运行时值决定的，而是由它们各自的 Domain 相对于比较指令的评估决定的。所以，更具体地说，如果 `%x` 的 Domain 是 `Domain::Zero`，`%y` 的 Domain 也是 `Domain::Zero`，由于小于比较会被认为是 **[相等时为假][LLVM CmpInst]**，那么结果 Domain 将是 `Domain::Zero`。

##### 步骤 2

检查 `DivZeroAnalysis::runOnFunction` 以了解编译器 pass 如何在高层面上执行分析：
```cpp
bool DivZeroAnalysis::runOnFunction(Function &F) {
  outs() << "Running " << getAnalysisName() << " on " << F.getName() << "\n";

  // 初始化 InMap 和 OutMap。
  for (inst_iterator Iter = inst_begin(F), E = inst_end(F); Iter != E; ++Iter) {
    auto Inst = &(*Iter);
    InMap[Inst] = new Memory;
    OutMap[Inst] = new Memory;
  }

  // 混沌迭代算法在 doAnalysis() 内部实现。
  doAnalysis(F);

  // 检查函数中的错误；
  ...
}
```
`runOnFunction` 过程为输入 C 程序中编译器在 pass 期间遇到的每个函数调用。每个指令 `I` 被用作键，在全局的 `InMap` 和 `OutMap` 哈希映射中初始化一个新的 `Memory` 对象。这些映射在下一步中有更详细的描述，但现在你可以将它们视为存储每个变量在指令之前和之后的抽象值。例如，抽象状态可能存储诸如"**在指令 i 之前，变量 x 是正数**"这样的事实。由于 `InMap` 和 `OutMap` 是全局的，请随意在你的代码中直接使用它们。

一旦 **In** 和 **Out** 映射初始化完毕，`runOnFunction` 调用 `doAnalysis`：一个你将在第二部分中实现的、用于执行混沌迭代算法的函数。对于第一部分，你可以假设它只是使用适当的 `InMap` 和 `OutMap` 映射来调用 `transfer`。

所以，在高层面上，`runOnFunction` 将：
1.  初始化 **In** 和 **Out** 映射。
2.  使用混沌迭代算法填充它们。
3.  通过使用每个除法指令的 `InMap` 条目来检查除数是否可能为零，从而发现潜在的除零错误。

##### 步骤 3

理解所提供框架中的内存抽象。

对于每个 `Instruction`，`DivZeroAnalysis::InMap` 和 `DivZeroAnalysis::OutMap` 分别存储指令之前和之后的**抽象状态**。

抽象状态是从 LLVM 变量到抽象值的映射；具体来说，我们将 `Memory` 定义为 `std::map<std::string, Domain *>`。

由于我们将变量引用为 `std::string`，我们提供了一个名为 `variable` 的辅助函数，它将 LLVM `Value` 编码为我们用于变量的内部字符串表示。

请注意，`Instruction` 也是一个 `Value`。

例如，考虑以下 LLVM 程序。我们展示了每个指令之前和之后的抽象状态，记为 **M**：

|  ID   | 指令                        | 指令之前的状态 | 指令之后的状态  |
| :---: | :-------------------------- | :------------- | :-------------- |
| `I1`  | `%x = call i32 (...) @input()` | `{  }`         | `{ %x: T }`     |
| `I2`  | `%y = add i32 %x, 1`        | `{ %x: T }`    | `{ %x: T, %y: T }` |

在第一条指令 `I1` 中，我们将一个输入整数赋值给变量 `%x`。

在抽象状态中，我们使用抽象值 **T**（也称为"top"或 `MaybeZero`），因为该值在编译时是未知的。

指令 `I2` 更新了 `%y` 的抽象值，该值是通过对 `%x` 的抽象值应用抽象加法运算（记为 `+`）计算得出的。

请注意，在 LLVM 框架中，赋值指令（例如，call、二元运算符、icmp 等）的对象也代表它定义的变量（即其左侧）。

因此，在你的实现中，你将使用指令 `I1` 和 `I2` 的对象来分别引用变量 `%x` 和 `%y`。

例如，`variable(I1)` 将引用 `%x`。

##### 步骤 4

既然我们理解了 pass 如何执行分析以及我们将如何存储每个抽象状态，我们就可以开始实现了。

首先，你将在 `src/Transfer.cpp` 中实现函数 `DivZeroAnalysis::transfer`，以填充每个指令的 `OutMap`。具体来说，给定一个指令及其传入的抽象状态（`const Memory *In`），`transfer` 应填充派生于相应 `eval` 实现的传出抽象状态（`Memory *NOut`）。

`Instruction` 类代表所有类型指令的父类。`Instruction` 有[许多子类][LLVM Instruction Class]。为了填充 `OutMap`，每种类型的指令都应区别处理。

回想一下，在本实验中你应该处理：
1.  [二元运算符][LLVM BinOps]（add、mul、sub 等）
2.  [CastInst][LLVM CastInst]
3.  [CmpInst][LLVM CmpInst]（icmp、eq、ne、slt、sgt、sge 等）
4.  通过 `getchar()` 的用户输入——回想一下，这是使用 `src/Transfer.cpp` 中的 `isInput()` 处理的。

LLVM 提供了[几个模板函数][LLVM template functions]来检查指令的类型。我们现在将专注于 `dyn_cast<>`。在此示例中，我们检查 `Instruction` `I` 是否是一个 BinaryOperator。

```cpp
if (BinaryOperator *BO = dyn_cast<BinaryOperator>(I)) {
  // I 是一个 BinaryOperator，执行某些操作
}
```
在运行时，`dyn_cast` 如果可能，将返回 `I` *转换后*的 `BinaryOperator`，否则返回 null。

此时，你的 `eval(...)` 实现将接受指令，并确定此指令的 Domain 如何受操作影响。例如，

```llvm
%add = add nsw i32 %x, %y
```
假设 `%x` 的域是 `Domain::Zero`，`%y` 的域是 `Domain::NonZero`。由于 `%y` 可以取任何非零值（正或负），`%add` 的结果域将由 `Zero` 与 `NonZero` 值的加法决定。因此，`%add` 的域被确定为 `Domain::NonZero`。通过这种方式，`DivZeroAnalysis::transfer` 函数为给定 `Instruction` 的相关操作更新 `OutMap`。

`PhiNode` 的 `eval` 函数已经为你实现，并提供了一个如何使用工具函数 `getOrExtract` 以及 `Domain::join` 的示例。

**处理 LLVM PHI 节点。**
出于优化目的，编译器通常以**静态单赋值**（SSA）形式实现其中间表示，LLVM IR 也不例外。在 SSA 形式中，一个变量恰好在一个代码点被赋值和更新。如果源代码中的一个变量有多个赋值，这些赋值在 LLVM IR 中被拆分为不同的变量，然后**合并**在一起。我们称这个合并点为 **phi 节点**。

为了说明 phi 节点，请考虑以下代码：

<table>
  <tbody>
    <tr valign="top">
      <td>
        <pre><code>
int f() {
  int y = input();
  int x = 0;
  if (y < 1) {
  # then
    x++;
  } else {
    x--;
  }
  # end
  return x;
}
      </code></pre>
      </td>
      <td>
      <pre><code>
entry:
  %call = call i32 (...) @input()
  %cmp = icmp slt i32 %call, 1
  br i1 %cmp, label %then, label %else
       <br></br>
then:                      ; preds = %entry
  %inc = add nsw i32 0, 1  ; 等同于左侧的 x++
  br label %if.end
       <br></br>
else:                      ; preds = %entry
  %dec = add nsw i32 0, -1 ; 等同于左侧的 x--
  br label %end
       <br></br>
end:                       ; preds = %else, %then
  %x = phi i32 [%inc, %then ], [%dec, %else ]
  ret i32 %x
        </code></pre>
      </td>
    </tr>
  </tbody>
</table>

根据 `y` 的值，我们要么走左分支执行 `x++`，要么走右分支执行 `x--`。在相应的 LLVM IR 中，对 `x` 的更新被拆分为两个变量 `%inc` 和 `%dec`。`%x` 在分支执行后通过 `phi` 指令赋值；抽象地说，`phi i32 [ %inc, %then ], [ %dec, %else ]` 表示如果执行了 then 分支，则将 `%inc` 赋值给 `%x`，如果执行了 else 分支，则将 `%dec` 赋值给 `%x`。

这里有一段示例代码可以帮助你处理 phi 节点，因为具体细节超出了本课程的范围；不过，如果你对这些编译器细节感兴趣，欢迎进一步阅读关于 SSA 的内容。

```cpp
Domain *eval(PHINode *Phi, const Memory *InMem) {
  if (auto ConstantVal = Phi->hasConstantValue()) {
    return new Domain(extractFromValue(ConstantVal));
  }

  Domain *Joined = new Domain(Domain::Uninit);

  for (unsigned int i = 0; i < Phi->getNumIncomingValues(); i++) {
    auto Dom = getOrExtract(InMem, Phi->getIncomingValue(i));
    Joined = Domain::join(Joined, Dom);
  }
  return Joined;
}
```

##### 步骤 5

实现 `src/DivZeroAnalysis.cpp` 中的 `DivZeroAnalysis::check` 函数。此函数检查一个 `Instruction` 以确定除零是否**可能**。任何**有符号**或**无符号**除法指令，如果其除数的 `Domain` 是 `Domain::Zero` 或 `Domain::MaybeZero`，都将被视为潜在的除零。你应该使用 `DivZeroAnalysis::InMap` 来判断是否存在错误。

为了测试你的 `check` 和 `transfer` 函数，我们提供了一个参考的 `doAnalysis` 二进制文件。在第二部分中，你需要自己实现 `doAnalysis` 函数，但现在你可以使用我们的二进制解决方案进行测试，以确保你到目前为止实现的函数能正确工作。按照以下步骤使用参考二进制文件进行编译：

```sh
/lab6/build$ rm CMakeCache.txt
/lab6/build$ cmake -DUSE_REFERENCE=ON ..
/lab6/build$ make
```

正如我们在设置部分演示的那样，使用 `opt` 在你的分析器上运行测试文件：

```sh
/lab6/test$ opt-19 -load-pass-plugin ../build/DivZeroPass.so -passes="DivZero" -disable-output test04.opt.ll > test04.out 2> test04.err
```

如果程序中存在除零错误，你的输出应如下所示：

```sh
Running DivZero on f
Instructions that potentially divide by zero:
  %div = sdiv i32 1, 0
```

##### 第二部分：整合所有内容——数据流分析

现在你已经有了填充 in 和 out 映射并使用它们检查除零错误的代码，下一步是在 `src/ChaoticIteration.cpp` 中的 `doAnalysis` 函数中实现混沌迭代算法。

首先，复习数据流分析的讲座内容。特别是，研究到达定值分析和混沌迭代算法。非正式地说，数据流分析为程序控制流图中的每个节点创建并填充一个 **IN** 集和一个 **OUT** 集。**flowIn** 和 **flowOut** 操作重复执行，直到算法达到一个不动点。

更正式地说，`doAnalysis` 函数应维护一个 `WorkSet`，其中包含"需要更多工作"的节点。当 `WorkSet` 为空时，算法已达到不动点。对于 `WorkSet` 中的每个指令，你的函数应执行以下操作：

1.  通过合并所有传入流的 **OUT** 集，并将结果保存到当前指令的 **IN** 集中，来执行 **flowIn** 操作。在这里，你将使用你在第一部分中填充的 `InMap` 和 `OutMap` 中的条目作为 **IN** 和 **OUT** 集。
2.  应用你在第一部分中实现的 `transfer` 函数来填充当前指令的 **OUT** 集。
3.  通过相应地更新 `WorkSet` 来执行 **flowOut** 操作。仅当 `transfer` 函数更改了 **OUT** 集时，才应添加当前指令的后继。

以下是一个示例，说明如何将指令加载到 `WorkSet` 中，以及如何引入 [llvm::SetVector][LLVM SetVector] 容器，请随意在你的实现中使用此代码：

```cpp
void DivZeroAnalysis::doAnalysis(Function &F) {
  SetVector<Instruction *> WorkSet;
  for(inst_iterator I = inst_begin(F), E = inst_end(F); I != E; ++I) {
    WorkSet.insert(&(*I));
  }
  // ...
}
```

对于本实验，我们不需要维护显式的控制流图；LLVM 已经在内部维护了一个。为了让你专注于本任务的数据流部分，我们提供了两个辅助函数 `getSuccessors` 和 `getPredecessors`（定义在 `include/DivZeroAnalysis.h` 中），它们查找并返回给定 LLVM `Instruction` 的后继和前驱。

接下来，你将实现混沌迭代算法的各个部分。

##### 步骤 1

在 `flowIn` 中，你将执行到达定值分析的第一步，即取 `I` 所有前驱的 **OUT** 变量的并集。你可能会发现 `src/ChaoticIteration.cpp` 中的 `getPredecessors` 方法在这里很有帮助。这应在以下为你模板化的函数中完成：

*   `void DivZeroAnalysis:flowIn(Instruction *I, Memory *In)`

给定一个 `Instruction` `I` 及其 **IN** 变量集 Memory `In`，你需要将 **IN** 与 `I` 的每个前驱的 **OUT** 进行合并。为了合并两个内存状态，你需要实现以下模板化的 join 函数：

*   `Memory* join (Memory *M1, Memory *M2)`

在此函数中，合并这些 `Memory` 对象时，你还需要考虑 `Domain` 值。请参考抽象域以了解为什么这是必要的。回想一下，`Domain` 类中定义了用于合并两个抽象值的 `join` 操作。

##### 步骤 2

调用你在第一部分中实现的 `transfer` 函数来填充当前指令的 **OUT** 集。

##### 步骤 3

在 `flowOut` 中，你将确定是否需要再次分析给定的指令。这应在以下为你模板化的函数中完成：

*   `void DivZeroAnalysis::flowOut(Instruction *I, Memory *Pre, Memory *Post, SetVector<Instruction *> &WorkSet)`

给定一个 `Instruction` `I`，你将分析**转移前**的 Memory `Pre` 和**转移后**的 Memory `Post`。如果在应用 `transfer` 后内存值存在变化，你将需要将指令 `I` 提交以进行额外的分析。为了确定在 `transfer` 函数期间内存是否发生了变化，你将实现函数 `equal`：

*   `bool equal(Memory *M1, Memory * M2)`

在此函数中，确定两个 `Memory` 对象是否相等时，你同样需要考虑 `Domain` 值。回想一下，`Domain` 类中定义了用于评估两个抽象值是否相等的 `equal` 操作。

最后，在 `flowOut` 中，确保你更新了指令 `I` 的 `OutMap`，使其包含 `Post` 中的值。

##### 步骤 4

回想一下，在第一部分中，可以使用参考的 `doAnalysis` 来验证你的 `check` 和 `transfer` 实现。现在你正在编写自己的 `doAnalysis` 版本，你可能需要在不使用参考的情况下重新构建 pass。按照以下步骤使用你的实现进行编译：

```sh
/lab6/build$ rm CMakeCache.txt
/lab6/build$ cmake ..
/lab6/build$ make
```

完成上述步骤后，你的分析应生成两个输出文件。
1.  `test.out`，其中 test 是你正在测试的程序，是结果的精简版本，仅包含具有潜在除零操作的指令。
2.  `test.err` 是一个完整报告，包括任何具有潜在除零操作的指令，以及每个被审查指令的 `InMap` 和 `OutMap` 的最终状态。

你的输出格式如下：

```
Dataflow Analysis Results:
Instruction:   %cmp = icmp ne i32 0, 0
In set: 

Out set: 
    [ %cmp     |-> Zero      ]

Instruction:   br i1 %cmp, label %if.then, label %if.end
In set: 
    [ %cmp     |-> Zero      ]
Out set: 
    [ %cmp     |-> Zero      ]

Instruction:   %div = sdiv i32 1, 0
In set: 
    [ %cmp     |-> Zero      ]
Out set: 
    [ %cmp     |-> Zero      ]
    [ %div     |-> Uninit    ]

Instruction:   br label %if.end
In set: 
    [ %cmp     |-> Zero      ]
    [ %div     |-> Uninit    ]
Out set: 
    [ %cmp     |-> Zero      ]
    [ %div     |-> Uninit    ]

Instruction:   ret i32 0
In set: 
    [ %cmp     |-> Zero      ]
    [ %div     |-> Uninit    ]
Out set: 
    [ %cmp     |-> Zero      ]
    [ %div     |-> Uninit    ]
```

### 提交

完成实验后，通过提交并推送 `lab6/` 下的更改来提交你的代码。具体来说，你需要提交对 `src/ChaoticIteration.cpp`、`src/DivZeroAnalysis.cpp` 和 `src/Transfer.cpp` 的更改。

```sh
lab6$ git add src/ChaoticIteration.cpp src/DivZeroAnalysis.cpp src/Transfer.cpp
lab6$ git commit -m "your commit message here"
lab6$ git push
```

[LLVM template functions]: http://releases.llvm.org/8.0.0/docs/ProgrammersManual.html#the-isa-cast-and-dyn-cast-templates
[LLVM CmpInst]: https://llvm.org/doxygen/classllvm_1_1CmpInst.html
[LLVM CastInst]: https://llvm.org/doxygen/classllvm_1_1CastInst.html
[LLVM BinOps]: https://llvm.org/doxygen/classllvm_1_1BinaryOperator.html
[LLVM Instruction class]: http://releases.llvm.org/8.0.0/docs/ProgrammersManual.html#the-instruction-class
[LLVM AllocaInst]: https://llvm.org/doxygen/classllvm_1_1AllocaInst.html
[LLVM SetVector]: https://llvm.org/doxygen/classllvm_1_1SetVector.html
[CMake Ref]: https://en.wikipedia.org/wiki/CMake
[Make Ref]: https://www.gnu.org/software/make/manual/html_node/Simple-Makefile.html#Simple-Makefile
[Menagerie Link]: https://drive.google.com/open?id=1uhCWzfBxsaBQQ6NyMTY64Y6x_qRR1YQwiTpWT0_N2Xc

## 指针分析

编写一个针对C程序的“除零”静态分析，作为LLVM pass，用于处理指针别名和动态分配的内存。

### 目标

本实验的目标是扩展实验6中的静态**除零**检查器，使其能够在存在指针的情况下进行分析。你将把上一个实验中的数据流分析与流不敏感指针分析结合起来，从而得到一个更全面的整体静态分析。

### 环境搭建

实验6的骨架代码位于`/lab6`目录下。在描述文件位置时，我们会经常将实验6的顶层目录称为`lab6`。本实验建立在实验5的工作基础之上，因此你可以重用`/lab5/src`目录中的大部分内容。

#### 步骤 1

以下命令使用之前见过的CMake/Makefile模式来搭建实验环境。

```sh
/lab6$ mkdir build && cd build
/lab6$ cmake ..
/lab6$ make
```

在生成的文件中，你应该会在`build`目录下看到`DivZeroPass.so`，这与上一个实验类似。在本实验中，你将修改`src/ChaoticIteration.cpp`、`DivZeroAnalysis.cpp`和`Transfer.cpp`。这些更改大部分可以从上一个实验复制过来，然后根据新的需求进行修改。

现在，我们准备在一个示例输入C程序上运行我们的基础实验。

#### 步骤 2

在运行pass之前，必须先生成LLVM IR代码。

```sh
/lab6/test$ clang -emit-llvm -S -fno-discard-value-names -Xclang -disable-O0-optnone -c test13.c -o test13.ll
/lab6/test$ opt -load ../build/DivZeroPass.so -DivZero test13.ll
```

第一行（`clang`）从输入的C程序`test13.c`生成LLVM IR代码。下一行（`opt`）在编译后的LLVM IR代码上运行你的pass。

在之前的实验中，我们使用了一个带有参数`-mem2reg`的中间步骤，该参数将每个[AllocaInst][LLVM AllocaInst]提升为寄存器，从而让你的分析器在本实验中可以忽略指针的处理。然而，在本实验中我们不再这样做，因此你需要扩展之前的代码来处理指针。

成功完成本实验后，输出应如下所示：

```sh
/lab6/test$ opt -load ../build/DivZeroPass.so -DivZero test13.ll
Running DivZero on f
Potential Instructions by DivZero:
    %div = sdiv i32 1, %2
```

### 输入程序的格式

本实验的输入格式与实验6相同，不同之处在于现在你需要处理指针：

* 你可以*不*精确处理整数以外的值，但你的LLVM pass在遇到其他类型的值时不得引发段错误。
* 你*必须*处理赋值、算术运算（+、-、*、/）、比较运算（<、<=、>、>=、==、!=）和分支。
* 你*不*需要精确处理XOR、OR、AND和Shift运算，但你的程序在这些情况下不得引发段错误。
* 输入程序*可以*包含if语句和循环。
* 用户输入*仅*通过提供的`isInput`函数返回`True`的那组函数引入。
* 你*可以忽略*对其他函数的其他调用指令。

### 实验说明

在本实验中，你将扩展在实验6中实现的**除零**分析，以在存在别名内存位置的情况下分析和捕获潜在的**除零**错误。

在课堂上，你了解到在语言中引入别名会使推理程序行为变得更加困难，并且需要某种形式的指针分析。你将使用**流不敏感指针分析**——我们从中抽象出控制流并构建一个全局的**指向图**——来帮助你的检查器分析更有意义的程序。

### 第一部分：函数参数/调用指令

#### 步骤 1

回想一下，在之前的实验中，所有的测试程序都是不接受参数的基本函数。

例如：

```c
void f() {
    int x = 0;
    int y = 2;
    int z;
    if(x < 1) {
        z = y / x; // 分支内的除零
    }
}
```

函数`f()`在其签名中没有参数。实际上，函数可以接受任意数量的变量，甚至可以是不同类型的（但本实验将所有参数视为`int`类型）。

因此，在`doAnalysis`中，你需要处理带参数的函数，并相应地设置它们的域。

#### 步骤 2

熟悉作为**除零**LLVM pass入口点的`doAnalysis()`例程。在上一个实验中，你在这里实现了混沌迭代算法。对于实验6，`doAnalysis()`的函数签名现在略有变化，包含了一个**PointerAnalysis**对象。我们将在第二部分中介绍这一点。

```cpp
/**
 * @brief 此函数使用 flowIn()、transfer() 和 flowOut() 实现混沌迭代算法。
 *
 * @param F 要分析的函数。
 */
void DivZeroAnalysis::doAnalysis(Function &F, PointerAnalysis *PA)
```

#### 步骤 3

给定一个传入`doAnalysis()`例程的任意函数`F`，找到该函数调用的参数，并为每个参数实例化抽象域值。请注意，这里的对象`F`是`Function`类型，可用于查找所有可用的参数。

此外，一旦你初始化了这些起始参数抽象值，将这些值传递到你现有的**除零**pass实现中，以便这些变量在整个**到达定值分析**中得到传播。

#### 步骤 4

除了处理被分析函数`F`的参数外，我们还希望覆盖程序中进行的其他函数调用。

我们之前已经见过这个函数：

```c
void main() {
    int x = getchar();
    int y = 5 / x;
    return 0;
}
```

在上面的例子中，`getchar()`是一个没有参数的外部函数调用，返回一个`int`。更新你的分析以处理任意的`CallInst`指令，但仅限于返回类型为`int`的情况。

### 第二部分：存储/加载指令

#### 步骤 1

如上所述，之前的`doAnalysis()`函数有一个变化：

```cpp
void DivZeroAnalysis::doAnalysis(Function &F, PointerAnalysis *PA)
```

此外，我们还修改了实验6中使用的`transfer`函数的签名：

```cpp
void DivZeroAnalysis::transfer(Instruction *I, const Memory *In, Memory *NOut,
                               PointerAnalysis *PA, SetVector<Value *> PointerSet)
```

请确保在重用上一个作业的代码时，复制你的实现细节和函数内容，但**保持函数签名不变！**。

这些参数在我们探索指针别名时是必需的。

为了帮助理解代码与实验6有何不同以及它是如何结合在一起的，请考虑来自`DivZeroAnalysis::runOnFunction()`的以下片段：

```cpp
bool DivZeroAnalysis::runOnFunction(Function &F) {
  outs() << "Running " << getAnalysisName() << " on " << F.getName() << "\n";

  // 此处有更多代码...
  PointerAnalysis *PA = new PointerAnalysis(F);
  doAnalysis(F, PA);
  // 此处有更多代码...
}
```

以及来自`DivZeroAnalysis::doAnalysis()`的以下片段：

```cpp
void DivZeroAnalysis::doAnalysis(Function &F, PointerAnalysis *PA) {
    for(inst_iterator I = inst_begin(F), E = inst_end(F); I != E, ++I) {
        WorkSet.insert(&(*I));
        PointerSet.insert(&(*I));
    }
    // 此处有更多代码...
    transfer(I, In, NOut, PA, PointerSet);
    // 此处有更多代码...
}
```

并且，请注意`transfer`函数现在接收`PointerAnalysis`和`PointerSet`作为输入。在重用实验6的代码时请记住这一点。

#### 步骤 2

从高层次来看，你将修改`Transfer.cpp`中的`transfer()`函数，通过跟踪指针来执行更复杂的**除零**分析。

`PointerAnalysis`的代码位于`src/PointerAnalysis.cpp`中，它包含了使用指针别名所需的各种方法的实现。在对`F`运行指针分析之后，`PointerAnalysis *PA`对象将包含对该函数运行指针分析的结果，而`PointerSet`将包含该函数中的所有指针。

我们将在以下部分更详细地讨论这个`PointerAnalysis`类的作用，但请通读文档字符串和代码，并理解所提供的每个方法中正在做什么。

##### 建模LLVM的alloca、store和load。

这里我们提供了一个在LLVM中使用指针的接口。

你可以按原样使用它作为后备方案，但也可以自由地按照自己的方式建模LLVM中的引用。

对于本实验，我们禁用了实验6中使用的`mem2reg` pass。因此，LLVM将为每个C变量创建一个内存单元。结果，你将看不到任何**phi节点**，并且不一定需要你在实验6中为实现处理它们而编写的代码段。

考虑以下代码：

<table>
<tbody>
<tr valign="top">
<td>
<pre><code>
int f() {
  int a = 0;
  int *c = &a;
  int x = 1 / *c;
  return x;
}
</code></pre>
</td>
<td>
<pre><code>
I1: %a = alloca i32, align 4
I2: %c = alloca i32*, align 4
I3: %x = alloca i32, align 4
I4: store i32 0, i32* %a, align 4
I5: store i32* %a, i32** %c, align 8
I6: %0 = load i32*, i32** %c, align 8
I7: %1 = load i32, i32* %0, align 4
I8: %div = sdiv i32 1, %1
I9: store i32 %div, i32* %x, align 4
I10: %2 = load i32, i32* %x, align 4
I11: ret i32 %2
</code></pre>
</td>
<td>
<pre><code>
M[variable(I1)] = 0
M[variable(I2)] = variable(I1)
M[variable(I6)] = M[variable(I2)]
...
...
...
...
...
...
</code></pre>
</td>
</tr>
</tbody>
</table>


与实验6一样，`variable()`方法仍然用于编码指令的变量。

##### 构建指向图

`PointerAnalysis`类构建了一个指向图，你将在`transfer`函数中使用它。`PointsToInfo`表示从变量到`PointsToSet`的映射，`PointsToSet`表示一个变量可能指向的分配站点的集合。

为了帮助建模与变量`%a`（即`variable(I1)`）对应的内存位置，我们提供了一个函数`address`，你可以在构建`PointsToSet`时使用它来编码变量的内存地址（`address(I1)`）。

指令`I2`将被类似地分析。

在`I5`处，在`I2`处分配的内存位置（即`address(I2)`）将存储在`I1`处分配的内存位置（即`address(I1)`）。

此外，字段`PointsTo`表示将被构建的完整指向图。

`PointerAnalysis`构造函数的实现将遍历给定`Function F`的所有指令并填充`PointsTo`，该实现已作为本作业骨架代码的一部分提供给你。

此外，我们还提供了一个`alias()`方法，如果两个指针可能是彼此的别名，则返回true。

#### 步骤 3

使用`PointerAnalysis`对象，增强`Transfer.cpp`中的`transfer()`函数，使其在分析过程中考虑指针别名。这应该通过在`transfer`函数中添加代码来处理`StoreInst`和`LoadInst`指令来完成。

##### LoadInst

我们可以依赖`In`内存中定义的现有变量来知道应该为加载指令引入的新变量分配什么抽象域。

例如，给定如下加载指令：

```llvm
%2 = load i32, i32* %1, align 4
```

这将`%1`处的指针值加载到类型为`i32`的新变量`%2`中。因此，`%2`的抽象域应该与`%1`的抽象域相同。

随着指针的加入，我们还可以有：

```llvm
%1 = load i32*, i32** %d, align 8
```

这将`%d`处的指针值（它本身是一个指针）加载到类型为`i32*`的新变量`%1`中。

**注意**与前面的例子相比，加载指令的类型（`load i32*`）中多了一个`*`字符。你可以使用`getType()`检索此加载指令的类型，并使用`isIntegerTy()`或`isPointerTy()`等方法进一步检查类型。

##### StoreInst

存储指令可以将新变量添加到我们的内存映射中，或者覆盖现有的变量。

例如，给定如下存储指令：

```llvm
store i32, 0, i32* %a, align 4
```

这将值`0`存储到变量`%a`中。

你应该熟悉使用`getOperand()`检索这些操作数，但你也可以分别使用`getValueOperand()`和`getPointerOperand()`方法。随着指针的加入，我们还可以有：

```llvm
store i32* %a, i32** %c, align 4
```

现在我们将`%a`处的指针存储到变量`%c`中，`%c`是一个指向指针的指针。我们可以再次使用每个操作数上`getType()`的类型信息来确定是否可能应用指针别名。

这显然使我们的抽象域分析复杂化了——如果某个后续指令更新了`%a`的值，我们不仅需要更新`%c`的抽象值，还需要考虑更新指向`%a`的其他指针的抽象值。这也适用于对`%c`所做的更改，这正是`test13.c`示例中发生的情况。

```c
int f() {
    int a = 1;
    int *c = &a;
    int *d = &a;
    *c = 0;
}
```

为了解决这些情况，我们可以依赖在`PointerAnalysis`中构建的指向图。

我们需要遍历提供的`PointerSet`：如果我们遇到某个实例存在可能别名（`PA->isAlias()`返回`true`），这本质上意味着存在一条连接两个变量之间指针值的边。一旦我们知道存在哪些连接，我们将需要获取每个抽象值，通过`Domain::join()`将它们全部合并，然后继续使用此抽象值更新当前赋值以及**所有**可能别名的赋值。这确保了所有指针引用保持同步，并且将在我们的分析中收敛到一个精确的抽象值。

### 提交

完成实验后，通过提交并推送`lab6/`下的更改来提交你的代码。具体来说，你需要提交对`src/ChaoticIteration.cpp`、`src/DivZeroAnalysis.cpp`和`src/Transfer.cpp`的更改。

```sh
lab6$ git add src/ChaoticIteration.cpp src/DivZeroAnalysis.cpp src/Transfer.cpp
lab6$ git commit -m "你的提交信息"
lab6$ git push
```

[LLVM AllocaInst]: https://llvm.org/doxygen/classllvm_1_1AllocaInst.html

## 动态污点分析

编写一个针对 C/C++ 程序的动态污点分析工具，作为 LLVM pass 来检测程序中的 `ControlFlowHijack` 和 `InjectionAttack` 问题。

### 实验目标
在本实验中，你将在 IR 中间表示上构建一个动态污点分析工具。通过实现污点源、污点传播策略和污点汇聚点，你将能够追踪污点在程序内部的传播，从而检测潜在的安全问题。

### 环境搭建
Lab7 的代码位于 `/lab7/` 目录下。

- 在 VS Code 中使用“打开文件夹”选项打开 lab7 文件夹。
- 确保 Docker 正在你的机器上运行。
- 按 F1 打开 VS Code 命令面板；搜索并选择“Reopen in Container”。
- 这将在 VS Code 中为本实验设置好开发环境。
- 在开发环境中，Lab6_2 的骨架代码将位于 `/lab7` 目录下。
- 之后，如果 VS Code 提示你为实验选择一个工具包，请选择 Clang 8。

#### lab7 的项目结构：

```
- lib
  |
  -- runtime.cpp: 处理运行时污点传播的运行时函数，例如 `StoreInstProcess` 等，你将通过你的 pass 注入这些函数。

- src
  |
  -- DynTaintAnalysisPass.cpp: 包含函数和指令的整体插桩逻辑，为不同类型的指令/函数调用不同的插桩函数。
  |
  -- Instrument.cpp: 每种指令或函数类型的插桩函数，这些函数在当前指令位置插入对运行时函数的调用。
  |
  -- Utils.cpp: 一些辅助函数，例如 `getOperandsString` 等。
```

#### 步骤 1
以下命令使用 CMake/Makefile 模式来设置实验环境。
```
/lab7$ mkdir -p build && cd build
/lab7/build$ cmake ..
/lab7/build$ make
```

你应该会看到在 lab7/build 目录下创建了几个文件。一个名为 `DynTaintAnalysisPass.so` 的 LLVM pass 将作为链接 `lab7/src` 下的 `DynTaintAnalysisPass.cpp` 和 `Instrument.cpp` 的结果生成，同时还会生成一个名为 `libruntime.so` 的运行时库，对应于 `lab7/lib/runtime.cpp`。这些都是你稍后需要修改的源文件。如果你还记得 lab2 的项目构建步骤，这里的步骤与使用动态分析 pass 的部分几乎完全相同。

#### 步骤 2
像之前的实验一样生成 LLVM IR。
```
/lab7$ cd test
/lab7/test$ clang -emit-llvm -S -fno-discard-value-names -c -o InjectionAttack.ll InjectionAttack.cpp -g
/lab7/test$ clang -emit-llvm -S -fno-discard-value-names -c -o ControlFlowHijack.ll ControlFlowHijack.cpp -g
```

#### 步骤 3
使用 opt 在编译好的 C++ 程序上运行提供的 DynTaintAnalysisPass pass。这一步会生成一个带有运行时函数调用的插桩后程序。
```
/lab7/test$ opt -load ../build/DynTaintAnalysisPass.so -DynTaintAnalysisPass -S InjectionAttack.ll -o InjectionAttack.dynamic.ll
/lab7/test$ opt -load ../build/DynTaintAnalysisPass.so -DynTaintAnalysisPass -S ControlFlowHijack.ll -o ControlFlowHijack.dynamic.ll
```

#### 步骤 4
接下来，编译插桩后的程序并将其与运行时库链接，生成一个独立的可执行文件：
```
/lab7/test$ clang -o InjectionAttack -L../build -lruntime InjectionAttack.dynamic.ll
/lab7/test$ clang -o ControlFlowHijack -L../build -lruntime ControlFlowHijack.dynamic.ll
```

#### 步骤 5
最后运行可执行文件。当你完成所有源文件后，它们应该像这样工作：
```
/lab7/test$ ./InjectionAttack
Filename:example.txt ; ls -al
tainted var address: 0x7ffc369a6c90
That's the address in:%arraydecay
Taint propagated from 0x7ffc369a6c90 to 0x7ffc369a6c90
From :%filename to :%arraydecay3 
Taint propagated from 0x7ffc369a6c90 to 0x7ffc369a7090
From :%arraydecay3 to :%arraydecay2 
Taint propagated from 0x7ffc369a7090 to 0x7ffc369a7090
From :%cmd to :%arraydecay5 
Taint detected in sensitive position: 0x7ffc369a7090!
That's the address in:%arraydecay5
This is an example txt file!total 264
drwxrwxrwx 1 root root   512 Nov 30 08:02 .
drwxrwxrwx 1 root root   512 Nov 26 12:10 ..
-rwxr-xr-x 1 root root 19616 Nov 30 08:02 ControlFlowHijack
-rwxrwxrwx 1 root root   605 Nov 26 12:08 ControlFlowHijack.cpp
-rw-r--r-- 1 root root 60332 Nov 30 08:02 ControlFlowHijack.dynamic.ll
-rw-r--r-- 1 root root 49436 Nov 30 08:02 ControlFlowHijack.ll
-rwxr-xr-x 1 root root 18968 Nov 30 08:02 InjectionAttack
-rwxrwxrwx 1 root root   420 Nov 26 12:08 InjectionAttack.cpp
-rw-r--r-- 1 root root 53797 Nov 30 08:02 InjectionAttack.dynamic.ll
-rw-r--r-- 1 root root 50311 Nov 30 08:02 InjectionAttack.ll
-rwxrwxrwx 1 root root   346 Nov 26 12:08 Makefile
-rw-r--r-- 1 root root    28 Nov 30 08:00 example.txt
```

```
/lab7/test$ ./ControlFlowHijack
input:AAAAAAAAA
tainted var : %call1
Taint propagated from %call1 to 0x7ffca89e706c
From :%call1 to :%ch 
Taint propagated from 0x7ffca89e706c to %7
From :%ch to :%7 
Taint propagated from %7 to %conv
From :%7 to :%conv 
Taint propagated from %conv to 0x7ffca89e7080
From :%conv to :%9 
tainted var : %call1

...

Taint propagated from %call1 to 0x7ffca89e706c
From :%call1 to :%ch 
Taint propagated from 0x7ffca89e7088 to %16
From :%data to :%16 
Taint propagated from %16 , 32 to %add
From :%16 , 32 to :%add 
Taint propagated from %add to 0x7ffca89e707c
From :%add to :%secret_value 
Taint propagated from 0x7ffca89e707c to %19
From :%secret_value to :%19 
Taint detected in sensitive position: %19!
You've discovered the secret value!
```

### 实验说明
#### 被分析的程序
我们提供了两个待分析的程序：`InjectionAttack.cpp` 和 `ControlFlowHijack.cpp`。

在 `InjectionAttack.cpp` 中，当用户向 `/bin/cat` 输入所需的文件名参数时，如果添加了一些额外内容，则可以不受检查地运行其他命令。例如，如果用户输入 `example.txt ; ls -al`，命令字符串将变为：`/bin/cat example.txt ; ls -al`。第一个命令 (`/bin/cat example.txt`) 被执行以显示 `example.txt` 的内容，然后第二个命令 (`ls -al`) 会在没有任何限制的情况下被执行。这使得攻击者可以在系统上执行任意命令，从而导致潜在的未授权访问或文件操作。
```
char cmd[2048] = "/bin/cat ";
char filename[1024];
printf("Filename:");
scanf (" %1023[^\n]", filename); // 攻击者可以在此注入 shell 转义符
strcat(cmd, filename);
system(cmd); // 警告：不可信数据被传递给系统调用
```
攻击示例：
```
/lab7/test$ ./InjectionAttack
Filename:example.txt ; ls -al
This is an example txt file.total 32
drwxrwxrwx 1 root root   512 Nov 26 09:22 .
drwxrwxrwx 1 root root   512 Nov 26 08:45 ..
-rwxr-xr-x 1 root root  8416 Nov 26 09:21 ControlFlowHijack
-rw-r--r-- 1 root root   728 Nov 26 08:48 ControlFlowHijack.cpp
-rwxr-xr-x 1 root root 12584 Nov 26 09:21 InjectionAttack
-rw-r--r-- 1 root root   420 Nov 25 16:22 InjectionAttack.cpp
-rwxrwxrwx 1 root root   346 Nov 26 08:47 Makefile
-rw-r--r-- 1 root root    28 Nov 26 09:22 example.txt
-rw-r--r-- 1 root root     0 Nov 26 09:22 otherfile.secret
```

在 `ControlFlowHijack.cpp` 中，当用户/黑客向 `mem.buffer` 写入数据而未检查缓冲区大小时，会覆盖其后内存中的内容；在这种情况下，要成功劫持控制流，用户必须恰好输入 9 个字符，且第 9 个字符是 'A'。这会将 `mem.data` 覆盖为值 65，导致 `secret_value` 被计算为 97。因此，用户的输入可以**意外地**影响程序的控制流，导致控制流劫持（正常情况下，`secret_value` 不会等于 97）。
```
struct Memory{
        char buffer[8]; 
        int data = 0; 
};

bool check_secret(int secret){
        return secret == 97;
}

int main() {
    Memory mem;
    int secret_value=0;
    
    //模拟不安全的 gets
    char* ptr = mem.buffer;
    int ch;
    while ((ch = getchar()) != '\n') {
        *ptr++ = ch; 
    }
    *ptr = '\0';
    
    secret_value=mem.data+32;
    // 检查 secret_value
    if (check_secret(secret_value)) {
        printf("You've discovered the secret value!\n");
    } else {
        printf("Secret value: %d\n", secret_value);
    }
}
```
攻击示例：
```
/lab7/test$ ./ControlFlowHijack
input:AAAAAAAAA
You've discovered the secret value!
```


#### 动态污点分析
污点分析包含三个组成部分：`污点源`/`污点传播策略`/`污点汇聚点`

- 污点源

    污点源是程序中那些可能引入不可信或不安全数据的输入点。这些输入点可能是用户输入、文件读取、网络数据等。

    提示：在我们的两个示例中，仅将用户输入用作污点源，但在实际应用中，文件读取和网络数据传输更为常见。

- 污点传播策略

    这部分可以简单概括为：如果源操作数被污染，那么污点应该传递给目标操作数。
    
    例如，`%b = load i32, ptr %a, align 4` 从 `%a` 中的地址加载一个 i32 类型的数据到 `%b`，源操作数是 `%a`，目标操作数是 `%b`，那么当 `%a` 被污染时，`%b` 也需要被污染。

    除了普通指令外，一些函数调用也会进行污点传播，在我们的例子中，`strcat` 连接两个字符串，如果其中一个字符串被污染，那么污点也需要传播到连接后的结果。

- 污点汇聚点

    当到达一个敏感的程序位置/敏感的程序行为时，会添加一个污点汇聚点来检查特定变量是否被污染。
    
    在我们的两个示例中，在调用 system/check_secret 之前，需要检查 system/check_secret 的参数变量是否被污染。



#### 我们工具的特性
不同的污点分析工具在数据结构和污点处理方法上具有不同的特性。这里，我们声明我们工具的一些特性：

- 污点粒度

    本工具的污点粒度是变量和字节的混合：对于非指针变量，我们以变量为粒度进行追踪；对于指针变量，则以字节为粒度进行追踪。

- 污点颜色

    在污点追踪中，污点颜色是一种用于标识和区分不同污点的属性。从污点的颜色可以推断其来源、类型或状态。然而，在我们的实现中，我们不追踪污点的来源或状态；我们仅区分两种状态：被污染或未被污染（即只有黑白两色）。

- 污点数据结构

    我们使用集合来存储污点信息。结合上述两个特性，在 `runtime.cpp` 中，你会找到两个集合 `taintedPtrVars` 和 `taintedVars`。对于一个非指针类型的变量，如果它的名字在 `taintedVars` 中，则该变量被视为被污染；对于一个指针类型的变量，如果它的运行时地址在 `taintedPtrVars` 中，则表示该变量被污染。
    
    一个更复杂的工具可能会使用诸如影子内存之类的数据结构，这里进行了简化。

- 支持的指令

    本工具不支持所有指令类型，仅支持其中的一部分，包括 TruncInst、GEPInst、StoreInst、LoadInst、BinaryOperator。要创建一个更全面和通用的工具，需要支持所有指令类型。

- 对指针和非指针类型的不同处理

    这种区分的**必要性**：**在 IR 层面**，我们**无法**获取非指针变量在内存中的位置，而在二进制（汇编）层面，我们可以通过指令判断值在哪个寄存器/内存中。

    在区分指针和非指针类型之前，我们需要知道每个指令操作数的指针/非指针类型。以下是每条指令的操作数类型：

    |指令|格式|目标类型|源类型|
    |:-:|:-:|:-:|:-:|
    |TruncInst|`%dest` = trunc **i32** `%src` to **i8**|int|int|
    |GetElementPtrInst|`%dest` = getelementptr **inbounds i8**, **ptr** `%src`, i32 1|ptr|ptr|
    |StoreInst|store **ptr/i8** `%src`, **ptr** `%dest`, align 8|ptr|ptr/int|
    |LoadInst|`%dest` = load **ptr/i8**, **ptr** `%src`, align 8|ptr/int|ptr|
    |BinaryOperator|`%dest` = add nsw **i32** `%src1`, **i32** `%src2`|int|int|
    
    因此，处理 StoreInst 污点传播的函数有两个版本：`StoreInstProcess` 和 `StoreInstProcessPtr`。类似地，在设置污点源（污点汇聚点）时，也会有两个版本：`TaintVal` (`CheckVal`) 和 `TaintPtrVal` (`CheckPtrVal`)。

    对于 LoadInst，由于其源操作数必须是指针，因此可以通过源操作数的地址来确定是否需要污染，所以只有一个 Ptr 版本。

#### TODO 列表：
在代码/技术实现方面，动态污点分析需要以下三个步骤：   
`1.` 开发插桩逻辑并将其打包为 LLVM pass；  
`2.` 使用该 pass 对目标程序的 IR 文件进行插桩，插入对运行时函数的调用；  
`3.` 将修改后的 IR 文件编译成可执行文件并运行。

因此，在本实验中，我们需要完成插桩逻辑以及被插入的运行时函数，你将有以下 TODO 列表：

- 在 `DynTaintAnalysisPass.cpp` 的主运行函数 `runOnFunction` 中，为各种指令和与污点源相关的函数（scanf, getchar）添加相应的插桩函数调用。这些插桩函数用于在特定位置插入运行时函数。
- 在 `Instrument.cpp` 中完成 `Trunc` 和 `Load` 指令的插桩函数。
- 在 `runtime.cpp` 中完成 `Store` 和 `BinaryOperator` 指令的运行时分析函数。

#### 关于插桩
本实验中的插桩方法与 lab2 的动态分析 pass 类似。如果你忘记了一些细节，请回顾 **lab2 教程**中的 [Instrumentation Pass](https://github.com/ecnu-sa-labs/ecnu-sa-labs/blob/ff8658063073a4aa46afa6552bd18c281b477baf/lab_manual/lab2.md#instrumentation-pass) 和 [Inserting Instructions into LLVM code](https://github.com/ecnu-sa-labs/ecnu-sa-labs/blob/ff8658063073a4aa46afa6552bd18c281b477baf/lab_manual/lab2.md#inserting-instructions-into-llvm-code)。

### 提交
完成实验后，通过提交并推送 lab7/ 下的更改来提交你的代码。具体来说，你需要提交对 `src/DynTaintAnalysisPass.cpp`、`src/Instrument.cpp` 和 `lib/runtime.cpp` 的更改。
```
   lab7$ git add src/DynTaintAnalysisPass.cpp src/Instrument.cpp lib/runtime.cpp
   lab7$ git commit -m "你的提交信息"
   lab7$ git push
```

## 动态符号执行

使用 LLVM 和 Z3 为 C 程序构建一个动态符号执行引擎。

### 目标

在本实验中，你将实现一个动态符号执行（DSE）引擎，该引擎能自动生成输入，以高效地探索不同的程序路径。
你将使用一个 LLVM pass 将 C 程序编码到我们提供的符号解释 API 中。
最终的工具将找到能使输入 C 程序崩溃的输入变量赋值。

本实验分为三个部分：
1.  在 `src/DSEInstrument.cpp` 中完成插桩函数。
2.  使用 Z3 的 C++ API，在 `src/Runtime.cpp` 中编写动态符号解释的约束逻辑。
3.  在 `src/Strategy.cpp` 中实现一个用于探索新程序路径的回溯搜索算法。

### 环境设置

Lab 7 的骨架代码位于 `/lab7` 目录下。
在描述文件位置时，我们会经常将 Lab 7 的顶级目录称为 `lab7`。

使用以下命令设置实验环境：

```sh
/lab7$ mkdir build && cd build
/lab7/build$ cmake ..
/lab7/build$ make
```

现在你应该能在当前目录（lab7/build）下看到 `dse` 和 `InstrumentPass.so`。

`dse` 是一个使用 Z3 对输入程序执行动态符号执行的工具。
你可以使用以下命令运行 dse 程序：

```sh
/lab7$ cd test
/lab7/test$ make simple0
/lab7/test$ ../build/dse ./simple0 N           # 其中 N 是迭代次数
/lab7/test$ timeout 10 ../build/dse ./simple0  # 运行 10 秒
```

初始时，你会看到 `formula.smt2` 未找到，因为你还没有实现插桩部分。

### 输入程序格式

本实验中的输入程序假定只包含 C 语言的以下子集特性：

-   所有值都是整数（即，没有浮点数、指针、结构体、枚举、数组等）。
    你可以忽略其他类型的值。
-   假定用户输入仅通过 `DSE_Input` 函数引入，并且不存在对其他函数的调用指令。

### 输入输出示例

你的 DSE 引擎应该能在给定的插桩程序上运行。
例如，以下命令将在 1 次迭代后找到一个导致崩溃的输入，并将输入存储在 `input.txt` 中：

```sh
/lab7$ cd test
/lab7/test$ make
/lab7/test$ ../build/dse ./simple0 5
Floating point exception
Crashing input found (1 iters)
/lab7/test$ cat input.txt
X0,1024
```

### 实验指导

*动态符号执行*（DSE）结合了随机测试和符号执行的技术，以搜索程序所有执行路径中的错误。
DSE 跟踪运行时值和符号约束，并在程序计算树上的回溯搜索过程中，使用前者来简化对后者的求解。

我们提供了使用 [Z3](https://github.com/Z3Prover/z3) 构建的符号解释器框架。
你需要将 C 程序编码到这个符号解释器 API 中，并编写驱动动态符号执行的代码。
在接下来的章节中，我们将提供关于如何执行此操作的几个细节。

本实验假设输入程序只包含整数变量（没有指针或其他类型的变量）并且没有函数（没有 `CallInst`）。

#### 理解 Z3

Z3 是微软开发的一个定理证明器。
它是一个庞大而复杂的工具，因此以下内容将作为其功能和能力的简要指南。
考虑一个简单的通用方程组，例如下面的例子，其中 `X` 和 `Y` 是整数：

```
X < Y
X > 2
```

虽然这个例子很简单，但请思考一下如何使用你选择的任何编程语言来解决它。
你可能会求助于使用循环来检查数字，或者寻找一个库来处理矩阵乘法。
这是因为大多数编程语言都是命令式的，这意味着需要一系列命令来解决问题。

另一方面，Z3 有一个声明式接口，在这种情况下，这意味着你只需要给它约束列表（在这个例子中是 `X < Y` 和 `X > 2`）。
将以下内容输入到[在线 Z3 求解器](https://compsys-tools.ens-lyon.fr/z3/index.php)中查看结果：

```
(declare-const x Int)
(declare-const y Int)
(assert (< x y))
(assert (> x 2))
(check-sat)
(get-model)
```

Z3 可能不会给出所有符合约束的可能结果，但重要的是，它验证了可满足性，这是本 DSE 引擎将利用的关键因素。

如果你对 Z3 感到好奇并想了解更多信息，可以查看以下资源：

-   [https://github.com/Z3Prover/z3/wiki/Documentation](https://github.com/Z3Prover/z3/wiki/Documentation)
-   [https://github.com/Z3Prover/z3/blob/master/examples/c%2B%2B/example.cpp](https://github.com/Z3Prover/z3/blob/master/examples/c%2B%2B/example.cpp)
-   [https://theory.stanford.edu/\~nikolaj/programmingz3.html](https://theory.stanford.edu/~nikolaj/programmingz3.html)

### 第一部分：LLVM 插桩

此动态符号执行实现的第一个组件是对输入程序的插桩，这在 `src/DSEInstrument.cpp` 中完成。
这遵循了先前实验中熟悉的格式和模式，不同之处在于，现在这个 LLVM pass 将注入在 `src/Runtime.cpp` 中定义的各种函数，并附带来自每个有效 LLVM 指令的适当元数据。
这将使 DSE 能够在运行时与 Z3 交互。
具体来说，以下是需要插桩的函数（来自 `include/DSEInstrument.h`）：

```cpp
static const char *DSEInitFunctionName = "__DSE_Init__";
static const char *DSEAllocaFunctionName = "__DSE_Alloca__";
static const char *DSEStoreFunctionName = "__DSE_Store__";
static const char *DSELoadFunctionName = "__DSE_Load__";
static const char *DSEConstFunctionName = "__DSE_Const__";
static const char *DSERegisterFunctionName = "__DSE_Register__";
static const char *DSEICmpFunctionName = "__DSE_ICmp__";
static const char *DSEBranchFunctionName = "__DSE_Branch__";
static const char *DSEBinOpFunctionName = "__DSE_BinOp__";
```

#### 符号输入

骨架代码提供了一个名为 `DSE_Input` 的辅助函数，供用户指定符号输入。
在目标程序中，你应该首先包含头文件 `include/Runtime.h` 才能使用该函数。
在下面的示例代码中，动态符号执行引擎会将变量 `x` 和 `y` 视为符号输入，而 `z` 具有具体值 0：

```cpp
#include "../include/Runtime.h"

int main() {
    int x, y, z;
    DSE_Input(x);
    DSE_Input(y);
    z = 0;
    ...
}
```

注意，`DSE_Input` 是一个宏，会用一个唯一的 ID 展开。
详情请参见 `include/Runtime.h` 和 `src/SymbolicInterpreter.cpp`。

初始时，DSE 引擎会为输入变量分配随机数。
在 DSE 的每次迭代之后，会生成新的输入并以逗号分隔值（CSV）的形式存储在文件 input.txt 中。
该文件将包含从 ID 到其整数值的映射。
以下是符号映射 `{X0 : 1, X1 : 10}` 的示例：

```
X0,1
X1,10
```

如果存在 `input.txt` 文件，则使用以下方法插桩的目标程序将使用文件中的整数值作为输入，而不是随机数。

#### 步骤 1：DSE 初始化的插桩

你首先需要插桩输入程序，使其在 main 函数的开头调用 `__DSE_Init__` 函数。
骨架代码在 `src/SymbolicInterpreter.cpp` 中提供了 `__DSE_Init__` 的定义。
该函数在 `input.txt` 存在时初始化输入，并注册一个回调函数 `__DSE_Exit__`，该函数将在目标程序正常终止时被调用。
骨架代码还提供了 `__DSE_Exit__` 的定义，用于存储已覆盖的分支列表（在 `branch.txt` 中）、路径公式（在 `formula.smt2` 中）和日志（在 `log.txt` 中）。
简而言之，你的插桩模块应将左侧的代码转换为右侧的代码：

<table>
<tbody>
<tr valign="top">
<td>
<pre><code>
define dso_local i32 @main() #0 {
entry:
    %retval = alloca i32, align 4
    ...
</pre></code>
</td>
<td>
<pre><code>
define dso_local i32 @main() #0 {
entry:
    call void @__DSE_Init__();
    %retval = alloca i32, align 4
    ...
</pre></code>
</td>
</tr>
</tbody>
</table>

#### 步骤 2：IR 指令的插桩

接下来，你需要插桩其余的 IR 指令。
通常，如果指令中的某个操作数会改变符号内存状态，则应对其进行插桩。
常量使用 `__DSE_Const__` 函数进行插桩，寄存器使用 `__DSE_Register__` 函数进行插桩（详情见下一节）。
此外，`Alloca` 指令的插桩函数调用必须出现在指令*之后*，而所有其他指令的插桩函数调用必须出现在指令*之前*。
`__DSE_ICmp__` 和 `__DSE_BinOp__` 将左侧寄存器的 ID 作为第一个参数，将其 LLVM 操作码（分别是 `llvm::CmpInst::Predicate` 和 `llvm::Instruction::BinaryOps`）作为第二个参数。
我们提供了一些插桩示例（为便于阅读，函数调用已简化）：

<table>
<tbody>
<tr valign="top">
<td>
<pre><code>
...
  %x = alloca i32, align 4
...
</pre></code>
</td>
<td>
<pre><code>
...
  %x = alloca i32, align 4 
  __DSE_Alloca__(i32 1, i32* %x)
...
</pre></code>
</td>
</tr>
<tr valign="top">
<td>
<pre><code>
...
  store i32 0, i32* %retval, align 4
...
</pre></code>
</td>
<td>
<pre><code>
...
  __DSE_Const__(i32 0)
  __DSE_Store__(i32* %retval)
  store i32 0, i32* %retval, align 4
...
</pre></code>
</td>
</tr>
<tr valign="top">
<td>
<pre><code>
...
  %cmp = icmp eq i32 %1, 1024
...
</pre></code>
</td>
<td>
<pre><code>
...
  __DSE_Register__(i32 5)
  __DSE_Const__(i32 1024)
  __DSE_ICmp__(i32 6, i32 32)
  %cmp = icmp eq i32 %1, 1024
...
</pre></code>
</td>
</tr>
</tbody>
</table>

### 第二部分：运行时符号解释

本实验的第二个组件涉及在 `src/Runtime.cpp` 中编写运行时符号解释函数。
在之前的实验中，插桩函数已经提供，但这次你需要自己编写。
当这些函数在运行时被调用时，它们会改变符号内存状态和路径条件。
在这里，你将使用 Z3 API 为符号解释器类添加约束。

#### LLVM 指令的符号解释

你需要为每个 LLVM 指令定义符号操作函数，并插桩输入程序以在运行时调用这些函数。
跟随程序的真实执行，DSE 引擎操作一个符号内存状态。
`include/SymbolicInterpreter.h` 中的 `SymbolicInterpreter` 类维护着符号内存，该内存被定义为从符号地址到符号表达式的映射。
它还维护着一个符号表达式栈。

`Address` 类的实例代表一个符号内存地址。
符号地址可以是内存地址或寄存器，遵循 LLVM IR 的定义。
`Type` 字段表示地址的类型。
对于内存地址（通过 LLVM 的 `AllocaInstruction` 分配），我们将使用它们的物理地址作为符号地址。
对于寄存器，我们将通过 `DSEInstrument.h` 中的 `getRegisterID()` 分配唯一的寄存器 ID。
对于符号表达式，你将重用 Z3 的表达式，它们是 `z3::expr` 类的实例。

具体执行的符号操作是使用两个辅助函数 `__DSE_Const__` 和 `__DSE_Register__` 执行的，每个函数将具体常量和寄存器编码为其符号对应物。
这些函数在 `src/SymbolicInterpreter.cpp` 中定义。
函数 `__DSE_Const__` 接收一个 LLVM IR 的常量整数，为该数字创建一个符号表达式，并将该符号表达式推入栈中（类 `SymbolicInterpreter` 中的 `Stack` 字段）。
函数 `__DSE_Register__` 接收一个 LLVM 寄存器的 ID，并将其符号对应物推入栈中。
栈中的每个元素要么是一个常量，要么是一个寄存器。
栈中的符号表达式将用于后续的插桩函数。

你将使用这些辅助函数为 LLVM 指令定义符号操作函数。
考虑以下 LLVM 代码，它等价于一个简单的 C 程序 `int x = 1; int y = x;`（为简单起见省略了类型）：

| 插桩后的代码              | 具体内存       | 栈            | 符号内存           |
| ----------------------- | --------------- | ------------- | ----------------- |
| `%x = alloca`           | `%x : 0x1000`   |               |                   |
| `__DSE_Alloca__(0,%x)`  |                 | `[]`          | `Reg(0) : 0x1000` |
| `%y = alloca`           | `%y : 0x1004`   |               |                   |
| `__DSE_Alloca__(1,%y)`  |                 | `[]`          | `Reg(1) : 0x1004` |
| `__DSE_Const__(1)`      |                 | `[Const(1)]`  |                   |
| `__DSE_Store__(%x)`     |                 | `[]`          | `0x1000 : 1`      |
| `store 1, %x`           | `0x1000 : 1`    |               |                   |
| `__DSE_Load__(2,%x)`    |                 | `[]`          | `Reg(2) : 1`      |
| `%a = load %x`          | `%a : 1`        |               |                   |
| `__DSE_Register__(2)`   |                 | `[Reg(2)]`    |                   |
| `__DSE_Store__(%y)`     |                 | `[]`          | `0x1004 : 1`      |
| `store %a, %y`          | `0x1004 : 1`    |               |                   |

-   `__DSE_Alloca__` 接收左侧寄存器的 ID 和新分配的物理内存块的地址。
    在上面的例子中，`%x` 的 ID 是 0，物理内存地址是 0x1000。
    第 2 行之后的符号内存将包含条目 `Reg(0) : 0x1000`。
-   `__DSE_Store__` 假设栈顶存在其值操作数（常量或寄存器）的符号表达式。
    它接收一个物理内存地址作为参数，并将该符号表达式存储在该地址。
-   `__DSE_Load__` 接收左侧寄存器的 ID 和物理内存块的地址，该内存块的值将被加载到该寄存器中。

其他符号操作函数的行为以类似的方式定义。
`__DSE_ICmp__` 和 `__DSE_BinOp__` 接收左侧寄存器的 ID 及其 LLVM 操作码（分别是 `llvm::CmpInst::Predicate` 和 `llvm::Instruction::BinaryOps`）。
骨架代码在 `SymbolicInterpreter.cpp` 中提供了 `__DSE_Branch__` 的实现作为参考。

#### 使用 Z3 表达式

像 `llvm::Inst::CmpInst` 和 `llvm::BinaryOperator` 这样的指令操作符号，并且需要在约束中进行等效表示。
你将使用 Z3 表达式来表示这些操作。
Z3 API 使用 C++ 的一个称为[运算符重载](https://en.cppreference.com/w/cpp/language/operators)的特性，允许你对 `z3::expr` 类型的对象使用 C++ 算术和比较运算符。
我们在下面展示了一些示例，用于表示对 `z3::expr` 对象的算术和比较表达式。
这些示例假设 E1 和 E2 是两个 `z3::expr` 类型的对象，它们的结果存储在另一个 `z3::expr` 类型的对象 E 中。

| 操作     | 表示方式       |
| -------- | -------------- |
| 加法     | `E = (E1 + E2)` |
| 小于     | `E = (E1 < E2)` |

### 第三部分：回溯策略

回想一下“示例 1：组合方法”讲座视频中，为了 DSE 分析能够探索输入测试程序的更多路径，是如何处理条件的。
修改 `src/Strategy.cpp` 中的 `searchStrategy()` 函数以执行此回溯行为。
它应该修改当前将提供给 Z3 的路径公式，以便推导出新的输入。

#### 路径公式与搜索策略

在每次执行插桩程序后，路径公式将被编码并存储在 `formula.smt2` 中。
所有已执行分支指令的 ID 将按执行顺序存储在 `branch.txt` 中，这可能有助于生成下一个输入。
给定当前可满足的路径公式，`searchStrategy` 函数将提出一个公式，以推导出能够探索更多路径的新输入。
`DSE.cpp` 中的 main 函数将迭代地生成新输入，直到找到导致崩溃的输入或发生超时。

### 提交

完成实验后，你可以使用以下命令创建一个 `submission.zip` 文件：

```sh
lab7$ make submit
...
submission.zip created successfully.
```

然后将提交文件上传到助教的邮箱。

<!-- TOC --><a name="dynamic-symbolic-execution"></a>
# 动态符号执行

<!-- TOC start -->

- [动态符号执行](#dynamic-symbolic-execution)
   * [1. 实验目标](#1-实验目标)
   * [2. 快速开始](#2-快速开始)
      + [2.1 示例程序](#21-示例程序)
      + [2.2 功能限制](#22-功能限制)
      + [2.3 环境配置](#23-环境配置)
    * [3. 理解 `miniklee` 的工作流程](#3-理解-miniklee-的工作流程)
   * [4. 任务 1：实现符号化过程](#4-任务-1实现符号化过程)
      + [4.1 你需要了解的函数](#41-你需要了解的函数)
      + [4.2 提示](#42-提示)
      + [4.3 概念验证 (POC)](#43-概念验证-poc)
   * [5. 任务 2：解释 `Add` 和 `Sub` 的语义](#5-任务-2解释-add-和-sub-的语义)
      + [5.1 你需要了解的函数](#51-你需要了解的函数)
      + [5.2 提示](#52-提示)
      + [5.3 概念验证 (POC)](#53-概念验证-poc)
   * [6. 任务 3：解释 `Br` 的语义](#6-任务-3解释-br-的语义)
      + [6.1 你需要了解的函数](#61-你需要了解的函数)
      + [6.2 提示](#62-提示)
      + [6.3 概念验证 (POC)](#63-概念验证-poc)
   * [7. 提交方式](#7-提交方式)


<a name="0-attention"></a>
## 0. 注意事项

> 由于 Windows 的虚拟化机制与我们较旧的 Docker 镜像存在差异，请注意以下调整

**如果你使用的是 Windows，请改用 WSL2。**

打开 PowerShell，下载 WSL2，并执行以下命令：

``` bash
wsl --install -d Ubuntu
```
（可选）在 PowerShell 中，将 Ubuntu 设置为默认操作系统：

``` bash
wsl --set-default Ubuntu
```
打开 WSL2，下载你的仓库，并使用 VSCode（使用 Windows 版本的 VSCode，无需单独下载）打开它：

``` bash
lab8: code .
```
确保 VSCode 已安装 Docker 和 Dev Container 扩展，然后重新打开容器即可。

此外，一个潜在的问题是当前容器中的 LLVM 版本过旧，不适合运行 MiniKLEE。为了解决这个问题，我添加了一个热补丁，让容器在启动时**自动**从网络下载合适的 LLVM 版本。但是，对于**网络状况不佳**的同学，最好切换到国内镜像，例如阿里云或清华镜像。切换镜像后，重新下载相应的 LLVM 版本。你可以选择重启容器让它**自动下载**，或者**手动下载**：

``` bash
lab8$ rm llvm.sh                        # 删除当前的 llvm.sh
lab8$ wget https://apt.llvm.org/llvm.sh # 从网络下载 llvm.sh
lab8$ chmod +x llvm.sh                  # 赋予执行权限
lab8$ ./llvm.sh 14 all                  # 执行以下载 LLVM 14 版本
```

> 对于实验准备仓促以及可能带来的不便，我深表歉意。


<a name="1-实验目标"></a>
## 1. 实验目标

在本实验中，你将实现一个动态符号执行 (DSE) 引擎 `miniklee`，包括：

1.  实现符号化过程
2.  实现一个基于执行生成测试 (EGT) 的符号执行框架。
    1.  解释 `Add` 和 `Sub` 的语义
    2.  解释 `Br` 的语义

<!-- TOC --><a name="2-快速开始"></a>
## 2. 快速开始

<!-- TOC --><a name="21-示例程序"></a>
### 2.1 示例程序

我们提供了可执行文件 `refminiklee`（位于 `./` 目录下），方便你快速了解符号执行。

我们的示例程序如下。假设 `__builtin_trap()`（第 9 行）是程序中的 bug。程序首先将变量 `a` 设为符号变量。然后，它遇到了一个 `if` 分支（`if (a + 2 == 100 - 10)`）。当变量 `a` 的值被设为 88 时，可以触发这个假设的 bug。

``` c
   1 #include "Symbolic.h"
   2 
   3 int main() {
   4     int a;
   5     make_symbolic(&a, sizeof(a), "a");
   6 
   7     if (a + 2 == 100 - 10) {
   8         // Trap, a must be 88
   9         __builtin_trap();
  10     } else {
  11         // Should reach, a can be assigned all values that are not 88
  12     }
  13 
  14     return 0;
  15 }
```

`refminiklee` 的工作流程如下：
1.  它将（第 5 行的）变量 `a` 在虚拟机内存中标记为符号变量。
2.  接着，它检查 if 分支（第 7 行），将分支语句编码为约束条件（`a + 2 == 100 - 10`），然后将其与之前的路径约束（本例中无）一起发送给约束求解器。
3.  然后，求解器判断这些约束的可行性，结果为“真分支和假分支都可行”。
4.  `miniklee` 随后分叉状态，并将新状态更新到状态池中。
5.  对于进入真分支的状态，`miniklee` 生成一个测试用例（后缀为 `.error`），其中 `a = 88`；对于假分支，它生成一个测试用例（后缀为 `.normal`），其中 `a` 为不等于 88 的随机值。

**以下展示了如何使用 `refminiklee` 对上述示例进行符号探索**：

1.  将待测程序编译为 LLVM IR，**不进行任何优化**

``` bash
$ clang -emit-llvm -g -O0 -S ./test/example.c -o ./test/example.ll -I./include
```

2.  使用 `refminiklee` 对生成的 LLVM IR（`./test/example.ll`）执行符号执行

``` bash
$ ./refminiklee ./test/example.ll
LLVM IR file loaded successfully
State 1: Alloca
State 1: Alloca
State 1 Store
State 1 Mk Sym
State 1 Load
State 1 Add
State 1 ICMP_EQ comparison
State 1 Br
Assigning 88 
Test case written successfully (result_1/test_case_1.error)
State 2 Br
State 2 Ret
Assigning -1634890980 
Test case written successfully (result_1/test_case_2.normal)
```

3.  检查生成的测试用例

``` bash
$ cat result_1/test_case_1.error
a, 88
$ cat result_1/test_case_2.normal
a, -1634890980
```

`test_case_2.normal` 的值是随机生成的，只要它不是 88 即可。

<!-- TOC --><a name="22-功能限制"></a>
### 2.2 功能限制

为简化起见，本实验中的输入程序被假定为**仅包含 C 语言的以下子集功能**：
-   所有值都是 32 位有符号整数（即没有浮点数、指针、结构体、枚举、数组等）
-   待测程序只包含 `main` 函数，意味着没有函数调用
-   涉及符号变量的条件只能是相等或不相等
-   仅涉及以下操作：
    -   [Alloca](https://llvm.org/doxygen/classllvm_1_1AllocaInst.html)：在栈上分配内存的指令
    -   [Load](https://llvm.org/doxygen/classllvm_1_1LoadInst.html)：从内存读取的指令
    -   [Store](https://llvm.org/doxygen/classllvm_1_1StoreInst.html)：存储到内存的指令
    -   [Ret](https://llvm.org/doxygen/classllvm_1_1ReturnInst.html)：返回值并转移控制流的指令
    -   [Eq](https://llvm.org/doxygen/classllvm_1_1ICmpInst.html)：根据谓词比较其操作数（是否相等）的指令
    -   [SLT](https://llvm.org/doxygen/classllvm_1_1ICmpInst.html)：根据谓词比较其操作数（是否小于）的指令
    -   [Br](https://llvm.org/doxygen/classllvm_1_1BranchInst.html)：条件或无条件分支指令
    -   [Call](https://llvm.org/doxygen/classllvm_1_1CallInst.html)：抽象目标机器调用约定的指令
    -   [Add](https://codebrowser.dev/llvm/llvm/include/llvm/IR/Instruction.def.html#147)：对两个操作数执行整数加法并产生其和的指令
    -   [Sub](https://codebrowser.dev/llvm/llvm/include/llvm/IR/Instruction.def.html#149)：执行整数减法，从第一个操作数中减去第二个操作数，并产生结果的指令

<!-- TOC --><a name="23-环境配置"></a>
### 2.3 环境配置

要构建你自己的 `miniklee`，只需在 `lab8` 目录下输入 `make`：

``` bash
$ make
```

然后你会在当前目录下得到你当前版本的 `miniklee`，它目前只能测试简单的测试用例（例如 `test/sequential.c`）：

``` bash
$ clang -emit-llvm -g -O0 -S -I./include test/sequential.c  -o test/sequential.ll
$ ./miniklee test/sequential.ll
LLVM IR file loaded successfully
State 1: Alloca
State 1: Alloca
State 1: Alloca
State 1 Store
State 1 Store
State 1 Store
Assigning -2082133583 
Test case written successfully (result_1/test_case_1.error)
```

你可以在终端日志中观察到一个生成的测试用例（例如 `-2082133583`，一个随机生成的值）。但是，`result_1/test_case_1.error` 中没有分配的值，因为 `sequential.c` 中没有符号变量。换句话说，`sequential.c` 没有接收任何输入。

你的第一个任务是让变量变为符号变量（在第 4 节中）。

<!-- TOC --><a name="3-理解-miniklee-的工作流程"></a>

## 3. 理解 `miniklee` 的工作流程

-   `src/main.cpp`

`main` 函数接收一个 LLVM IR 文件并解析它，然后将控制流传递给符号执行器。

-   `src/Executor.cpp:runFunctionAsMain`

准备工作完成后，`miniklee` 在 `runFunctionAsMain` 函数中执行符号执行：

1.  它从一个初始状态开始，并使用一个状态池（`states`）进行存储。
2.  在主循环中，如果状态池不为空，则继续：
    1.  选择一个状态来执行。
    2.  获取要执行的下一条指令。
    3.  执行该指令并进行分析。
    4.  通过添加新状态和移除死亡状态来更新状态池。
3.  当一个状态到达终止点时，为该状态生成一个测试用例。

-   `src/Executor.cpp:executeInstruction`

专注于指令执行，这部分主要是一个大的 `switch-case` 语句。它识别并解释获取到的指令。例如：
-   解释 `Ret` 指令会终止当前状态。
    -   `src/Executor.cpp:terminateState`
        -   为当前状态生成测试用例
        -   移除即将结束的状态
-   解释 `Br` 指令会将控制权转移到下一个基本块。
    -   `src/Executor.cpp:fork`
        -   调用求解器判断当前分支条件的可行性
        -   根据求解器的结果分叉状态
-   解释 `Add` 指令会对两个操作数执行整数加法。


<!-- TOC --><a name="4-任务-1实现符号化过程"></a>
## 4. 任务 1：实现符号化过程

如第 3 节所述，`miniklee` 根据相应的语义解释每条指令。有了解释，我们可以设计如何解释符号化的语义并实现它。

**实现 `src/Executor.cpp:executeMakeSymbolic` 函数。我们提供了标记为 “Task 1: Your Code Here” 的代码骨架。**

<!-- TOC --><a name="41-你需要了解的函数"></a>
### 4.1 你需要了解的函数

-   `include/Symbolic.h:make_symbolic`

我们已经在 `include/Symbolic.h` 中提供了符号化的函数声明：

```c++
void make_symbolic(int32_t *sym, size_t nbytes, const char *name);
```

`make_symbolic` 函数接收三个参数：
1)  要符号化的变量的地址
2)  变量的字节数
3)  赋予变量的名称。

我们可以在待测程序中使用它，如下面的代码片段所示。实际上，KLEE 符号执行器也使用这种方法来标记一个变量为符号变量（KLEE 官方文档 [Marking input as symbolic](https://klee-se.org/tutorials/testing-function/)）。

``` c++
1: int a;
2: make_symbolic(&a, sizeof(a), "a"); // 变量 a 现在应该被符号化
3: if (a + 2 == 100 - 10) { ...  }
```

-   `src/Executor.cpp:executeInstruction`

请关注 `Call` 指令的情况：当 `miniklee` 执行 `make_symbolic` 语句（代码片段 1 中的第 2 行）时，它会识别并处理符号化。

-   `src/Executor.cpp:needsSymbolization`

识别当前调用是否为 `make_symbolic` 函数。

-   `src/Executor.cpp:processMakeSymbolic`

解析 `make_symbolic` 的参数，并继续将它们符号化。

<!-- TOC --><a name="42-提示"></a>
### 4.2 提示

**提示 1：阅读友好的代码**
-   阅读 `Load` 和 `Store` 指令的代码解释（`src/Executor.cpp:executeInstruction`）可能有助于理解 `miniklee` 的存储系统（**特别是函数 `include/Executor.h:executeMemoryOperation`**）
-   阅读建模指令的代码解释（`include/Expr.h`）可能有助于理解符号执行中每个数据的表示。

 **提示 2：深入理解程序的表示**

 我们从不同的角度表示程序，例如：
 -   **源代码**
   这是程序的具体语法，其优点是易于阅读，但难以转换、分析和优化。下面是一个计算存储在 `value` 中的数字（本例中为 `8`）的阶乘的例子。
 ``` c++
 int value = 8;
 int result = 1;
 for (int i = 1; i <= value; ++i) {
     result *= i;
 }
 std::cout << result << std::endl;
 ```

 -   **抽象语法树**
 ```
       program
             |
         block
      /      |     \
  alloc load store ...
 ```

   [抽象语法树](https://en.wikipedia.org/wiki/Abstract_syntax_tree) (AST) 表示有利于编译器，因为它简化了解析和分析。对于解释器来说，它特别有用——递归处理树可以轻松地通过解释每个语句并更新程序环境来评估块。AST 的主要缺点是其节点类型的多样化行为。编写编译器分析需要不断处理这些节点类型之间的语义差异，这可能很繁琐。存在其他更适合实现复杂编译器优化的表示形式。这些方法使表示更加规则，从而简化了过程。

 -   **指令**（特别是 LLVM IR）
   LLVM IR 采用静态[单一赋值](https://en.wikipedia.org/wiki/Static_single_assignment_form) (SSA) 形式，这在 [LLVM IR 讲座](https://tingsu.github.io/files/courses/slides/lec-2-llvm-framework-primer.pdf)中已经解释过。我们喜欢指令表示，因为它具有规则性。然而，要利用它做任何有用的事情，我们需要提取更高级别的表示（**`miniklee` 是在基本块和指令级别上工作的**）：
   -   [控制流图](https://en.wikipedia.org/wiki/Control-flow_graph) (CFG)。
   -   [基本块](https://en.wikipedia.org/wiki/Basic_block)。
   -   终结指令（此处为 jmp 和 br）。
   -   推导形成基本块的算法。
   -   后继与前驱。
   -   推导形成基本块 CFG 的算法。

   我们欣赏 LLVM IR，特别是它的 SSA（静态单一赋值）属性：每个变量在全局范围内只有一个静态赋值。然而，这并不意味着动态单一赋值，因为同一个语句可以执行多次。 总结一下，在 LLVM IR 代码中：
   -   定义 == 变量
   -   指令 == 值
   -   参数 == 数据流图边

**提示 3：“太长不看；我只想躺平。”**

有这种感觉很正常。一步一步来，你已经做得很好了！💪。

让我们将符号化的步骤分解如下：
1.  使用提供的类型 `SymbolicExpr` 表示符号值
2.  使用 `executeMemoryOperation` 将创建的符号值存储到符号内存中

答案如下：

``` c++
void Executor::executeMakeSymbolic(ExecutionState& state,
                                   Instruction *symAddress,
                                   std::string name) {
    // 将要符号化的变量（Instruction 类型）注册为符号变量
    executeMemoryOperation(state, true, symAddress, 
                           SymbolicExpr::create(name), 0);
}
```


<!-- TOC --><a name="43-概念验证-poc"></a>
### 4.3 概念验证 (POC)

实现任务 1 后，运行测试用例 `test/symbolic.c` 来验证你的更改。此测试引入了符号变量，让你可以观察符号执行引擎如何处理它们。检查生成的测试输入，确保符号输入被识别并正确处理。

预期结果：

``` bash
$ make clean
$ make
... 编译日志省略 ...
$ clang -emit-llvm -g -O0 -S -I./include test/symbolic.c  -o test/symbolic.ll
$ ./miniklee test/symbolic.ll
LLVM IR file loaded successfully
State 1: Alloca
State 1: Alloca
State 1 Store
State 1 Mk Sym
Assigning -399613364
Test case written successfully (result_1/test_case_1.error)
```
现在你可以看到 `result_1/test_case_1.error` 中为符号值 `a`（假定为程序输入）分配了一个值（此处 `-399613364` 是随机生成的）。

<!-- TOC --><a name="5-任务-2解释-add-和-sub-的语义"></a>
## 5. 任务 2：解释 `Add` 和 `Sub` 的语义

如第 3 节所述，`miniklee` 根据相应的语义解释每条指令。有了解释，我们可以设计如何解释 `Add` 和 `Sub` 指令的语义并实现它们。

**为 `Add` 和 `Sub` 实现语义解释（`src/Executor.cpp:executeInstruction`）。我们提供了标记为 “Task 2: Your Code Here.” 的代码骨架。**

<!-- TOC --><a name="51-你需要了解的函数"></a>
### 5.1 你需要了解的函数

-   `src/Executor.cpp:executeInstruction`

请关注 `Add` 和 `Sub` 指令的情况，当 `miniklee` 执行 `Add` 或 `Sub` 语句时，它会识别并处理该指令。

<!-- TOC --><a name="52-提示"></a>
### 5.2 提示

**提示 1：“太长不看；我只想躺平。”**

阅读 KLEE 友好的源代码以获得灵感。
-   [KLEE 处理 `Add` 的代码](https://github.com/klee/klee/blob/master/lib/Core/Executor.cpp#L2582)
-   [KLEE 处理 `Sub` 的代码](https://github.com/klee/klee/blob/master/lib/Core/Executor.cpp#L2589)

<!-- TOC --><a name="53-概念验证-poc"></a>
### 5.3 概念验证 (POC)

实现任务 2 后，运行测试用例 `test/example.c` 来验证你的更改。此测试引入了 `add` 操作、`sub` 操作和分支条件，让你可以观察 `miniklee` 如何处理它们。

`example.c` 的内容

``` c++
#include "Symbolic.h"
int main() {
    int a;
    make_symbolic(&a, sizeof(a), "a");

    if (a + 2 == 100 - 10) {
        // Trap, a must be 88
        __builtin_trap();
    } else {
        // Should reach, a can be assigned all values that are not 88
    }
    
    return 0;
}
```

运行测试

``` bash
$ make clean
$ make
... 编译日志省略 ...
$  clang -emit-llvm -g -O0 -S ./test/example.c -o ./test/example.ll -I./include
$ ./miniklee test/example.ll
LLVM IR file loaded successfully
State 1: Alloca
State 1: Alloca
State 1 Store
State 1 Mk Sym
State 1 Load
State 1 Add
State 1 ICMP_EQ comparison
State 1 Br
Assigning -732525800 
Test case written successfully (result_1/test_case_1.error)
```

看起来不错。但有些问题：`miniklee` 探索了真分支，并为符号变量 `a` 分配了一个不会触发崩溃的值（此处 `-732525800` 是随机生成的）（该值应为 `88`）。

**为什么？这是因为分支指令没有被正确处理。** 在当前版本中，当 `miniklee` 遇到分支指令时，它简单地认为条件为真并探索真分支（阅读 `src/Executor/cpp:executeInstruction` 中处理 `Br` 指令的 switch-case 源代码）。

你的任务 3 是正确处理它。

<!-- TOC --><a name="6-任务-3解释-br-的语义"></a>
## 6. 任务 3：解释 `Br` 的语义

**为 `Br` 实现语义解释（`src/Executor.cpp:executeInstruction` 和 `src/Executor.cpp:fork`）。我们提供了标记为 “Task 3: Your Code Here” 的代码骨架。**

分支处理是执行生成测试 (EGT) 符号执行器的核心。在继续之前，让我们回顾一下[它的背景](https://dl.acm.org/doi/10.1145/2408776.2408795)。

目前有两种类型的符号执行：

-   **混合符号执行 (Concolic Testing)**：使用随机输入开始执行，执行后，使用当前路径的路径条件 pc₀（通过否定最后一个条件）构建一个新的路径条件 pc₁，并求解 pc₁ 以获得新的输入 I₁ 来探索新路径，然后重复该过程。如 [CREST](https://www.burn.im/crest/) 和 [DART](https://dl.acm.org/doi/10.1145/1064978.1065036) 中所示。
_我们之前的实验属于这种类型，[MIT 6.858: Computer System Security Lab 3: Symbolic Execution](https://css.csail.mit.edu/6.858/2022/labs/lab3.html) 也是如此。_

-   **执行生成测试 (EGT)**：在每个条件分支处（如果两个方向都可行）分叉符号执行，维护多个部分路径，并协调它们同时执行。如 [EXE](https://dl.acm.org/doi/10.1145/1455518.1455522)、[SPF](https://dl.acm.org/doi/10.1145/1858996.1859035) 和 [KLEE](https://dl.acm.org/doi/10.5555/1855741.1855756) 中所示。
_这是 `miniklee` 实现的类型。_

如上所述，EGT 执行器在每个条件分支处，如果两个方向都可行，则分叉其执行。你的任务是实现用于解释 `Br` 指令的 `fork` 函数。

<!-- TOC --><a name="61-你需要了解的函数"></a>
### 6.1 你需要了解的函数

-   `src/Executor.cpp:executeInstruction`

-   `src/Executor.cpp:transferToBasicBlock`

更新程序计数器，将执行状态转移到指定基本块的起始位置。

-   `src/Executor.cpp:getInstructionValue`

获取相应指令定义的符号值。

<!-- TOC --><a name="62-提示"></a>
### 6.2 提示

 **提示 1：理解 `miniklee` 中执行 `Br` 的工作流程**
 
 当执行器处理 `Br` 指令时，它首先将其转换为相应的 `Br` 类型（[讲座 The LLVM Framework, p.37](https://tingsu.github.io/files/courses/slides/lec-2-llvm-framework-primer.pdf)）。然后它使用 API（[BranchInstr 的 isUnconditional](https://llvm.org/doxygen/classllvm_1_1BranchInst.html#a7e4be8b16fbd68c9045a388904044e01)）来判断分支是无条件还是条件分支，并分别处理每种情况：
 
 -   **无条件**：将执行状态转移到下一个基本块。
 -   **条件**：提取条件并将其发送给求解器以检查可行性：
     -   **真分支可行**：转移到真分支的基本块。
     -   **假分支可行**：转移到假分支的基本块。
     -   **两个分支都可行**：为每个分支分叉出新状态，将控制权转移到它们各自的基本块，并将分叉出的状态添加到状态池中。
 
 
 **提示 2：理解 `fork` 函数的工作流程**
 
 为了减少做实验的痛苦，我们已经为 `fork` 函数（`src/Executor.cpp:fork`）提供了一个骨架，`fork` 的工作方式如下：
 
 -   **调用求解器判断分支的可行性**：它首先调用求解器，检查对于给定的查询（路径约束下的真分支和假分支），是否存在一个有效的赋值使得条件为真。明确地说，如果真分支可行，我们说 `trueBranch` 被设为 true；否则为 false。类似地，如果假分支可行，`falseBranch` 被设为 true；否则为 false。你可以按如下方式实现这部分：

``` c++
    // 调用求解器判断条件的可行性
    bool trueBranch = solver->evaluate(
        Query(current.constraints, condition)
    );
    bool falseBranch = solver->evaluate(
        Query(current.constraints, NotExpr::create(condition))
    );
```

 -   **根据求解器的结果执行操作。**
     -   **`trueBranch` 为真，`falseBranch` 为假**
         -   只需将当前状态作为 `StatePair` 的第一个位置返回
     -   **`falseBranch` 为真，`trueBranch` 为假**
         -   只需将当前状态作为 `StatePair` 的第二个位置返回
     -   **`trueBranch` 和 `falseBranch` 都为真**
         -   克隆当前状态（_阅读 `src/ExecutionState.cpp` 中 `ExecutionState` 提供的 API 可能会有所帮助_）
         -   将新克隆的状态添加到状态池中（_推送到全局变量 `addedStates` 即可；不要直接操作状态池 `states`_）
         -   将当前条件添加到当前状态（通过真分支的状态），并将取反后的条件添加到克隆状态（通过假分支的状态）
         -   在 `StatePair` 中返回这两个状态

**提示 3：“太长不看；我只想躺平。”**

阅读 KLEE 友好的源代码以获得灵感。
-   [KLEE 处理 `Br` 的代码](https://github.com/klee/klee/blob/master/lib/Core/Executor.cpp#L2218)
-   [KLEE 的 fork 函数代码](https://github.com/klee/klee/blob/master/lib/Core/Executor.cpp#L1039)

<!-- TOC --><a name="63-概念验证-poc"></a>
### 6.3 概念验证 (POC)
实现任务 3 后，运行测试用例 `test/example.c` 来验证你的更改。你现在应该看到与运行 `refminiklee` 相同的结果（除了随机生成的值）。请根据 [2.1 示例程序](#21-示例程序) 进行自我检查。

<!-- TOC --><a name="7-提交方式"></a>
## 7. 提交方式

完成实验后，通过提交并推送 lab8/ 目录下的更改来提交你的代码。具体来说，你需要提交对 `src/Executor.cpp` 的更改。

``` bash
   lab8$ git add src/Executor.cpp
   lab8$ git commit -m "你的提交信息"
   lab8$ git push
```

