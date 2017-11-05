#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask,request,render_template,redirect,session
from db import insert,getone,listall,updateuser,delete
from utils import WriteLog
from app import app
import json

field = ['id','name','name_cn','password','email','mobile','role','status']

# 用户列表
@app.route('/userlist/')
def userlist():
    if not session:
        return redirect('/login/')
    if session['role'] == 'admin':
        result = listall('users',field) 
        if result['code'] == 0:
            result = result['msg']
        return render_template('userlist.html',ret=result,session=session)
    else:
        return redirect('/userinfo/')

# 用户更新
@app.route('/update/',methods=['GET','POST'])
def update():
    if request.method == 'GET':
        userid = request.args.get('id')
        data={'id':userid}
        field = ['id','name','name_cn','email','mobile','role','status']
        result = getone('users',field,data)
        return json.dumps(result['msg'])
    else:
        data = {k:v[0] for k,v in dict(request.form).items()}
        field = ['name','name_cn','email','mobile','role','status']
        result = updateuser('users',field,data)
        return json.dumps(result)
    return render_template('update.html')   

# 添加用户
@app.route("/add/",methods=['GET','POST'])
def add():
    if request.method == 'POST':
        data = {k:v[0] for k,v in dict(request.form).items()}
        field = ['name','name_cn','password','email','mobile','role','status']
        result = insert('users',field,data)
        if result['code']==0:
            result['msg'] = "添加用户成功"
            return json.dumps(result)
        else:
            result['msg'] = "添加用户失败"
            return json.dumps(result)
    else:
        return render_template("add.html")

# 删除用户信息
@app.route('/delete/')
def delete_user():
    uid = int(request.args.get('id'))
    result = delete('users',uid)
    return json.dumps(result)
