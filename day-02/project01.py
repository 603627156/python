#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-07-31 
# @Author  : tangbo
# @Site    : 
# @File    : 
# @Software:
import os
import subprocess
CMD = "awk '{print $1}' access.txt1 |sort |uniq -c|sort -rn | head -10"
print os.system(CMD)
