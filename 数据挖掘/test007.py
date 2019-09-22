#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:TBH time:2019/8/9
import urllib.request
import re

url = "http://www.bilibili.com/"
headers = {"User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}

opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)
data = urllib.request.urlopen(url).read().decode("utf-8")

form = '<li><a href="(.*?)"><span>'
all_url = re.compile(form).findall(data)

# for i in range(0,len(all_url)):
#     try:
#         print("第" + str(i) + "次爬取")
#         this_url = all_url[i]
#         file = open("E:/Pycharm 文件/数据挖掘/爬取网站/b站" + str(i) + ".html", "wb")
#         urllib.request.urlretrieve(this_url, file)
#         print("---成功---")
#     except urllib.error.URLError as e:
#         if hasattr(e, "code"):
#             print(e.code)
#         if hasattr(e, "reason"):
#             print(e.reason)
for i in range(0,len(all_url)):
    file = "E:/Pycharm 文件/数据挖掘/爬取网站/b站/" + str(i) + ".html"
    urllib.request.urlretrieve(all_url[i], filename=file)
    print("第" + str(i) + "次爬取")