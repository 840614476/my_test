#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:TBH time:2019/9/17

'''
kmeans算法
'''


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pymysql
from sklearn.cluster import KMeans

#通过程序实现录取学生的聚类
file = "F:/学习文件/源码/源码/luqu.csv"
data = pd.read_csv(file)
x = data.iloc[:, 1:4].as_matrix()
kms = KMeans(n_clusters = 4)
y = kms.fit_predict(x)
print(y)
























