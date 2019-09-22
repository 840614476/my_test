#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:TBH time:2019/9/17

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pymysql
from sklearn.cluster import KMeans

#通过程序实现TB商品的聚类

conn = pymysql.connect(host = "127.0.0.1", user = "root", passwd = "root", db = "test")
sql = "select price,comment from taob limit 100"

data_sql = pd.read_sql(sql, conn)
x = data_sql.iloc[:, :].as_matrix()
kms_good = KMeans(n_clusters=3)
y= kms_good.fit_predict(x)

for i in range(0, len(y)):
    x1 = data_sql.iloc[i:i+1, 0:1].as_matrix()
    y1 = data_sql.iloc[i:i+1, 1:2].as_matrix()
    if y[i] == 0:
        plt.plot(x1, y1, "*r")
    if y[i] == 1:
        plt.plot(x1, y1, "sy")
    if y[i] == 2:
        plt.plot(x1, y1, "pk")

plt.show()