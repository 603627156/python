def add_user():
    f =open('user.txt','a+')
    while True:
        name = input("请输入姓名：").strip()
        if len(name)==0:
            print("用户名不能为空，请重新输入：")
            break;
        else:
            password = input("请输入密码：").strip()
            repass = input("请确认密码：").strip()
            if len(password)==0 or password !=repass:
                print("密码不一致")
                continue;
            else:
                f.write("%s:%s\n" %(name,password))
                f.close()
                print("注册成功")
                break;
def login():
    users={}
    file = open("user.txt")
    content = file.readlines()  #readlines()读取后成为列表
    file.close()
    ##################循环列表，取出用户名密码###
    for user in content:
        name = user.rstrip("\n").split(":")[0]
        users[name] = user.rstrip("\n").split(":")[1]
        
    ###################三次登录####################
    count = 0
    while True:
        count =count+1
        if count >3:
            print("输入次数过多，账号已经锁定！")
            break
        name = input("请输入姓名：").strip()
        if name not in users:
            print("用户不存在，请重新输入！")
            continue
        else:
            password = input("请输入密码：").strip()
            if password != users[name]:
                print("密码错误！")
                continue;
            else:
                print("登录成功！")
            break;

def start_login():
	action = input("Usage:Please Input Your Choice add_user or login!\n").strip()
	if len(action) == 0:
		print("选择错误！")
	if action == "login":
		res = login()
	else:
		res = add_user()
	return res
start_login()
