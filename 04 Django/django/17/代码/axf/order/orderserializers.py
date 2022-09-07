#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: orderserializers.py
@time: 2020/3/30 12:04 下午
'''
from rest_framework import serializers

from home.models import AxfOrder, AxfOrdergoods
from market.markserializers import GoodsSerializer


class OrderGoodsSerializer(serializers.ModelSerializer):
    o_goods = GoodsSerializer()
    class Meta:
        model = AxfOrdergoods
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = AxfOrder
        fields = "__all__"

    def to_representation(self, instance):
        # 调用父类方法获取序列化后的数据
        data = super().to_representation(instance)
        order_goods = instance.goods.all()
        # 序列化订单商品信息
        serializer = OrderGoodsSerializer(order_goods,many=True)
        data['order_goods_info'] = serializer.data
        return data


