#!/usr/bin/python2.6.6
#-*- coding:utf-8 -*-

from flask import Flask,request,redirect,render_template,session
from app import app
from ansible.runner import Runner
import os,json,urllib,sys,time

def ansible_cmd(pattern,module,args,forks):
    result = Runner(
            module_name = module,
            module_args = args,
            pattern = pattern,
            forks = forks).run()
    return result


@app.route('/ansible/')
def ansible():
    if not session.get('name',None):
        return redirect("/login")
    return render_template("ansible/ansible.html",info=session)

@app.route('/cmd/',methods=['GET','POST'])
def cmd():
    if not session.get('name',None):
        return redirect("/login")
    name = session.get('name')
    cmd_time = time.strftime('%Y-%m-%d %H:%M:%S')
    if request.method == "POST":
        cmdmsg  = {k:v[0] for k,v in dict(request.args).items()}
        results = ansible_cmd(cmdmsg['pattern'],cmdmsg['module'],cmdmsg['cmd'],cmdmsg['forks'])
        record = "[%s] - %s - %s - %s\n" % (cmd_time,name,cmdmsg['pattern'],cmdmsg['cmd'])
        with open("/tmp/jobs.log",'a') as f:
            f.write(record)
        string = ""
        if results is None:
            print "No host found"
            sys.exit(1)
        for (hostname,result) in  results['contacted'].items():
            if not "failed" in result and result['stdout'] != "":
                string += "%s | %s | sucess >> \n %s \n" % (hostname,result['cmd'],result['stdout'])
            else:
                string += "%s | %s | failed >> \n %s \n" % (hostname,result['cmd'],result['stderr'])
        return string

@app.route('/ansible/joblist/')
def cmdlist():
    str = ''
    with open('/tmp/jobs.log','r') as f:
        for line in reversed(f.readlines()):
            str += line+"</br>"
    return str
