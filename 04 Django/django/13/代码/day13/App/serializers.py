#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: serializers.py
@time: 2020/3/24 10:14 上午
'''
from rest_framework import serializers

from App.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = "__all__"