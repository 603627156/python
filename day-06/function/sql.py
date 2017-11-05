#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : tangbo
# @Site    : 
# @File    : 
# @Software:
from flask import Flask,render_template,request
import pymysql
conn = pymysql.connect(host='192.168.6.250', port=3306, user='root', passwd='111111',db='flask',charset='utf8mb4')
conn.autocommit(True)
cur = conn.cursor()

#查
def list(table,field):
    query = "select * from %s" %(table)
    cur.execute(query)
    res = cur.fetchall()
    #print(res)
    if not res:
        resault ={'code':1,'errmsg':'data is null'}
        return  resault
    else:
        user = []
        for row in res:
            dictionary = dict(zip(field, row))
            user.append(dictionary)
        return user
#list('user',['id','username','email','phone','passwd'])

#删除
def delete(user_id):
    delete = "delete from record where id = %s;" %(user_id)
    cur.execute(delete)

#添加
def insert(table,field,data):
    add = "insert into %s (%s) VALUES (%s)" %(table,','.join(field),','.join(['"%s"'  %data[x] for x in field]))
    print(add)
    cur.execute(add)
    # if rest:
    #     rest ={'code':1,'errmsg':'insert is ok'}
    # else:
    #     rest ={'code':1,'errmsg':'insert is fail'}
    # return rest
#更新
def update(table,data,sid):
    update = "update %s set %s where id=%s"  %(table,','.join(["%s='%s'" %(k,data[k]) for k in data]),sid)
    cur.execute(update)