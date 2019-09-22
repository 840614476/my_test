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

#离差标准化
Li_cha = (data - data.min()) / (data.max() - data.min())
# print(Li_cha)

#标准差标准化
biao_z = (data - data.mean()) / data.std()
# print(biao_z)

#小数定标规范化
k = np.ceil(np.log10(data.abs().max()))
Ding_biao = data / 10**k
print(Ding_biao)
'''
ceil : 进一取整    ceil（3.1) = 4
(np.log10(data.abs().max()))   取数据绝对值的最大值
(np.log10(|-3000|)
'''