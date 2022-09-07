#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: celery.py
@time: 2020/3/18 2:46 下午
'''
from __future__ import absolute_import #绝对路径导入
from celery import Celery
from django.conf import settings
import os

# 设置工程配置文件
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "day08.settings")


# 实例话celery对象
# 第一个参数是应用名称，必须gei
app = Celery('mycelery')

# 设置时区
app.conf.timezone = "Asia/Shanghai"

# 读取配置文件
app.config_from_object("django.conf:settings")

# 自动发现任务
app.autodiscover_tasks()


