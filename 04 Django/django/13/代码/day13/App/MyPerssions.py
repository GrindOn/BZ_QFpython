#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: MyPerssions.py
@time: 2020/3/24 3:21 下午
'''
from rest_framework.permissions import BasePermission

from App.models import User


class MyPermisson(BasePermission):
    # 对视图授权
    def has_permission(self, request, view):
        print("权限限制")
        # 返回True就是有权限
        # 返回False就是没权限
        # return False

        # 认证通过就有权限
        return request.user and isinstance(request.user,User)