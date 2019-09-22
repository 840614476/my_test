#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:TBH time:2019/9/19

##############使用人工神经网络实现手写体数字识别################

import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense,Activation
from os import listdir
from test046 import data_to_array,sep_label,traindata


'''数据读取和处理'''
train_data, train_labels = traindata()

x_F = pd.DataFrame(train_data)
y_F = pd.DataFrame(train_labels)
x = x_F.as_matrix().astype(int)
y = y_F.as_matrix().astype(int)


'''使用人工神经网络模型'''

model = Sequential()                               #建立BP神经网络模型对象

#输入层
model.add(Dense(10, input_dim=len(x[0])))         #输入层，10层   input_dim=（有多少特征）
model.add(Activation("relu"))                      #激活函数

#输出层
model.add(Dense(1, input_dim=1))                   #输出层1层
model.add(Activation("sigmoid"))                  #sigmoid 二元分类

#模型的编译
model.compile(loss="mean_squared_error", optimizer="adam")     #loss:损失函数（损失方式）  optimizer:求解方法

#训练
model.fit(x, y, nb_epoch=10000, batch_size=100)        #nb_epoch：训练次数   batch_size：批量大小

#预测分类
result = model.predict_classes(x).reshape(len(x))
print(result)

print("\n")

#检验准确率
error_num = 0
for i in range(0, len(x)):
    if result[i] != y[i]:
        error_num += 1

print(1 - (error_num / len(x)))

print("\n")

