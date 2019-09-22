#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:TBH time:2019/8/8

import urllib.request

keywd = "广东技术师范大学"
keywd = urllib.request.quote(keywd)
url = "http://www.baidu.com/s?wd=" + keywd
req = urllib.request.Request(url)
data = urllib.request.urlopen(req).read()
file = open("E:/Pycharm 文件/数据挖掘/2.html","wb")
file.write(data)
file.close()