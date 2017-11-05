#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask,request,render_template,redirect,session
from db import insert,getone,listall,updateuser,delete
from utils import WriteLog
from app import app
import json


# 机柜列表
@app.route('/cabinet/')
def cabinet():
    if session:
        if session['role'] == 'admin':
            field = ['id','name','idc_id','u_num','power']
            idc_field = ['id','name']
            cab = listall('cabinet',field)['msg']
            idcs = listall('idc',idc_field)['msg']
            idc = {"%s" % idc['id']:idc['name'] for idc in idcs}
            for c in cab:
                if str(c['idc_id']) in idc:
                    c['idc_id'] = idc[str(c['idc_id'])]
            return render_template('cabinet/cabinet.html',ret=cab,session=session)
        else:
            return redirect('/')
    return redirect('/login/')

# 机柜更新
@app.route('/cabinetupdate/',methods=['GET','POST'])
def cabinetupdate():
    if request.method == 'GET':
        userid = request.args.get('id')
        data={'id':userid}
        field = ['id','name','idc_id','u_num','power']
        ret = getone('cabinet',field,data)['msg']
        idc_field = ['id','name']
        idcs = listall('idc',idc_field)['msg']
    else:
        data = {k:v[0] for k,v in dict(request.form).items()}
        field = ['name','idc_id','u_num','power']
        result = updateuser('cabinet',field,data)
        return json.dumps(result)
    return render_template('cabinet/cabinetupdate.html',cabinet=ret,idcs=idcs)

# 机柜添加
@app.route('/cabinetadd/',methods=['GET','POST'])
def cabinetadd():
    if request.method == 'POST':
        data = {k:v[0] for k,v in dict(request.form).items()}
        field = ['name','idc_id','u_num','power']
        result = insert('cabinet',field,data)
        if result['code']==0:
            result['msg'] = "添加机柜成功"
            return json.dumps(result)
        else:
            result['msg'] = "添加机柜失败"
            return json.dumps(result)
    else:
        field_idc = ['id','name']
        idcs = listall('idc',field_idc)['msg']
    return render_template('cabinet/cabinetadd.html',idcs=idcs)

# 删除机柜信息
@app.route('/cabinetdelete/')
def delete_cabinet():
    uid = int(request.args.get('id'))
    result = delete('cabinet',uid)
    return json.dumps(result)
