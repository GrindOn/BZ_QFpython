#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: mytag.py
@time: 2020/3/10 3:58 下午
'''
from django import template

# 建立模板对象
register = template.Library()


@register.filter(name='sub1')
def sub(value):   # 参数最多两个
    return value - 1
