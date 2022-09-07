#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: MyAuthentications.py
@time: 2020/3/24 11:28 上午
'''
import itsdangerous
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from App.models import User
from App.util import token_confirm

class MyAuthentaion(BaseAuthentication):
    # 自定义的认证类必须实现authenticate，
    # 认证的规则，自己定义，成功返回一个二元组(user,value)
    def authenticate(self, request):
        # print("authenticate")
        # 1.获取token
        # token可以从请求的get参数中获取
        token = request.query_params.get('token')

        try:
            uid = token_confirm.confirm_validate_token(token,expiration=3600)
        except itsdangerous.exc.SignatureExpired as e: # token过期
            print(e)
            raise AuthenticationFailed("token过期")
        except:
            return None  # 认证不成功

        # 如果获取到uid
        # 查询数据库，获取用户信息
        try:
            user = User.objects.get(pk=uid)
        except:
            print("数据库访问错误")
            return None

        # print(user.__dict__)
        print("认证通过")
        # 如果找到了用户,认证成功
        return (user, None)

