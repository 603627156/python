#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : tangbo
# @Site    : 
# @File    : 
# @Software:
#定义空列表获取读入数据
data = []
#打开并关闭文件
with open('/Data/reboot/two/access.txt1','a+') as f:
	#读取数据
	ip = f.readlines()
	#print(ip)
	#循环数据，区0号位置，即我需要的列
	for i in ip:
		#print i
		user = i.split(' ')[0]
		#写入data列表
		data.append(user)
#列表去重
a = list(set(data))
h = {}
#循环重复列表，和元列表做对比，新数据加入到字典
for i in a:
    b = data.count(i)
    h[i]=b
#print(h)
#对字典排序
re = sorted(h.items(),key=lambda item:item[1],reverse=1)
#print(re)
#循环取到我需要的前10位
for obj in re[0:10]:
    print obj[0],obj[1]
