#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:TBH time:2019/9/10

import jieba
import jieba.analyse
import jieba.posseg

#分析盗墓笔记词频
#
# data = open("E:/Pycharm 文件/数据挖掘/文本分析/盗墓.txt").read()

data = open("E:/Pycharm 文件/数据挖掘/文本分析/盗墓笔记.TXT", 'rb').read().decode('utf-8') #'rb'  二进制读取
tag = jieba.analyse.extract_tags(data, 20)
print(tag)