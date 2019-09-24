#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:TBH time:2019/9/17

'''
决策树
'''

import pandas as pd

file = "F:/学习文件/源码/源码/lesson.csv"
data = pd.read_csv(file, encoding='gbk')

x = data.iloc[:, 1:5].as_matrix()           #iloc提取指定行、指定列数据,as_matrix转换为数组
y = data.iloc[:, 5].as_matrix()             #[:, 1:5]  逗号左边指取所有行，右边指取1到4列

for i in range(0, len(x)):                  #遍历x元素
    for j in range(0, len(x[i])):
        this_data = x[i][j]
        if this_data == "是" or this_data == "多" or this_data == "高":
            x[i][j] = 1
        else:
            x[i][j] = -1

for i in range(0, len(y)):                  #遍历y元素
    this_data = y[i]
    if this_data == "高":
        y[i] = 1
    else:
        y[i] = -1


#不能直接dtc训练
#先转换好格式：将x，y转换为数据框，然后再转换为数组并指定格式

x_F = pd.DataFrame(x)
y_F = pd.DataFrame(y)
x1 = x_F.as_matrix().astype(int)
y1 = y_F.as_matrix().astype(int)


'''
建立决策树
'''
from sklearn.tree import DecisionTreeClassifier as DTC

dtc = DTC(criterion="entropy")          #设置为信息熵模式
dtc.fit(x1, y1)

'''
可视化决策树
'''
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO

with open("E:/Pycharm 文件/数据挖掘/决策树/dtc.dot","w") as file:
    export_graphviz(dtc, feature_names = ["shizhan","keshi","cuxiao","ziliao"], out_file = file)

'''
直接预测结果
'''
import numpy as np

test = np.array([[1,1,1,1],[-1,1,-1,1],[1,-1,-1,1]])
result = dtc.predict(test)                         #predict 预测结果
print(result)



















