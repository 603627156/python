#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask,request,render_template,redirect,session
from db import insert,getone,listall,updateuser,delete
from utils import WriteLog
from app import app
import json


# 服务器列表
@app.route('/server/')
def server():
    if session:
        if session['role'] == 'admin':
            field = ['id','hostname','lan_ip','wan_ip','cabinet_id','op','phone']
            result = listall('server',field) 
            if result['code'] == 0:
                result = result['msg']
            return render_template('server/server.html',ret=result,session=session)
        else:
            return redirect('/')
    return redirect('/login/')

# 添加服务器
@app.route("/serveradd/",methods=['GET','POST'])
def serveradd():
    if request.method == 'POST':
        data = {k:v[0] for k,v in dict(request.form).items()}
        field = ['hostname','lan_ip','wan_ip','cabinet_id','op','phone']
        result = insert('server',field,data)
        if result['code']==0:
            result['msg'] = "添加机房成功"
            return json.dumps(result)
        else:
            result['msg'] = "添加机房失败"
            return json.dumps(result)
    else:
        return render_template("server/serveradd.html")

# 删除服务器信息
@app.route('/serverdelete/')
def serverdelete():
    uid = int(request.args.get('id'))
    result = delete('server',uid)
    return json.dumps(result)

# 服务器更新
@app.route('/serverupdate/',methods=['GET','POST'])
def serverupdate():
    if request.method == 'GET':
        userid = request.args.get('id')
        data={'id':userid}
        field = ['id','hostname','lan_ip','wan_ip','cabinet_id','op','phone']
        ret = getone('server',field,data)['msg']
    else:
        data = {k:v[0] for k,v in dict(request.form).items()}
        field = ['hostname','lan_ip','wan_ip','cabinet_id','op','phone']
        result = updateuser('server',field,data)
        return json.dumps(result)
    return render_template('server/serverupdate.html',server=ret)
