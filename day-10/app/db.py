#!/usr/bin/env python
#-*- coding:utf-8 -*-

import MySQLdb as mysql
import config
import traceback
from utils import WriteLog

conn = mysql.connect(
    host = config.host,
    user = config.user,
    passwd = config.passwd,
    db = config.db,
    charset = config.charset
    )

conn.autocommit(True)
cur = conn.cursor()

# 插入数据
def insert(table,field,data):
    sql = "insert into %s (%s) values (%s)" % (table,','.join(field),','.join(['"%s"' % data[x] for x in field]))
    try:
        res = cur.execute(sql)
        WriteLog("sql").info("insert:%s" % sql)
        result = {'code':0,'msg':'insert ok'}
    except:
        result = {'code':1,'msg':'insert fail'}
        WriteLog("sql").error("Execute %s error : %s" % (sql,traceback.format_exc()))
    return result

# 查询数据
def getone(table,field,data):
    if data.has_key('name'):
        sql = 'select %s from %s where name = "%s"' % (','.join(field),table,data['name'])
    else:
        sql = 'select %s from %s where id = "%s"' % (','.join(field),table,data['id'])
    try:
        cur.execute(sql)
        res = cur.fetchone()
        WriteLog("sql").info("getone:%s" % sql)
        user = {k:res[i] for i,k in enumerate(field)}
        result = {'code':0,'msg':user}
    except:
        result = {'code':1,'msg':'data is null'}
        WriteLog("sql").error("Execute %s error : %s" % (sql,traceback.format_exc()))
    return result

# 查询全部
def listall(table,field):
    sql = "select %s from %s" % (','.join(field),table)
    try:
        cur.execute(sql)
        res = cur.fetchall()
        WriteLog("sql").info("listall:%s" % sql)
        user = [{k:row[i] for i,k in enumerate(field)} for row in res]
        result = {'code':0,'msg':user}
    except:
        result = {'code':1,'msg':'data is null'}
        WriteLog("sql").error("Execute %s error : %s" % (sql,traceback.format_exc()))
    return result

# 更新数据
def updateuser(table,field,data):
    conditions = ["%s='%s'" % (k,data[k]) for k in field]
    print conditions
    sql = "update %s set %s where id = %s" % (table,','.join(conditions),data['id'])
    print sql
    try:
        res = cur.execute(sql)
        WriteLog("sql").info("updateuser:%s" % sql)
        result = {'code':0,'msg':'update success'}
    except:
        result = {'code':1,'msg':'update false'}
        WriteLog("sql").error("Execute %s error : %s" % (sql,traceback.format_exc()))
    return result

# 删除数据
def delete(table,uid):
    sql = "delete from %s where id = %s" % (table,uid)
    try:
        res = cur.execute(sql)
        WriteLog("sql").info("delete:%s" % sql)
        result = {'code':0,'msg':'delete success'}
    except:
        result = {'code':1,'msg':'delete false'}
        WriteLog("sql").error("Execute %s error : %s" % (sql,traceback.format_exc()))
    return result



