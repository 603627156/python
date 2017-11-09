#coding:utf-8

import logging

def InitLogger(filename,level,name):

    # create a logging object
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # format log
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(filename)s - [line:%(lineno)s] - %(message)s')

    # create the logging file handle
    fh = logging.FileHandler(filename,mode= 'a+')
    fh.setFormatter(formatter)

    logger.addHandler(fh)
    return logger




