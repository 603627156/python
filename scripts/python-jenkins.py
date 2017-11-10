#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : tangbo
# @Site    : 
# @File    : 
# @Software:
import jenkins
import time
import sys
url = 'xxxxxxxxxxxxx'
username = 'xxxxxxxx'
password = 'xxxxxxxxxxxxxxx'
jobName='gateway'
server = jenkins.Jenkins(url, username, password)
def anxin():
    server = jenkins.Jenkins(url, username, password)
    server.build_job(jobName)
    next_bn = server.get_job_info(jobName)['nextBuildNumber']
    print(next_bn)
    while True:
        time.sleep(1)
        print ('正在构建中')
        last_build_number = server.get_job_info(jobName)['lastCompletedBuild']['number']
        if last_build_number == next_bn:   #==0表示在构建
            break;
        else:
            time.sleep(5)

        #最后构建
    last_build_number = server.get_job_info(jobName)['lastCompletedBuild']['number']
    build_info = server.get_build_info(jobName, last_build_number)
    build_result = build_info['result']
    if build_result == 'SUCCESS':
        print(jobName,last_build_number,'构建成功')
        sys.exit(0)
    else:
        print("Fail")
        sys.exit(-1)

if __name__ == '__main__':
        anxin()


        #git describe --tags `git rev-list --tags --max-count=1`