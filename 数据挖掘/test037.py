#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:TBH time:2019/9/10

import jieba

text = "我喜欢上海东方明珠"
ci_1 = jieba.cut(text, cut_all=True)   #全模式
for item in ci_1:
    print(item)

print("")

ci_2 = jieba.cut(text, cut_all=False)   #标准模式(省略cut_all，默认标准模式)
for item in ci_2:
    print(item)

print("")

ci_3 = jieba.cut_for_search(text)       #搜索引擎模式
for item in ci_3:
    print(item)