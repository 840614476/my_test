#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:TBH time:2019/8/12
import urllib.request

def use_proxy(url, proxy_IP):
    proxy = urllib.request.ProxyHandler({"http": proxy_IP})
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode("utf-8")
    return data

proxy_IP = "219.131.242.37:9797"
url = "http://www.baidu.com/"
data = use_proxy(url, proxy_IP)
print(len(data))
