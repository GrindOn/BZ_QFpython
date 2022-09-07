#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: CartPeressions.py
@time: 2020/3/28 3:57 下午
'''
from rest_framework.permissions import BasePermission

from home.models import AxfUser


class CartPermission(BasePermission):
    def has_permission(self, request, view):
        # 登录用户返回True,未登录的用户返回False
        return isinstance(request.user,AxfUser)