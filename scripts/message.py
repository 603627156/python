#!/usr/bin/env python
#add  tangbo
#qq 79317360
import json
import requests,sys,time
people = '唐波'
money = 12000
code = 1573
posturl = "http://211.147.239.62:9050/xx/xx"
data = {
    "username":"xxxx",
    "password":"xxxxx",
    "to":"15922585040,",
    "text":"玄武科技短信平台暂时没发现限制，到达率还不错：尊敬的%s，您正在申请旅游分期，金额%s，验证码为：%s，请确认该申请由本人操作！" %(people,money,code),
    "subID":"","msgType":1,
    "encode":1,
    "version":"",
}
postdata = json.dumps(data)
print(postdata)
r = requests.post(posturl,postdata)
print(r)
