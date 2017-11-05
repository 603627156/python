#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask,request,render_template,redirect,session
from db import insert,getone,listall,updateuser,delete
from utils import WriteLog
from app import app
import json
import time


table="ops_jobs"
field=['id','apply_date','apply_type','apply_desc','deal_persion','status','deal_desc','deal_time','apply_persion']

# 工单申请
@app.route("/jobadd/",methods=['GET','POST'])
def jobadd():
    if request.method == 'POST':
        job = {k:v[0] for k,v in dict(request.form).items()}
        field = ['apply_date','apply_type','apply_desc','status','apply_persion']
        job['apply_date'] = time.strftime('%Y-%m-%d %H:%M')
        job['apply_persion'] = session['name']
        job['status'] = 0
        result = insert('ops_jobs',field,job)
        if result['code']==0:
            result['msg'] = "工单提交成功"
            return json.dumps(result)
        else:
            result['msg'] = "工单提交失败"
            return json.dumps(result)
    else:
        return render_template("job/jobadd.html")

# 工单列表
@app.route("/job/")
@app.route("/joblist/",methods=['GET','POST'])
def joblist():
    if not session:
        return redirect("/")
    result = listall(table,field)['msg']
    return render_template("job/joblist.html",job=result,res=session )

# 修改列表
@app.route("/jobupdate/",methods=['GET','POST'])
def jobupdate():
    if not session:
        return redirect("/")
    if request.method == "GET":
        data = {}
        data['id'] = int(request.args.get('id'))
        data['deal_persion'] = session['name']
        data['status'] = 1
        field = ['deal_persion','status']
        result = updateuser(table,field,data)
        print result
        return json.dumps(result)
    else:
        data={k:v[0] for k,v in dict(request.form).items()}
        data['deal_persion'] = session['name']
        data['status'] = 2
        data['deal_time'] = time.strftime('%Y-%m-%d %H:%M')
        field=['deal_persion','deal_time','deal_desc','status']
        result=updateuser(table,field,data)
        return json.dumps(result)

# 工单详情
@app.route('/jobdetail/',methods=["GET","POST"])
def jobdetail():
    if request.method == "GET":
        data = {}
        data['id'] = int(request.args.get("id"))
        result = getone(table,field,data)
        result['msg']['apply_date'] = str(result['msg']['apply_date'])
        result['msg']['deal_time'] = str(result['msg']['deal_time'])
        return json.dumps(result)

# 历史工单
@app.route("/jobhistory/",methods=['GET','POST'])
def jobhistory():
    if not session:
        return redirect("/")
    result=listall(table,field)['msg']
    return render_template("job/jobhistory.html",data=result,res=session )
