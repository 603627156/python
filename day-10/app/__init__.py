#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask

app = Flask(__name__)
app.secret_key="dsddddddffdsggdsgagdg"

import login
import user
import userlist
import idc
import cabinet
import server
import job
import ansiblecmd
