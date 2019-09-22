#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:TBH time:2019/9/6

import pymysql
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#解决可视化中文乱码
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

#导入数据
#连接数据库
conn = pymysql.connect(host="127.0.0.1",user="root",passwd="root",db="test")
sql = "select * from taob"
data = pd.read_sql(sql, conn)
# print(data.describe())

#数据清洗
#将价格为0的设置空值
x = 0
data["price"][(data["price"] == 0)] = None
for i in data.columns:       #columns 获取所有表头然后遍历
    for j in range(len(data)):
        if (data[i].isnull())[j]:       #判断data[i]中的None
            data[i][j] = "36"
            x = x + 1

print(x)

#异常值处理
#自定义：评论数异常>200000，价格异常>2300

line = len(data.values)
# col = len(data.values[0])
da = data.values
for i in range(0, line):
    # for j in range(0, col):
        if da[i][2] > 2300:
            da[i][2] = 36
        if da[i][3] > 200000:
            da[i][3] = 58


# #画散点图
# data2 = data.T
# #价格
# price = data2.values[2]
# #评论
# comment = data2.values[3]
da2 = da.T
price = da2[2]
comment = da2[3]
plt.xlabel("价格")
plt.ylabel("评论")
plt.scatter(price, comment)
plt.show()