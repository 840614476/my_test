#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:TBH time:2019/8/28

import pandas as pd

#导入CSV文件
a = pd.read_csv("E:/Pycharm 文件/导入数据/hexun.csv", encoding='gbk')
# data = a.describe()
# print(data)

#按照某一个表头排序
data = a.sort_values(by = "21")
print(data)