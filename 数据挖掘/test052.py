#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:TBH time:2019/9/18

from test046 import data_to_array,sep_label,traindata
from test047 import Bayes
from os import listdir         #读取当前文件夹的所有文件

Bys = Bayes()           #建立一个贝叶斯对象

'''
训练数据
'''
train_data, train_labels = traindata()
Bys.train(train_data, train_labels)

'''
识别多个手写体数字
'''
test_all_data = listdir("F:/学习文件/源码/源码/第7周/testandtraindata/testdata")
num = len(test_all_data)
all_label = [0,1,2,3,4,5,6,7,8,9]

for i in range(0, num):
    this_file = test_all_data[i]
    this_label = sep_label(this_file)

    this_test_data = data_to_array("F:/学习文件/源码/源码/第7周/testandtraindata/testdata/" + this_file)
    this_t_d_label = Bys.bayes_test(this_test_data, all_label)

    print("该数字：" + str(this_label) + ",识别数字为：" + str(this_t_d_label))





