#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/29 11:45
# @Author  : tangbo
# @Site    : 
# @File    : 003-简单爬虫编写.py
# @Software: PyCharm

import urllib.request
import re
index = urllib.request.urlopen("http://edu.51cto.com").read().decode("utf-8")
#print(index)
data = '<a href="#nav\d.*?">(\S*?)</a>'
res = re.compile(data).findall(index)
print(res)

