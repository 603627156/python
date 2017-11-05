#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask,request,render_template,redirect,session
from db import insert,getone,listall,updateuser,delete
from utils import WriteLog
from app import app
import json

field = ['id','name','name_cn','password','email','mobile','role','status']

# 个人信息
@app.route('/userinfo/')
def userinfo():
    if not session:
        return redirect('/login/')
    data = {'name':session['name']}
    result = getone('users',field,data)
    if result['code'] == 0:
        result = result['msg']
    return render_template('userinfo.html',user=result)

# 修改个人密码
@app.route('/changepwd/oneself/',methods=['POST'])
def chpwdoneself():
    if not session:
        return redirect('/login/')
    passwd = {k:v[0] for k,v in dict(request.form).items()}
    data = {'name':session['name']}
    field = ['id','name','password']
    result = getone('users',field,data)
    if result['msg']['password'] == passwd['oldpasswd']:
        result['msg']['password'] = passwd['newpasswd']
        field = ['password']
        result = updateuser('users',field,data=result['msg'])
    else:
        result ={'code':1, 'msg':u"旧密码不正确请重新输入!"}
    return json.dumps(result)

# 更新
@app.route('/update/oneself/',methods=['GET','POST'])
def update_oneself():
    if request.method == 'GET':
        userid = request.args.get('id')
        data={'id':userid}
        field = ['id','name','name_cn','email','mobile']
        result = getone('users',field,data)
        return json.dumps(result['msg'])
    else:
        data = {k:v[0] for k,v in dict(request.form).items()}
        field = ['name','name_cn','email','mobile']
        result = updateuser('users',field,data)
        return json.dumps(result)
    return render_template('update.html')   
