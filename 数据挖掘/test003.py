#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:TBH time:2019/8/8
import urllib.request
import urllib.parse

url = "https://www.iqianyue.com/mypost/"
mydata = urllib.parse.urlencode({
    "name": "test",
    "pass": "123456"
}).encode("utf-8")
req = urllib.request.Request(url, mydata)
data = urllib.request.urlopen(req).read()

file = open("E:/Pycharm 文件/数据挖掘/3.html", "wb")
file.write(data)
file.close()
