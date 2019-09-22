#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:TBH time:2019/9/12

'''
KNN算法
'''

from numpy import *
import operator

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

