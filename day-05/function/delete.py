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
def delete():
    record = "select * from record;"
    cur.execute(record)
    record = cur.fetchall()
    da = record
    user_id = int(request.args.get('id',1000))
    print(user_id)
    sql = "delete from record where id = %s;" %(user_id)
    print(sql)
    cur.execute(sql)
    res = cur.fetchone()
    return da