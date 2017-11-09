#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/20 9:16
# @Author  : tangbo
# @Site    :
# @File    : 04-上午.py
# @Software: PyCharm

#导入flask需要的模块
from flask import Flask,render_template,request
from function.ng import *
from function.delete import *
res =nginx()

##########################Mysql###########################
import pymysql
conn = pymysql.connect(host='192.168.6.250', port=3306, user='root', passwd='111111',db='flask',charset='utf8mb4')
conn.autocommit(True)
cur = conn.cursor()
username = "select username,passwd from user;"
cur.execute(username)
data = cur.fetchall()   #取值后是元祖 需要转换成字典
##########################Mysql###########################
# record = "select * from record;"
# cur.execute(record)
# record = cur.fetchall()
#########################################################

##################把数据库数据搞成字典###############################
ddyy={}
for i in data:
    ddyy[i[0]]=i[1]
#print(dict)
##################################################
#创建一个实例名叫  app
app = Flask(__name__)
#访问/ 调函数登录函数
@app.route('/')
def login():
    users =[{'name':'tangbo','age':18,'role':'admin'},{'name':'reboot','age':2,'role':'fin'},{'name':'wenwen','age':33,'role':'master'}]
    return render_template('login.html',users=users)
                        #前端数据返回到后端  后端数据返回前端

@app.route('/root/',methods=['GET','POST'])
def index():
     if request.method == "POST":
        for user,pwd in ddyy.items():
            if user == request.form.get('username') and pwd == request.form.get('password'):
                    return render_template('index.html')
        else:
                errors="用户名密码错误，请重新输入！"
                return render_template('login.html',error=errors)

@app.route('/two/')
def b():
    data = res[0:10]
    return render_template('01/b.html', contan=data)

@app.route('/management/',methods=['GET','POST'])
def management():
        delete()
        da =delete()
        if request.method == "POST":
            user_name = request.form.get('user_name')
            print(user_name)
            name = request.form.get('name')
            print(name)
            shuzinumber=request.form.get('shuzi_number')
            print(shuzinumber)
            department=request.form.get('department')
            print(department)
            port= request.form.get('port')
            print(port)

            sql2 = "insert into record(id,name,shuzi_number,Department,number) values('%d','%s','%d','%s','%s');" %(user_name,name,shuzinumber,department,port)
            cur.execute(sql2)
        return render_template('01/management.html',record=da)

@app.route('/test/',methods=['GET','POST'])
def test():
    record = "select * from record;"
    cur.execute(record)
    record = cur.fetchall()
    data1 = record
    res1 = []
    test =[]
    for i in data1:
        res1.append(list(i))

    y = ['id','name','email','tt','ttt']
    for x in res1:
        dictionary = dict(zip(y, x))
        test.append(dictionary)
    print(test)
    return render_template('01/01.html',resault=test)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug = True)
