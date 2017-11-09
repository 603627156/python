#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/20 9:16
# @Author  : tangbo
# @Site    :
# @File    : 04-上午.py
# @Software: PyCharm

#导入flask需要的模块
from flask import Flask,render_template,request
import function
from function.sql import *

#创建一个实例名叫  app
app = Flask(__name__)
#访问/ 调函数登录函数
@app.route('/',methods=['GET','POST'])
#登录页面
def login():
    return render_template('login.html')
                        #前端数据返回到后端  后端数据返回前端
#超级管理员页面
@app.route('/index/',methods=['GET','POST'])
def index():
     if request.method == "POST":
         #前端传入
         user1 = dict((k,v[0]) for k,v in dict(request.form).items())
         #print(user1)
         #数据库取出来
         user2 = list('user',['id','username','email','phone','passwd'])
         for i in user2:
                if i.get('username') == user1.get('username') and i.get('passwd') == user1.get('password'):
                         return render_template('index.html')
                else:
                    errors="用户名密码错误，请重新输入！"
         return render_template('login.html',error=errors)

#录音管理页面
@app.route('/management/',methods=['GET','POST'])
def management():
        #查询
        record = list('record',['id','name','shuzinumber','department','number',])
        if request.method == "POST":
            data = dict((k,v[0]) for k,v in dict(request.form).items())      #获取前端数据
            #print(data)
            #添加
            if data.get('user_id[]'):
                data1 = dict(request.form)
                res = data1.get('user_id[]')  #转换成字典格式
                for user_id in res:
                    delete(user_id)    #删除用户id

            #删除
            elif data.get('add') == '提交':
                field =['number','shuzinumber','name','department']
                insert('record',field,data)
        return render_template('01/management.html',record=record)

@app.route('/update/',methods=['GET','POST'])
def update():
    record = list('record',['id','name','shuzinumber','department','number',])
    if request.method == "POST":
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        #print(data)
        uid = data.get('update_id[]')
        global uid
        del data['update_id[]']
        sid = data.get('uid')
        del data['uid']
        update('record',data,sid)
        cur.execute(update)
        # conditions = ["%s='%s'" %(k,data[k]) for k in data]
        # update = "update record set %s where id=%s"  %(','.join(conditions),sid)
        # print(update)
        # print(conditions)
    return render_template('01/update.html',uid=uid)
# @app.route('/two/')
# def b():
#     data = res[0:10]
#     return render_template('01/b.html', contan=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug = True)
