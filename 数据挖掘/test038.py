#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:TBH time:2019/9/10

import jieba.posseg

#词性标注
#
text  = "我喜欢上海东方明珠"

ci_1 = jieba.posseg.cut(text)
#  item.word  词语
#  item.flag  词性
for item in ci_1:
    print(item.word + "---" + item.flag)

print("")

#词典加载
#
jieba.load_userdict("E:/Anaconda/Anaconda 3.7/Lib/site-packages/jieba/dict2.txt")
text2 = "广师大是我的母校"
ci_2 = jieba.posseg.cut(text2)
for item in ci_2:
    print(item.word + "---" + item.flag)