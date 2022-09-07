#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    用户自定义表单
@author:  
@contact: 
@file: forms.py
@time: 2020/3/16 9:45 上午
'''
from django import  forms
from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList


class RegisterForm(forms.Form):
    def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None,
                 initial=None, error_class=ErrorList, label_suffix=None,
                 empty_permitted=False, field_order=None, use_required_attribute=None, renderer=None,request=None):
        super().__init__(data,files,auto_id,prefix,label_suffix,empty_permitted,field_order,use_required_attribute,renderer)
        self.request = request

    username = forms.CharField(min_length=3,required=True,error_messages={
        'required':'用户名必须输入',
        'min_length':'用户名至少3个字符'
    })
    password = forms.CharField(min_length=3,required=True,error_messages={
        'required': '密码名必须输入',
        'min_length': '密码至少3个字符'
    })
    confirm = forms.CharField(min_length=3,required=True,error_messages={
        'required': '密码名必须输入',
        'min_length': '密码至少3个字符'
    })
    regtime = forms.DateTimeField(required=False,error_messages={
        'invalid':'日期格式错误',
    })
    sex = forms.BooleanField(required=False)

    # 单个字段验证: clean_xxxx
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password and password.isdigit():
            raise ValidationError("密码不能是纯数字")
        return password


    # 全局验证
    def clean(self):
        password = self.cleaned_data.get('password',None)
        confirm = self.cleaned_data.get('confirm','')
        print(password,confirm)
        if password != confirm:
            raise ValidationError({'confirm':"两次密码输入不一致"})
        return self.cleaned_data

