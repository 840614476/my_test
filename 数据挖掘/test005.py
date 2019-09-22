#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:TBH time:2019/8/9
import urllib.request


url = "http://www.bilibili.com/"
headers = {"User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
opener = urllib.request.build_opener()
opener.addheaders = [headers]
data = opener.open(url).read()
file = open("E:/Pycharm 文件/数据挖掘/爬取网站/4.html", "wb")
file.write(data)
file.close()
