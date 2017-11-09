#  作业
###  扒页面

###  static目录没有上传

# 目录结构

<pre>

├── app.py                 # 主文件
├── README.md              # 测试文档及项目文档
├── config.py              # 链接数据库配置
├── test                   # 测试结构图片
├── show_create_table.md   # 表结构
├── static                 # 静态文件(没有上传git）
│   ├── css
│   ├── img
│   ├── js
│   └── pulgin
├── templates              # html文件
│   ├── add.html           # 添加用户
│   ├── base.html          # 模板
│   ├── cabinet_add.html   # 添加机柜
│   ├── cabinet.html       # 机柜列表
│   ├── idc_add.html       # 添加机房 
│   ├── idc.html           # 机房列表 
│   ├── index.html         # 主界面
│   ├── list.html          # 用户界面
│   ├── login.html         # 用户登录
│   ├── reg.html           # 用户注册
│   └── userlist.html      # 用户列表
├── utils.py               # 功能模块
└── utils.pyc




</pre>


# 测试结果

#### 主界面

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/seven/liukai/test/index.png)

#### 注册界面 

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/seven/liukai/test/reg.png)

#### 注册失败

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/seven/liukai/test/reg_error.png)

#### 注册成功

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/seven/liukai/test/reg_ok.png)

#### 登录界面

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/seven/liukai/test/login.png)

#### 登录失败

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/seven/liukai/test/login_error.png)

#### 登录成功

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/seven/liukai/test/login_ok.png)

#### 管理员界面

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/seven/liukai/test/admin.png)


#### 修改个人资料

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/seven/liukai/test/修改个人资料.png)

#### 用户列表

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/seven/liukai/test/userlist.png)

#### 编辑用户信息

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/seven/liukai/test/编辑用户信息.png)

## 删除用户

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/seven/liukai/test/删除用户.png)

## 添加用户

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/seven/liukai/test/添加用户.png)

## 普通用户界面

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/seven/liukai/test/普通用户.png)

# ----------------------资产管理---------------------

## 机房列表

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/eight/liukai/test/%E6%9C%BA%E6%88%BF%E5%88%97%E8%A1%A8.png)

## 添加机房

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/eight/liukai/test/添加机房.png)

## 编辑机房

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/eight/liukai/test/编辑机房.png)

## 删除机房

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/eight/liukai/test/删除机房.png)

## 机柜列表

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/eight/liukai/test/机柜列表.png)

## 添加机柜

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/eight/liukai/test/添加机柜.png)

## 编辑机柜

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/eight/liukai/test/编辑机柜.png)

## 删除机柜

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/eight/liukai/test/删除机柜.png)

## 普通用户机房列表（只读）

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/eight/liukai/test/普通用户机房列表.png)

## 普通用户机柜列表（只读）

