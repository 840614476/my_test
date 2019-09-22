#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:TBH time:2019/9/16

import pandas as pd
from sklearn.linear_model import LogisticRegression as LR               #导入逻辑回归模型
from sklearn.linear_model import RandomizedLogisticRegression as RLR

file = "F:/学习文件/源码/源码/luqu.csv"
data = pd.read_csv(file)

x = data.iloc[:, 1:4].as_matrix()         #iloc提取指定行、指定列数据,as_matrix转换为数组
y = data.iloc[:, 0:1].as_matrix()

