#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/07/24 21:34
# @Author  : tangbo
# @Site    : 
import pymysql
import sys
def login():
	for i in range(3):
		USER = raw_input("请输入您的用户名：")
		PASSWD = raw_input("请输入您的密码：")
		###############################锁定用户,生产最好用state状态字段来做#################################
		conn = pymysql.connect(host='192.168.6.250', port=3306, user='root', passwd='111111',db='user')
		cur = conn.cursor()
		sql_lock = "select user from user.lock"
		cur.execute(sql_lock)
		lock_user = cur.fetchall()
		lock_user1=[]
		for i in lock_user:
			#print(i)
			lock_user1.append(i)
			#print(lock_user1[0])
			if USER == i[0]:
				print "该用户已被锁定，请10分钟后在试试:"
				sys.exit()
		###############################################锁定用户#################################

		 ###############################################用户为空或者密码为空，提示错误#################################
		if  len(USER) == 0 or len(PASSWD) == 0 :
			print '*'*50,"用户名或者密码不能为空，请重新输入:",'*'*50
			continue
		 ##############################################密码长度小于6，提示错误#################################
		if  len(PASSWD) < 6 :
			print '*'*50,"密码长度至少是6位:",'*'*50
			continue
		###############################查询用户#############################
		cur = conn.cursor()
		sql = "select ax_user.login,ax_password.passwd from ax_user inner join ax_password where ax_user.id=ax_password.id and ax_user.login='%s' and ax_password.passwd='%s';"%(USER,PASSWD)
		#print(sql)
		cur.execute(sql)
		name = cur.fetchall()
		# print(name)
		if name == ():
			print '*'*50,"用户名密码错误，请重试",'*'*50
		################################登录成功#################################
		else:
			user_pass = name[0]
			input_user = user_pass[0]
			input_passwd = user_pass[1]
			if USER == input_user and PASSWD == input_passwd:
				print '*'*50,'欢迎登陆系统','*'*50
				break
if __name__=='__main__':  
    login()  
