#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : tangbo
# @Site    : 
# @File    : 
# @Software:
# data = []
# #打开并关闭文件
# with open("access.txt","r") as f:
#         #读取数据
#         ip = f.readlines()
#         #print(ip)
#         #循环数据，区0号位置，即我需要的列
#         for i in ip:
#                 #print i
#                 user = i.split(' ')[0]
#                 #写入data列表
#                 data.append(user)
# #列表去重
# a = list(set(data))
# h = {}
# #循环重复列表，和元列表做对比，新数据加入到字典
# for i in a:
#     b = data.count(i)
#     h[i]=b
# #print(h)
# #对字典排序
# re = sorted(h.items(),key=lambda item:item[1],reverse=1)
# #print(re)
# print(list(re))
# a=[]
# for i in re:
#     a.append(list(i))
# print(a)
#
#
# #循环取到我需要的前10位
# # for obj in re[0:10]:
# #     print ('%s %s' % (obj[0],obj[1]))

def nginx():
    data = []
    with open("access.txt","r") as f:
            ip = f.readlines()
            for i in ip:
                    #print i
                    user = i.split(' ')[0]
                    #写入data列表
                    data.append(user)
    a = list(set(data))
    h = {}
    for i in a:
        b = data.count(i)
        h[i]=b

    re = sorted(h.items(),key=lambda item:item[1],reverse=1)
    #print(list(re))
    a=[]
    for i in re:
        a.append(list(i))
    return a
res = nginx()
print(res)














