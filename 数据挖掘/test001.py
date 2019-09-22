#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:TBH time:2019/8/8

import urllib.request

for i in range(0,30):
    try:
        file = urllib.request.urlopen("http://www.baidu.com",timeout = 1)
        data = file.read()
        print(len(data))
    except Exception as e:
        print("出现异常：" + str(e))