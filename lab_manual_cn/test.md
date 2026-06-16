---
CJKmainfont: Noto Serif CJK SC
CJKsansfont: Noto Sans CJK SC
CJKmonofont: Noto Sans Mono CJK SC
---
## 理解静态分析与动态分析

理解软件分析的基本概念以及用于评估分析有效性的度量指标。

### 目标

本实验的目标是使用标准的静态与动态分析工具对 C 程序进行分析，以发现除零错误，并解读其结果，从而更好地理解各种技术之间的权衡。具体来说，我们将使用 <a href="https://github.com/google/AFL">AFL</a>（American Fuzzy Lop，一种动态分析器/模糊测试器）和 <a href="https://clang-analyzer.llvm.org/">CSA</a>（Clang 静态分析器）。

### 前置要求

课程讲座介绍了本实验中使用的各种术语，例如：静态分析与动态分析、可靠性、完备性、精确率、召回率等。