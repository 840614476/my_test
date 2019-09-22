#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:TBH time:2019/8/28

import pandas as pd

#创建一维数组
a = pd.Series([8,2,3,6])
# print(a)
# print("\n")

b = pd.Series([8,2,3,6], index = ["a","b","c","d"])    #index  索引
# print(b)
# print("\n")

#创建二维数组
c = pd.DataFrame([[5,53,35,0],[85,21,3,7],[5,5,61,3],[5,15,3,8]])
# print(c)
# print("\n")

d = pd.DataFrame([[5,53,35,0],[85,21,3,7],[5,5,61,3],[5,15,3,8]], columns = ["a","b","c","d"])    #columns  索引
# print(d)
# print("\n")

#输出d数组的具体信息
data = d.describe()
print(data)