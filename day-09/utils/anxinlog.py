#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : tangbo
# @Site    : 
# @File    : 
# @Software:
import logging
def writelog(sql):
    # 定义handler的输出格式            时间          文件名
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(filename)s- %(levelname)s - %(message)s')
    # 创建一个handler，用于写入日志文件,只输出debug级别以上的日志  把日志打到test.log
    fh = logging.FileHandler('wirte.log')
    fh.setFormatter(formatter)
    print(sql)
    # 再创建一个handler，用于输出到控制台
    #ch = logging.StreamHandler()
    #ch.setFormatter(formatter)

    # 创建一个logger命名为mylogger, %(name)s可调用这个名字      日志级别INFO
    logger = logging.getLogger('%s' %sql)
    #print(logger)
    logger.setLevel(logging.INFO)

    ############################上面是定义###################################
    # 给logger添加handler         调用日志
    logger.addHandler(fh)          #日志输出到文件，实际开发
#    logger.addHandler(ch)          #日志输出到控制台，测试


    ###上面代码直接封装成模块
    # 记录两条日志                 #开始记录日志的信息
    logger.info ('foorbar')
    #logger.debug('just a test ')
    return logger
#loging('select * from aa')