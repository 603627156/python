from django.shortcuts import render
from django.shortcuts import redirect
from app01 import models

########包装用户请求
from django.shortcuts import HttpResponse
from app01 import models
###########所有都有request，来接收用户数据
########################################首页-登录页面开始###################################################
def index(request):
    if 'user_name' in request.session:
        username = request.session['user_name']
        request.session.set_expiry(60)
        return render(request,'persion.html',{'username':username})
    else:
        return redirect('/login/')
# Create your views here.

#登录页面
def login(request):
    if request.method == "POST":
        login_form = { k:v[0] for k,v in dict(request.POST).items() }
        user_list_obj = models.UserInfo.objects.all()  #查询所有

        for user in user_list_obj:
                 #数据库密码                       #前端传送密码
            if user.user_password == login_form['user_password']:
                request.session['user_name'] = login_form['user_name']
                request.session.set_expiry(60)
                #request.session.get('user_name') == login_form['user_name']
                return redirect('/')
    return render(request,'login.html')
########################################首页-登录页面结束####################################
#######################################用户管理开始##########################################
#注册
def reg(request):
    if request.method == "POST":
        login_form = { k:v[0] for k,v in dict(request.POST).items() }
        models.UserInfo.objects.create(**login_form)
        return redirect('/login/')
    #session信息
    if 'user_name' in request.session:
        username = request.session['user_name']
        request.session.set_expiry(60)
        return render(request,'reg.html',{'username':username})
    else:
        return redirect('/login/')
#用户列表
def userlist(request):
    if 'user_name' in request.session:
        username = request.session['user_name']
        request.session.set_expiry(60)
        result = models.UserInfo.objects.all()
        return render(request,'userlist.html',{'result':result,'username':username})
    else:
        return redirect('/login/')
#退出登录
def logout(request):
    username = request.session['user_name']
    if 'user_name' in request.session:
        request.session.flush()
        return redirect('/login/')
#######################################用户管理结束##########################################

#######################################资产管理开始##########################################
#录音管理
def record(request):
    if 'user_name' in request.session:
        username = request.session['user_name']
        request.session.set_expiry(120)
        result = models.Record.objects.all()
        return render(request,'record.html',{'result':result,'username':username})
    else:
        return redirect('/login/')
#电脑管理
def cumputer(request):
    if 'user_name' in request.session:
        username = request.session['user_name']
        request.session.set_expiry(120)
        result = models.Computer.objects.all()
        return render(request,'computer.html',{'result':result,'username':username})
    else:
        return redirect('/login/')
#######################################工单管理开始##########################################

#######################################运维发布开始##########################################






