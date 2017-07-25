#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : tangbo
# @Site    : 
# @File    : 
# @Software:
#求这个list的最大的两个值
list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45,5000]
#方法一、
list.sort()
print(list[-2:])
#方法二、
max = 0
max1 = 0
#max_list = []
for i in list:
    if max<i:
        max=i
    for x in list:
        if max1<x and x<max:
            max1=x
print(max,max1)


