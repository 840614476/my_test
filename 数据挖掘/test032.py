#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:TBH time:2019/9/9

import numpy as np

a = np.array([[1,2,3],[4,5,6]])
b = np.array([[7,8,9],[89,576,85]])

#数据集成
c = np.concatenate((a,b))
print(c)