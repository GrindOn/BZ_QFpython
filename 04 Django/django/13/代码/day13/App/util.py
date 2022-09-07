#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: util.py
@time: 2020/3/18 11:09 上午
'''

from itsdangerous import URLSafeTimedSerializer as utsr
import base64
# from django.conf import settings as django_settings

class Token:
    def __init__(self, security_key):
        self.security_key = security_key
        self.salt = base64.encodebytes(security_key.encode('utf8'))
    # 生成token
    def generate_validate_token(self, username):
        serializer = utsr(self.security_key)
        res = serializer.dumps(username, self.salt)
        print(serializer)
        return res
    # 验证token
    def confirm_validate_token(self, token, expiration=3600):
        serializer = utsr(self.security_key)
        return serializer.loads(token, salt=self.salt, max_age=expiration)
    # 移除token
    def remove_validate_token(self, token):
        serializer = utsr(self.security_key)
        print(serializer.loads(token, salt=self.salt))
        return serializer.loads(token, salt=self.salt)


token_confirm = Token("sdkfksdfkl*(()872873784387#@#@94.,.,xcv,ksdkfi$#$#")    # 定义为全局变量