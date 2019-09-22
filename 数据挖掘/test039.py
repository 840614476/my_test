#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:TBH time:2019/9/10

import jieba.analyse
import jieba.posseg

#更改词频
#
text  = "我喜欢上海东方明珠"

#jieba.add_word("上海东方", freq=700)
ci_1 = jieba.cut(text)
for item in ci_1:
    print(item)

print("")

#分析关键词
#
text2  = "我喜欢上海东方明珠"
tag = jieba.analyse.extract_tags(text2, 3)
print(tag)

print("")

#返回词语的位置
#
pos = jieba.tokenize(text2)
for item in pos:
    print(item)