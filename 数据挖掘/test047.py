#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:TBH time:2019/9/13

#贝叶斯算法

import numpy as np

class Bayes:

    '''初始化'''
    def __init__(self):
        self.length = -1                #初始化长度
        self.labels_count = dict()      #初始化标签
        self.vector_count = dict()      #初始化向量（测试数据）

    '''用于训练的方法'''
    def train(self, data_Set:list, labels:list):
        if (len(data_Set) != len(labels)):
            raise ValueError("输入的测试数组跟类别数组长度不一致")
        self.length = len(data_Set[0])       #测试数据特征值的长度
        labels_num = len(labels)            #类别的所有数量
        no_repeat_labels = len(labels)      #某一类别的数量

        for item in range(no_repeat_labels):
            this_label = item
            self.labels_count[this_label] = labels.count(this_label) / labels_num        #求某一类别占所有类别数量的比例

        for vector,label in zip(data_Set,labels):
            if label not in self.vector_count:              #判断某一类别是否在vector_count
                self.vector_count[label] = []
            self.vector_count[label].append(vector)         #把某一类别的特征值添加到vector_count里

        print("训练结束")
        return self

    def bayes_test(self, testdata, labels_Set):
        if self.length == -1:
            raise ValueError("该数据没有进行训练，请先进行训练")

        test_label_Dict = dict()

        for this_test_label in labels_Set:                                  #依次遍历各个类别
            p = 1
            all_test_label = self.labels_count[this_test_label]
            all_test_vector = self.vector_count[this_test_label]
            vector_num = len(all_test_vector)
            all_test_vector = np.array(all_test_vector).T                   #转置

            for item in range(0, len(testdata)):
                vector = list(all_test_vector[item])                            #当前的测试数据
                p = p*vector.count(testdata[item]) / vector_num                 #求当前的测试数据占所有测试数据的比例

            test_label_Dict[this_test_label] = p * all_test_label               #得到testdata占某一类别的比例

        this_label = sorted(test_label_Dict, key = lambda x:test_label_Dict[x], reverse = True)[0]
        return this_label




