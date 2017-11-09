#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : tangbo
# @Site    : 
# @File    : 
# @Software:
import pymysql
from utils.anxinlog import *
from utils.config import *
conn = pymysql.connect(host=host, port=3306, user=user, passwd=passwd,db=db,charset=charset)
conn.autocommit(True)
cur = conn.cursor()
#查询单条
def getone(table,field,data):
	if data.get('user_name'):
		sql = "select * from %s where user_name='%s'" %(table,data['user_name'])
	else:
		sql = "select * from %s where user_id='%s'" %(table,data.get('user_id'))
	#print (sql)
	writelog('getone: %s'%sql)
	cur.execute(sql)
	res = cur.fetchone()
	#print (res)
	if res:
		user = {k:res[i] for i,k in enumerate(field)}
		#print (user)
		result = {'code':0,'msg':user}
	else:
		result = {'code':1,'msg':'用户名密码错误'}
	return result

#列出所有
def list(table,field):
	sql = "select * from %s" %table
	cur.execute(sql)
	writelog('getall: %s'%sql)
	res = cur.fetchall()
	if res:
		user = [{k:row[i] for i,k in enumerate(field)} for row in res]
		result = {'code':0,'msg':user}
	else:
		result = {'code':1,'msg':'data is null'}
	return result
#插入数据
def insert(table,field,data):
	sql = "insert into %s (%s) values (%s)" %(table,','.join(field),','.join(['"%s"' %data[x] for x in field]))
	writelog('insert: %s'%sql)
	res = cur.execute(sql)
	if res:
		result = {'code':0,'msg':'insert ok'}
	else:
		result = {'code':1,'msg':'insert fail'}

	return result

#删除数据
def delete(table,user_id):
    delete = "delete from %s where user_id = %s;" %(table,user_id)
    writelog('getone: %s'%delete)
    res = cur.execute(delete)
    if res:
        result = {'code':0,'msg':'delete ok'}
    else:
        result = {'code':1,'msg':'delete fail'}
    return result

def update(table,field,data):
    conditions = ["%s='%s'" % (k,data[k]) for k in data]
    #print (conditions)
    sql = "update %s set %s where user_id=%s" %(table,','.join(conditions),data['user_id'])
    writelog('getone: %s'%sql)
    #print (sql)
    res = cur.execute(sql)
    if res :
        result = {'code':0,'msg':'update ok'}
    else:
        result = {'code':1,'errmsg':'update fail'}
    return result

def mem():
	mem = "select localhost_mem from localhost"
	writelog('getone: %s'%mem)
	meme = cur.execute(mem)
	meme1 = cur.fetchall()
	return meme1

