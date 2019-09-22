#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:TBH time:2019/9/20

from apriori import *
import pandas as pd

'''
计算学员购买课程的关联性
'''

#加载数据
file = "F:/学习文件/源码/源码/lesson_buy.xls"
data_frame = pd.read_excel(file, header=None)

#转化数据
change = lambda x:pd.Series(1, index=x[pd.notnull(x)])      #转换规则：将有数据的项变为1
m = map(change, data_frame.as_matrix())                     #根据提供的函数对指定序列做映射
data = pd.DataFrame(list(m)).fillna(0)                      #转换为数据框，将空的项转为0

#临界支持度、置信度设置
support = 0.1
confidence = 0.3

#使用 apriori 算法计算关联结果
result = generateRules(data, support)
print(result)




















