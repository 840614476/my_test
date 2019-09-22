#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:TBH time:2019/8/9
import urllib.request
import urllib.error
import re

url = urllib.request.urlopen("http://news.sina.com.cn/").read()
data = url.decode("utf-8")
form = 'href="(http://slide.news.sina.com.cn/.*?)"'
all_url = re.compile(form).findall(data)

for i in range(0,len(all_url)):
    try:
        print("第" + str(i) + "次爬取")
        this_url = all_url[i]
        file = "E:/Pycharm 文件/数据挖掘/爬取网站/sina_news/" + str(i) + ".html"
        urllib.request.urlretrieve(this_url,file)
        print("---成功---")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
