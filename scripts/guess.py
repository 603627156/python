#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/2/5 19:47
# @Author  : tangbo
# @Site    : 
# @File    : 01-for.py
# @Software: PyChar

lucky_num = 30
input_num = -1
for i in range(3):
    input_num = int(input("Input the guess num:"))
    if input_num > lucky_num:
        print("The real number is smaller.")
    elif input_num < lucky_num:
        print("The real num is bigger..")
    else:
        print("Bingo!")
        break
else:
    print("Too many retrys!")
