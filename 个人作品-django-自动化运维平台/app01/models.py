from django.db import models

# Create your models here.
    #E:\tangbo\devops_prod   路径下执行 cmd 命令
    #python manage.py makemigrations  生成配置文件
    #python manage.py migrate         生成创建数据库相关
    #无法创建表    到E:\tangbo\devops_prod\app01\migrations  删除除了init以外的所有文件
###################################本机数据库###########################################
class Localhost(models.Model):
    Localhost_id = models.IntegerField()
    Localhost_memory = models.IntegerField()
    Localhost_cpuifnfo = models.IntegerField()
    Localhost_network = models.IntegerField()

###################################用户管理数据库############################################
class UserInfo(models.Model):
    user_id = models.AutoField
    user_name = models.CharField(max_length=255)
    user_password = models.CharField(max_length=255)
    user_role = models.IntegerField()
    user_user = models.CharField(max_length=255)
    user_phone = models.BigIntegerField()
    user_mail = models.CharField(max_length=255)
    user_status = models.IntegerField()
    createtime = models.DateTimeField(auto_now=True)         #自动添加创建时间
    uptime = models.DateTimeField(auto_now_add=True)    #自动添加更新时间

###################################录音管理数据库############################################
class Record(models.Model):
    record_id = models.AutoField
    record_name = models.CharField(max_length=255)
    record_number =  models.IntegerField()
    record_departmen = models.CharField(max_length=255)
    record_port = models.CharField(max_length=255)
    record_status = models.IntegerField()
    createtime = models.DateTimeField(auto_now=True)         #自动添加创建时间
    uptime = models.DateTimeField(auto_now_add=True)    #自动添加更新时间

###################################电脑固定资产管理数据库#####################################
class Computer(models.Model):
    Computer_id = models.AutoField
    Computer_name = models.CharField(max_length=255)
    Computer_code =  models.CharField(max_length=255)
    Computer_model = models.CharField(max_length=255)
    Computer_price = models.CharField(max_length=255)
    Computer_status = models.IntegerField()
    Computer_departmen = models.CharField(max_length=255)
    Computer_people = models.CharField(max_length=255)
    Computer_source = models.CharField(max_length=255)
    Computer_comment = models.CharField(max_length=255)
    createtime = models.DateTimeField(auto_now=True)         #自动添加创建时间
    uptime = models.DateTimeField(auto_now_add=True)    #自动添加更新时间

###################################电脑变更资产管理数据库###################################
class ComputerChange(models.Model):
    ComputerChange_id = models.AutoField
    ComputerChange_name = models.CharField(max_length=255)
    ComputerChange_code =  models.IntegerField()
    ComputerChange_model = models.CharField(max_length=255)
    ComputerChange_price = models.CharField(max_length=255)
    ComputerChange_status = models.IntegerField()
    ComputerChange_departmen = models.CharField(max_length=255)
    ComputerChange_now = models.CharField(max_length=255)
    ComputerChange_source = models.CharField(max_length=255)
    ComputerChange_comment = models.CharField(max_length=255)
    createtime = models.DateTimeField(auto_now=True)         #自动添加创建时间
    uptime = models.DateTimeField(auto_now_add=True)    #自动添加更新时间

###################################工单系统数据库#############################################
class Job(models.Model):
    job_id = models.AutoField
    job_apply_name = models.CharField(max_length=255)
    job_handle_name =  models.CharField(max_length=255)
    job_apply_type = models.IntegerField()
    job_apply_desc = models.CharField(max_length=255)
    job_status = models.IntegerField()
    createtime = models.DateTimeField(auto_now=True)         #自动添加创建时间
    uptime = models.DateTimeField(auto_now_add=True)    #自动添加更新时间





