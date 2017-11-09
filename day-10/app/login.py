#!/usr/bin/env python
#-*- coding:utf-8 -*-

from flask import Flask,request,render_template,redirect,session
from db import insert,getone,listall,updateuser,delete
from utils import WriteLog
from app import app
import json

field = ['id','name','name_cn','password','email','mobile','role','status']

# 首页
@app.route('/')
@app.route('/index/')
def index():
    if not session:
        return redirect('/login/')
    return redirect("/userinfo/")

# 注册
@app.route('/reg/',methods=['GET','POST'])
def reg():
    if request.method == 'POST':
        user = { k:v[0] for k,v in dict(request.form).items()}
        result = insert('users',field,user)
        if result['code'] == 0:
            return redirect('/login/')
        else:
            return render_template('reg.html',result=resutl)
    return render_template('reg.html')

# 登录
@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        data = { k:v[0] for k,v in dict(request.form).items()}
        field = ['name','password','role','status']
        result = getone('users',field,data)
        if result['code'] == 0:
            if result['msg']['password'] == data['password']:
                WriteLog("login").info("%s login success" % data['name'])
                session['name'] = data['name']
                session['role'] = result['msg']['role']
                return json.dumps(result)
            else:
                result['code'] = 1
                result['msg'] = '密码错误!'
                return json.dumps(result)
        else:
            result['msg'] = "用户名不存在!"
            return json.dumps(result)
    return render_template('login.html')

# 销毁session
@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/login/')
