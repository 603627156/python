#! /usr/bin/env python
# __*__coding:utf-8__*__

from flask import Flask,render_template,request,redirect,session
import utils
import json
table="user"
field=['id','username','name','password','phone','email','role','status']

app=Flask(__name__)
app.secret_key="sdafasdfasfd"


#############用户权限管理########################

# 首页
@app.route('/')
@app.route('/index/')
def index():
    return render_template("index.html")

# 注册
@app.route('/reg/',methods=['GET','POST'])
def reg():
    if request.method=='POST':
        user_dict={k:v[0] for k,v in dict(request.form).items()}
        field=['username','name','password','phone','email','role','status']
        user=utils.get_one(table,field,user_dict)
        if user['code']==1:
            result=utils.insert(table,field,user_dict)
            return json.dumps(result)
        else:
            result={'code':1,'msg':'username is error '}
            return json.dumps(result)
    return render_template("reg.html")
      
# 登录
@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method=='POST':
        user_dict={k:v[0] for k,v in dict(request.form).items()}
        user=utils.get_one(table,field,user_dict)
        if  user['code']==0  and  user_dict['password']==user['msg']['password']:
           if user['msg']['status']==0:
               session['username']=user_dict['username']
               session['role']=user['msg']['role']
               data=user
               return json.dumps(data)
           else:
               data={'code':1,'msg':'username is locking'}
               return json.dumps(data)
        else:
           data={'code':1,'msg':'username or password  is error'}
           return json.dumps(data)
    return render_template("login.html")

# 用户界面
@app.route('/user/')
def user():
    if not session:
        return redirect('/')
    username=session['username']
    user_dict={'username':username}
    result=utils.get_one(table,field,user_dict)
    return render_template('list.html',res=session ,result=result['msg'])


# 管理员用户列表
@app.route('/userlist/')
def userlist():
    if session:
        result=utils.list(table,field)
        print result['msg']
        print session
        if result['code']==0:
            return render_template('userlist.html',res=session,result=result['msg'])
        else:
            result={'code':1,'msg':'username or password  is error'}
            return render_template("login.html",result=result)
    else:
        return redirect("/login/")

# 管理员添加用户
@app.route('/add/',methods=['GET','POST'])
def add():
    if not session:
        return redirect('/')
    if request.method=='POST':
        user={k:v[0] for k,v in dict(request.form).items()}
        field=['username','name','password','email','role','status']
        if user['username'] and user['password']:
            data=utils.insert(table,field,user)
            return json.dumps(data)
        else:
           data={'code':1,'errmsg':'username or password is not null'}
           return json.dumps(data)
    return render_template("add.html",res=session)


# 删除   
@app.route('/delete/',methods=['GET','POST'])
def delete():
    if not session:
       return redirect('/')
    uid=request.args.get('id')
    print uid,table
    data=utils.delete(table,uid)
    return json.dumps(data)

# 修改界面
@app.route('/userinfo/',methods=['GET','POST'])
def userinfo():
     if not session:
         return redirect('/')
     if request.method=='GET':
         uid=request.args.get('id')
         data={'id':uid}
         result=utils.get_one(table,field,data)
         if result['code']==0:
            result=result['msg']
     return json.dumps(result)

# 刷新
@app.route('/update/',methods=['GET','POST'])
def update():
    if not session:
       return redirect('/')
    if request.method=='POST':
       user_dict={k:v[0] for k,v in dict(request.form).items()}
       data=utils.update(table,field,user_dict)
       return  json.dumps(data)

# 用户登出
@app.route("/logout/")
def logout():
   if session:
      session.clear()
   return redirect("/")


###### CMDB 资产管理 ##############

#————————————————————机房——————————————————————
idc_table="idc"
idc_field=['id','idc_name','cn_name','address','name','phone']

# 机房管理列表
@app.route("/idc/")
def idc():
    if not session:
        return redirect("/")
    data=utils.list(idc_table,idc_field)
    result=data['msg']
    return render_template("idc.html",res=session,result=result)

# 机房编辑
@app.route('/idc_info/')
def idc_info():
     if not session:
         return redirect('/')
     uid=request.args.get('id')
     data={'id':uid}
     result=utils.get_one(idc_table,idc_field,data)
     if result['code']==0:
        result=result['msg']
     return json.dumps(result)

# 机房信息更新
@app.route('/idc_update/',methods=['GET','POST'])
def idc_update():
    if not session:
       return redirect('/')
    if request.method=='POST':
       user_dict={k:v[0] for k,v in dict(request.form).items()}
       data=utils.update(idc_table,idc_field,user_dict)
       return  json.dumps(data)

# 添加机房,(有个bug，机房名不重复没有判断)
@app.route('/idc_add/',methods=['GET','POST'])
def idc_add():
    if not session:
        return redirect('/')
    if request.method=='POST':
        user={k:v[0] for k,v in dict(request.form).items()}
        idc_field=['idc_name','cn_name','address','name','phone']
        if user['idc_name']:
            data=utils.insert(idc_table,idc_field,user)
            return json.dumps(data)
        else:
           data={'code':1,'errmsg':'username or password is not null'}
           return json.dumps(data)
    return render_template("idc_add.html",res=session)

# 删除机房   
@app.route('/idc_delete/',methods=['GET','POST'])
def idc_delete():
    if not session:
       return redirect('/')
    uid=request.args.get('id')
    data=utils.delete(idc_table,uid)
    return json.dumps(data)

#————————————————机柜——————————————————————————
cab_table="cabinet"
cab_field=['id','cabinet_num','idc_name','cabinet_u','cabinet_a']

# 机柜列表
@app.route('/cabinet/')
def cabinet():
   if not session:
      return redirect('/')
   data=utils.list(cab_table,cab_field)
   print data
   result=data['msg']
   return render_template("cabinet.html",res=session,result=result)

# 添加机柜,(有个bug，机柜名不重复没有判断）
@app.route('/cabinet_add/',methods=['GET','POST'])
def cabinet_add():
    if not session:
        return redirect('/')
    if request.method=='POST':
        user={k:v[0] for k,v in dict(request.form).items()}
        print 'user........',user
        cab_field=['cabinet_num','idc_name','cabinet_u','cabinet_a']
        if user['cabinet_num']:
            data=utils.insert(cab_table,cab_field,user)
            return json.dumps(data)
        else:
           data={'code':1,'errmsg':'username or password is not null'}
           return json.dumps(data)
    return render_template("cabinet_add.html",res=session)

# 添加机柜式选机房接口
@app.route('/idcdata/')
def idcdata():
    result=utils.select(idc_table,'idc_name')
    return json.dumps(result)

# 机柜编辑
@app.route('/cabinet_info/')
def cabinet_info():
     if not session:
         return redirect('/')
     uid=request.args.get('id')
     data={'id':uid}
     result=utils.get_one(cab_table,cab_field,data)
     if result['code']==0:
        result=result['msg']
     return json.dumps(result)

# 机房信息更新
@app.route('/cabinet_update/',methods=['GET','POST'])
def cabinet_update():
    if not session:
       return redirect('/')
    if request.method=='POST':
       user_dict={k:v[0] for k,v in dict(request.form).items()}
       data=utils.update(cab_table,cab_field,user_dict)
       return  json.dumps(data)

# 删除机房   
@app.route('/cabinet_delete/',methods=['GET','POST'])
def cabinet_delete():
    if not session:
       return redirect('/')
    uid=request.args.get('id')
    data=utils.delete(cab_table,uid)
    return json.dumps(data)



if __name__=="__main__":
    app.run(host='0.0.0.0',port=5555,debug=True)

