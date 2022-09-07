#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: homeserializers.py
@time: 2020/3/26 3:24 下午
'''

from rest_framework import serializers

from home.models import AxfWheel, AxfNav, AxfMainshow, AxfShop, AxfMustbuy


class WheelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AxfWheel
        fields = "__all__"

class NavSerializer(serializers.ModelSerializer):
    class Meta:
        model = AxfNav
        fields = "__all__"

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = AxfShop
        fields = "__all__"

class MainShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = AxfMainshow
        fields = "__all__"

class MustBuySerializer(serializers.ModelSerializer):
    class Meta:
        model = AxfMustbuy
        fields = "__all__"
