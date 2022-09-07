#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: urls.py
@time: 2020/3/9 11:08 上午
'''
from django.urls import path

from App import views

# 路由列表 名称就叫urlpatterns
urlpatterns = [
    # 不能以/ 开头
    path('home/',views.home,name='home'),
]