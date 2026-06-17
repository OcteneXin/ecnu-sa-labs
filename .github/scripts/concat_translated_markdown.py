from pathlib import Path

# ------------------------pdf元数据，不要的参数可以删除--------------------------
# toc                               是否生成目录
# toc-own-page                      目录是否单独一页
# titlepage                         是否生成封面
# number-sections                   标题是否编号
# toc-depth: 2                      目录最深层级
# shift-heading-level-by: -1        编号偏移量，不要动
# syntax-highlighting: idiomatic    代码块样式
# ============以下3个必须同时删除，删除后，每个lab结束时将无法自动分页================
# book                              是否采用书籍排版（每个大标题分页）
# classoption: [oneside]            单栏排版
# top-level-division: chapter       配合此排版使用
# ===========================================================================
YAML_HEADER = '''---
title: "软件分析与测试实验手册"
author: [ecnu-sa-labs]
date: "2026-06-01"
lang: "zh"
toc: true
toc-own-page: true
titlepage: true
number-sections: true
toc-depth: 2
shift-heading-level-by: -1
syntax-highlighting: idiomatic
book: true
classoption: [oneside]
top-level-division: chapter
...

'''

# 以下文件的根目录
BASE_FOLDER = "lab_manual_cn"

# 用于生成pdf的文件名，严格按顺序排列
MARKDOWN_FILE_ARRAY = [
    'course-vm.md',
    'lab1.md',
    'lab2.md',
    'lab3.md',
    'lab4.md',
    'lab5.md',
    'lab6.md',
    'lab7.md',
    'lab8.md',
    'lab9-MiniCREST.md',
    'lab9.md'
]

OUTPUT_FILE = 'output.md'

if __name__ == "__main__":
    final_markdown = YAML_HEADER

    for file in MARKDOWN_FILE_ARRAY:
        input_path = Path(f"{BASE_FOLDER}/{file}")
        with input_path.open("r", encoding="utf-8") as f:
            original_content = f.read()

        final_markdown += original_content

        final_markdown += '\n'

    output_path = Path(f"{BASE_FOLDER}/{OUTPUT_FILE}")
    with output_path.open("w", encoding="utf-8") as f:
        f.write(final_markdown)    