#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:TBH time:2019/9/9

import pymysql
import pandas as pd
import numpy as np

#连接taob数据库
con = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='test')
sql = 'select price,comment from taob'
data = pd.read_sql(sql, con)

# 连续型数据离散化
# 等宽离散化
a = data["price"].copy().T.values
# k = 3
# b = pd.cut(a, k, labels=["便宜","适中","贵"])
# print(b)
k = [0,50,100,300,1000,a.max()]
b = pd.cut(a, k, labels=["非常便宜","便宜","适中","很贵","非常的贵"])
print(b)