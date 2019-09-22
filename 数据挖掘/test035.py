#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:TBH time:2019/9/9

#属性构造
import pymysql
import pandas as pd
import numpy as np

cont = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='test')
sql = "select * from myhexun"
data = pd.read_sql(sql, cont)

c_h = data["comment"] / data["hits"]
data["评点比"] = c_h
file = "./hexun.xls"
data.to_excel(file, index = False)