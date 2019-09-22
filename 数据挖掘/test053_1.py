#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:TBH time:2019/9/19

'''
BP人工神经网络的实现步骤
#1、读取数据
#2、keras.models Sequretial    /     keras.layers.core Dense Activation
#3、Sequretial 建立BP神经网络模型
#4、Dense 建立层
#5、Activation 激活函数
#6、compile 模型编译
#7、fit 训练（学习）
#8、验证（测试，分类预测）
'''


##############使用人工神经网络预测课程销量################

import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense,Activation


'''数据读取与整理'''

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
            x[i][j] = 0

for i in range(0, len(y)):                  #遍历y元素
    this_data = y[i]
    if this_data == "高":
        y[i] = 1
    else:
        y[i] = 0


#不能直接dtc训练
#先转换好格式：将x，y转换为数据框，然后再转换为数组并指定格式

x_F = pd.DataFrame(x)
y_F = pd.DataFrame(y)
x1 = x_F.as_matrix().astype(int)
y1 = y_F.as_matrix().astype(int)

'''使用人工神经网络模型'''

model = Sequential()                               #建立BP神经网络模型对象

#输入层
model.add(Dense(10, input_dim=len(x1[0])))         #输入层，10层   input_dim=（有多少特征）
model.add(Activation("relu"))                      #激活函数

#输出层
model.add(Dense(1, input_dim=1))                   #输出层1层
model.add(Activation("sigmoid"))                  #sigmoid 二元分类

#模型的编译
model.compile(loss="binary_crossentropy", optimizer="adam")     #loss:损失函数（损失方式）  optimizer:求解方法    class_mode:模式

#训练
model.fit(x1, y1, nb_epoch=1000, batch_size=100)        #nb_epoch：训练次数   batch_size：批量大小

#预测分类
result = model.predict_classes(x1).reshape(len(x1))
print(result)

print("\n")

#检验准确率
error_num = 0
for i in range(0, len(x1)):
    if result[i] != y[i]:
        error_num += 1

print(1 - (error_num / len(x1)))

print("\n")

#自定义一个测试，预测分类
test = np.array([[1,1,1,1],[-1,1,-1,1],[1,-1,-1,1]])
result_t = model.predict_classes(test).reshape(len(test))
print(result_t)














































