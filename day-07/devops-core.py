#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/20 9:16
# @Author  : tangbo
# @Site    :
# @File    : 04-上午.py
# @Software: PyCharm
from flask import Flask,render_template,request,redirect,session
from utils.utils import *
import time
import json

#创建一个实例名叫  app
app = Flask(__name__)
app.secret_key="jdbjd67436734hjdsbuie"

#根和index都是首页
@app.route("/",methods=["GET","POST"])
@app.route('/index/')
def index():
	if not session:
		return redirect("/login")
	username = "wd"
	return render_template("index.html",username=username)

#reg注册增加页面
@app.route('/reg/',methods=['GET','POST'])
def reg():
	if request.method == "POST":
		#前端进来数据生成字典
		user = { k:v[0] for k,v in dict(request.form).items() }
		print (user)
		#定义数据库字段，要和数据库一致
		field = ['user_name','user_password','user_role']
				#调用数据库函数，一致的
		result = insert('user',field,user) #赋值变量函数还是会执行
				#成功返回
		if result['code'] == 0:
			return redirect('/login/')
		else:
	        #失败返回
			return render_template('reg.html',result=result)
	return render_template('reg.html')

#用户登录
@app.route("/login/",methods=["GET","POST"])
def login():
	if request.method == "POST":
		data = { k:v[0] for k,v in dict(request.form).items() }
		# print (data)
		field = ['user_id','user_name','user_password','user_role']
		result = getone('user',field,data)
		if result['code'] == 0:
			if result['msg']['user_password'] == data['user_password']:
				session['user_name'] = data['user_name']
				session['user_role'] = result['msg']['user_role']
				# print (session)
				if session['user_role'] == 0:
					return redirect('/')
				else:
					return redirect('/')
		else:
			result['errmsg'] = "user is exist password is wrong "
			return render_template('login.html',result=result)
	return render_template('login.html')

#列出所有
@app.route("/userlist/",methods=["GET","POST"])
def userlist():
	if not session:
		return redirect('/login')
	field = ['user_id','user_name','user_password','user_role']
	result = list('user',field)
	if result['code'] == 0:
		result = result['msg']
	return render_template('userlist.html',result=result)

#删除用户
@app.route("/delete/",methods=["GET","POST"])
def userdel():
    if not session:
        return redirect('/login')
    user_id = request.args.get('id','')
    print(user_id)
    result = delete('user',user_id)
    return redirect('/userlist/')

#用户信息和下面用户更新是一致的
@app.route("/userinfo/",methods=["GET","POST"])
def userinfo():
    if not session:
        return redirect('/login')
    uid = request.args.get('id','')
    data = {'user_id':uid}
    print(uid)
    field = ['user_id','user_name','user_password','user_role']
    result = getone('user',field,data)
    print('111',result)
    return  render_template('update.html',result=result)

#用户更新
@app.route("/update/",methods=["GET","POST"])
def modity():
    if not session:
        return redirect('/login')
    if request.method == "POST":
        data = dict(request.form)
        data = { k:v[0] for k,v in data.items() }
        # print (data)
        field = ['user_name','user_password','user_role']
        result = update('user',field,data)
        # print (result)
        if result['code'] == 0:
            return redirect('/userlist/')
        else:
            return render_template('update.html',result=result)

#退出登录
@app.route("/logout/",methods=["GET","POST"])
def logout():
	if session:
		session.clear()
	return redirect('/login')


#localhost
@app.route("/host/",methods=["GET","POST"])
def host():
	if not session:
		return redirect('/login')
	res = mem()
	now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	b = [now]
	c=[]
	for i in res:
		c.append(i[0])
	local_data = [[b[0],item] for  item in c ]
	return  render_template('host.html',local_data=local_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug = True)
