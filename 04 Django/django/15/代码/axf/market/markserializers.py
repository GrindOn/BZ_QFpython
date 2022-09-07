#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: markserializers.py
@time: 2020/3/26 4:45 下午
'''

from rest_framework import serializers

from home.models import AxfFoodtype
class GoodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AxfFoodtype
        fields = "__all__"
