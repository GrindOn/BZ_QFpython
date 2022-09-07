#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: cartserializers.py
@time: 2020/3/28 11:12 上午
'''
from rest_framework import serializers

from home.models import AxfGoods, AxfCart
from market.markserializers import GoodsSerializer


class CartAddSerializer(serializers.Serializer):
    goodsid = serializers.CharField(required=True)
    token = serializers.CharField()
    def validate_goodsid(self, value):
        value = int(value)
        print(value)
        the_goods = AxfGoods.objects.filter(pk=value).first()
        if not the_goods:
            raise serializers.ValidationError("商品不存在")
        return value

    def validate_token(self, data):
        if not data:
            raise serializers.ValidationError("token不存在")
        return data




class CartSerializer(serializers.ModelSerializer):
    c_goods = GoodsSerializer()  # 关联序列化
    class Meta:
        model = AxfCart
        fields = "__all__"