#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:TBH time:2019/8/8
import urllib.error
import urllib.request

try:
    urllib.request.urlopen("http://www.bilibili.com/")
except urllib.error.URLError as e:
    if hasattr(e, "code"):
        print(e.code)
    if hasattr(e, "reason"):
        print(e.reason)
