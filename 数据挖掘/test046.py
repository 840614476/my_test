#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:TBH time:2019/9/12

from numpy import *
import operator
import os
from os import listdir         #读取当前文件夹的所有文件

#KNN算法
def knn(k, testdata, traindata, labels):
    train_data_size = traindata.shape[0]                   #计算训练集（样本）的行数
    test_data = tile(testdata, (train_data_size,1))        #扩展测试集的行数，与训练集相同

    #欧式距离(类似勾股定理)
    D_value = test_data - traindata                        #计算测试集与训练集的差值（向量 - 向量）
    D_value_sum = (D_value**2).sum(axis=1)                 #计算差值平方的和
    distance = D_value_sum**0.5                            #然后开方得出距离

    sort_distance = distance.argsort()                     #将距离进行排序

    #接下来选择距离最小的k个点
    count = {}                                             #创建一个空字典
    for i in range(0, k):
        votes = labels[sort_distance[i]]                   #判断k是哪个类别
        count[votes] = count.get(votes,0) + 1              #统计某一类别出现的次数
    sort_count = sorted(count.items(), key=operator.itemgetter(1), reverse=True)              #将次数进行排序，降序
    return sort_count[0][0]                                #返回第一个结果

#加载数据
#将各个文件存储为一个数组
def data_to_array(f_name):
    array = []
    file = open(f_name)
    for i in range(0, 32):
        this_line  = file.readline()
        for j in range(0, 32):
            array.append(int(this_line[j]))
    return array

#取文件前缀名
def sep_label(f_name):
    this_file = f_name.split(".")[0]
    label = int(this_file.split("_")[0])
    return label

    # this_file = re.findall('(\d+)_', f_name)
    # label = int(this_file)
    # return label

#建立训练数据
def traindata():
    labels = []             #建立一个类别的列表
    train_file = listdir("F:/学习文件/源码/源码/第7周/testandtraindata/traindata")        #listdir：读取该文件夹下的所有文件
    num = len(train_file)       #计算文件的数量
    # 长度1024列，每一行存储一个文件
    # 用一个数组存储所有训练集的数据，行：文件总数（num），列：1024
    train_array = zeros((num, 1024))        #zeros:生成num行1024列的数组
    for i in range(0, num):
        this_train = train_file[i]          #在当前文件
        this_label = sep_label(this_train)   #识别当前文件的类别
        labels.append(this_label)           #增加到类别表中
        train_array[i,:] = data_to_array("F:/学习文件/源码/源码/第7周/testandtraindata/traindata/" + this_train)    #将所有训练集数据加载到train_array数组中
    return train_array, labels

#调用KNN算法测试“测试数据”，检验是否准确识别
def testdata():
    train_data, label = traindata()
    test_file = listdir("F:/学习文件/源码/源码/第7周/testandtraindata/testdata")
    num = len(test_file)
    for i in range(0, num):
        this_test = test_file[i]
        test_data = data_to_array("F:/学习文件/源码/源码/第7周/testandtraindata/testdata/" + this_test)          #将所有测试数据加载
        knn_result = knn(3, test_data, train_data, label)
        print(knn_result)



