#导入flask需要的模块
from flask import Flask,render_template,request
from function.ng import *
res =nginx()

##########################Mysql###########################
import pymysql
conn = pymysql.connect(host='192.168.6.250', port=3306, user='root', passwd='111111',db='flask')
cur = conn.cursor()
username = "select username,passwd from user;"
cur.execute(username)
data = cur.fetchall()   #取值后是元祖 需要转换成字典
##########################Mysql###########################

##################把数据库数据搞成字典###############################
dict={}
for i in data:
    dict[i[0]]=i[1]
#print(dict)
##################################################
#创建一个实例名叫  app
app = Flask(__name__)
#访问/ 调函数登录函数
@app.route('/')
def login():
    users =[{'name':'tangbo','age':18,'role':'admin'},{'name':'reboot','age':2,'role':'fin'},{'name':'wenwen','age':33,'role':'master'}]
    return render_template('login.html',users=users)
                        #前端数据返回到后端  后端数据返回前端

@app.route('/root/',methods=['GET','POST'])
def index():
     if request.method == "POST":
        for user,pwd in dict.items():
            if user == request.form.get('username') and pwd == request.form.get('password'):
                    return render_template('index.html')
        else:
                errors="用户名密码错误，请重新输入！"
                return render_template('login.html',error=errors)

@app.route('/two/')
def b():
    data =res
    return render_template('01/b.html', contan=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug = True)