![Alt text](https://github.com/51reboot/actual-15-homework/blob/master/eight/liukai/test/普通用户机柜列表.png)

# 项目文档

## 需求分析

> 用户权限管理系统

## 功能模块

### 首页

V: index.html

	1. reg/login两个导航按钮，会连接到登录注册模块
	2. 欢迎信息：wlcome {{username }}
C端
<pre>
@app.route('/') 
@app.route('/index/')
def index():
    username="wd"
    return render_template("index.html",username=username)
</pre>

### 注册页面
V端：reg.html
<pre>
  <\form atction"/reg/",method="POST">
    用户名，密码，角色
  <\/form>
</pre>   
 
C端：
<pre>
@app.route("/reg/",methods=['GET','POST'])
def reg():
    if  method为POST：
        username=request.form.get('username','')
		.........
        if  判断用户是否存在
            如果存在则返回错误信息render_template("reg.html",error=error)
        else:
            sql
            return rediret("跳转到登录页面")
    return render_tempalte("reg.html")
</pre>  

M端:user
<pre>
 mysql> CREATE TABLE `user` (
 ->   `id` int(100) NOT NULL AUTO_INCREMENT,
 ->   `username` varchar(100) NOT NULL,
 ->   `password` varchar(100) NOT NULL,
 ->   `role` int(10) NOT NULL,
 ->   PRIMARY KEY (`id`)
 -> )  DEFAULT CHARSET=utf8;

select * from user where username=username
insert into user () values()
</pre>

#### 登录页面
V端: login.html
<pre>
    <\form atction '/login/',method="POST">
        用户名，密码
    <\/form>
</pre>

C端:
<pre>
@app.route("/login/",methods=["GET","POST"]
def login():
    if method为post：
       username=request.form.get("username"," ")
       password=request.form.get("password"," ")
       if 判断用户是存在并且密码正确：
             if role==1:
                user_dict=查询所有用户信息,并转换为字典
                return render_template("user_list.html",user_dict=user_idct,usaername=username,role=role)
             else:
                user=按用户名查询单用户信息
                return render_template("user.html",user=user)
       
       else：
           msg=用户或密码错误
           return redicet("/login/?msg='用户名或密码错误'")
    return render_tempalte("login.html")
</pre> 

M端:  
<pre>
查所用户信息 sql=" select * from user"
按username 查单用户信息 sql= "select * from user where username=%s"%username
</pre>

## 管理页面/用户列表
    
### 管理员界面    
V端: 
<pre>
1. 左部分 ----><font color=red>显示管理员功能/普通用户更能</font>

2. 右部分 
list.html （右边一个表格显示所有用户信息） 
id ，用户名 ，密码， 权限 ，操作（删除，修改） 
{% for i in user_dict %}                                
  {{ user_dict.id}} ,{{user_dict.username}},{{user_idct.password}},{{user_dict.role}}<\a href="/delete/?id={{user_dict.id }}">删除</a><\a href="/update/?id={{}user_dict.id}">修改</id>
{% endfor %}
</pre>        
     
C端：
<pre>
@app.route("/delete/")
def delete():
    id=request.args.get("id"," ")
        执行删除函数
    return render_tempalte("user_list.html")
</pre>

M端: 
<pre>
sql="delete from user where id=%s"%id
</pre>

### 删除界面
V端： 在list.html上有个按钮，删除后直接跳到登录界面

C端： 获取前端id，根据执行删除sql，然后跳转到login.html

M端： sql="delete from %s where id =%s"%(table,uid)

### 更新页面
V端: update.html

   显示一个表格(名称 ，信息) ,信息内容可改，最下方有个提交按钮（跳转到管理员页面）
                                            
C端:
<pre>
@app.route("/update/")
def update():
    user=执行查询单用户sql，
        return  render_tempalte('update.html'user=user)

@app.route("/update/")
    获取修改的数据
    执行update sql 更改数据库
            
    return render_template("跳转登录界面")
       
  普通用户同上 
</pre>  

M端：
<pre>
  sql="select * from user where id=%s"%id
  
  sql="update user set password='%s',sex=%d,age=%d,phone=%d,email='%s',role=%d where id=%d"%(my_tup[0],my_tup[1],my_tup    
</pre>       

# cdmd 资产管理 

## 机房列表

V端: idc.html  
     <pre>
     显示一个表格（编号，机房名，地址，中文名， 联系人，电话 ，操作）操作里有两个按钮（编辑，删除）表格上方有添加按钮
     点击添加,弹出模态窗，添加机房信息
     点击编辑按钮，跳转到界面，idc_uptdae.html
     点击删除按照，直接执行删除sql
     
     idc_update.html
     点击编辑按钮 ,跳转到idc_update.html，获取id.执行utils.getone。渲染信息
     修改信息。然后点击更新，执行util.update.
     </pre>
     
 C端：
 <pre>
 @app.route('/idc/')
 def idc()：
       查所有机房，
       return render_template("渲染信息")
   
  @app.route("/idc_getone")
  def idc_getone():
      date=utils.getone(idc_table,filed,data)
      return render_template(‘渲染信息')
   
 @app.route('/idc_update/'） 
 def idc_update():
     date=utils.update()
     return json.dumps(data)
   </pre> 
 
 M端：
   <pre> 
    查idc表
    执行util.select(idc_table,idc_field,data)
    
    查单idc信息
    util.getone(idc_table,idc_field,data)
    
    #更新
    utils.update(idc_table,idc_field,data)
    </pre>
