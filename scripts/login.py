me    : 2017/2/6 21:37
# @Author  : tangbo
# @Site    : 
# @File    : (021)作业.py
# @Software: PyCharm

def login():
    f=open("user-login",'r') #读取user配置文件。
    cont=f.readlines() #readlines把读取的行当作元素返回一个列表
    f.close()
    allname=[]         #初始化一个用户列表
    allpasswd=[]
    for i in range(0,len(cont)-1):          #len获取cont列表的元素数量
        onecont=cont[i].split()         #循环取一行内容并分割成列表，split（）以空格为分隔符分割字符串并返回一个列表。
        onename=onecont[0]              #循环取一行中的帐号
        onepasswd=onecont[1]            #
        allname.append(onename)         #循环把每一行取到的帐号追加到用户列表中
        allpasswd.append(onepasswd)
    lf=open("user-login.lock",'r')
    lcont=lf.readlines()
    lf.close()
       # print(lcont) #打印用户锁文件内容
      # print(allname)
        # print(allpasswd)

    cont=0
    while cont < 3:
        username=input("login user-login:").strip()
        passwd=input("password:")
        if username not in allname:
            print("No this accont!")

        elif (username +"\n") in lcont:
            print("your account has been locked!Please contact admin!")
            break
        else:
            rel_passwd_index=allname.index(username) #取该帐号在用户列表中的索引，此时用户列表的索引和密码列表的索引是对应的，因此我们同样>取到了该帐号的密码在密码列表的索引
            rel_passwd=allpasswd[rel_passwd_index]     #取该帐号的真实密码
        if passwd==rel_passwd:
            print("Login success!")
            break
        else:
            print("password is error!")
            cont+=1
        if cont >= 3:
            print("Excessive password error,your account has been locked!Please contact admin!")
            nf=open("user-login.lock",'wb')
            nf.write(username+"\n")
            nf.close()
 login()
