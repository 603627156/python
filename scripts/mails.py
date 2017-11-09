#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : tangbo
# @Site    : 
# @File    : 
# @Software:

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
def mail():
    ret = True
    try:
        msg = MIMEText('邮件内容','plain','utf-8')
        msg['From'] = formataddr(["唐波",'79313760@qq.com.com'])
        msg['To'] = formataddr(["任川",'bo.tang@szpcg.com.com'])
        msg['To'] = formataddr(["tangbo",'603627156@qq.com'])
        msg['Subject'] = "主题"

        server = smtplib.SMTP("smtp.qq.com", 25)
        server.login("79313760@qq.com","tb79313760")
        server.sendmail("79313760@qq.com",['bo.tang@szpcg.com'],msg.as_string())
        server.quit()
    except Exception:
        ret = False
    return 'ret'
ret = mail()
if ret:
    print("Mail is Sucess")  #函数返回值,"Success"成功，Fail则失败
else:
    print("Mail is Failed")
