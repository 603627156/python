## 第十天作业

### 更新

* 将各个模块进行分拆
* 资产管理(机房，机柜，服务器更新优化)
* 工单申请(工单申请，工单列表,历史工单)

### 目录：

```
[root@LearnPython 09]# tree -L 3
.
├── app
│   ├── cabinet.py
│   ├── config.py
│   ├── db.py
│   ├── idc.py
│   ├── __init__.py
│   ├── job.py
│   ├── loggers.py
│   ├── login.py
│   ├── server.py
│   ├── static
│   │   ├── css
│   │   ├── img
│   │   ├── js
│   │   ├── pulgin
│   │   ├── sort_asc.png
│   │   ├── sort_both.png
│   │   ├── sort_desc.png
│   │   ├── style.css
│   │   └── toastr.min.css
│   ├── templates
│   │   ├── add.html
│   │   ├── base.html
│   │   ├── cabinet
│   │   ├── idc
│   │   ├── job
│   │   ├── login.html
│   │   ├── server
│   │   ├── userinfo.html
│   │   └── userlist.html
│   ├── userlist.py
│   ├── user.py
│   └── utils.py
├── README.md
└── run.py
```


