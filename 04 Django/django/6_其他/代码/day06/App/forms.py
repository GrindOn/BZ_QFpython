#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: forms.py
@time: 2020/3/16 3:29 下午
'''

from django import forms
from captcha.fields import CaptchaField
class LoginForm(forms.Form):
    captcha = CaptchaField()  # 验证码字段
