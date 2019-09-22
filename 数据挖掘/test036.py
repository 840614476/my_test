#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:TBH time:2019/9/9

#主成分分析
from sklearn.decomposition import PCA
import pymysql
import pandas as pd
import numpy as np

cont = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='test')
sql = "select hits,comment from myhexun"
data = pd.read_sql(sql, cont)
c_h = data["comment"] / data["hits"]
data["评点比"] = c_h

'''主成分分析进行'''
pca_1 = PCA()          #调用方法
pca_1.fit(data)        #加载数据