#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : tangbo
# @Site    : 
# @File    : 
# @Software:

import pymysql
for i in range(3):
    USER = input("请输入您的用户名：")
    PASSWD = input("请输入您的密码：")
    conn = pymysql.connect(host='192.168.6.250', port=3306, user='root', passwd='111111',db='user')
    cur = conn.cursor()
    sql = "select ax_user.login,ax_password.passwd from ax_user inner join ax_password where ax_user.id=ax_password.id and ax_user.login='%s' and ax_password.passwd='%s';"%(USER,PASSWD)
    #print(sql)
    cur.execute(sql)
    name = cur.fetchall()
    print(name)
    if name == ():
        print('*'*50,"用户名密码错误，请重试",'*'*50)

    else:
        user_pass = name[0]
        input_user = user_pass[0]
        input_passwd = user_pass[1]
        if USER == input_user and PASSWD == input_passwd:
            print('*'*50,'欢迎登陆系统','*'*50)
            break
