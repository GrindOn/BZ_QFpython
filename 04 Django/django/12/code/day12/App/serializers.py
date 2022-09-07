#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: serializers.py
@time: 2020/3/23 11:19 上午
'''
from datetime import datetime

from rest_framework import serializers

# 就是把对象转换为内置的字典
from rest_framework.relations import PrimaryKeyRelatedField, StringRelatedField

from App.models import Bookinfo, Heroinfo


# def check_date(value):
#     if value < datetime(2010,1,1).date():
#         raise serializers.ValidationError("日期不能小于2010-1-1")
#

# class BookSerializer(serializers.Serializer):
#     btitle = serializers.CharField(max_length=30,required=True)
#     bpub_date = serializers.DateField(allow_null=True,required=False,validators=[check_date])
#     bread = serializers.IntegerField(min_value=30,error_messages={
#         'min_value':'最小值不能小于30'
#     })
#     bcomment = serializers.IntegerField(max_value=50)
#     bimage = serializers.CharField(max_length=300)
#
#     # 单字段验证
#     def validate_bread(self, attrs):
#         print(attrs)
#         if attrs > 1000:
#             raise serializers.ValidationError("不能大于1000")
#
#     # 如果涉及多个字段
#     # def validate(self, attrs):
#     #     pass
#
#     # 重载
#     def create(self, validated_data):
#         print("create")
#         print(validated_data)
#         # book = Bookinfo(btitle=validated_data.get('btitle'))
#         # book.bpub_date = validated_data.get('bpub_date')
#         # book.bread = validated_data.get('bread',0)
#         # book.bcomment = validated_data.get('bcomment',0)
#         # book.bimage = validated_data.get('bimage','')
#         # book.save()
#         # return book
#         return Bookinfo.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#
#         :param instance: 要更新的对象
#         :param validated_data: y要更新的属性字典
#         :return: 对象
#         """
#         print("update")
#         instance.btitle =  validated_data.get('btitle') if validated_data.get('btitle') else instance.btitle
#         if validated_data.get('bpub_date'):
#             instance.bpub_date = validated_data.get('bpub_date')
#         else:
#             instance.bpub_date =  instance.bpub_date
#         instance.bread = validated_data.get('bread') if  validated_data.get('bread') else instance.bread
#         instance.bcomment = validated_data.get('bcomment') if  validated_data.get('bcomment') else instance.comment
#         instance.bread = validated_data.get('bimage') if  validated_data.get('bimage') else instance.bimage
#         instance.save()
#         return instance

class  HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heroinfo
        fields = "__all__"



class BookSerializer(serializers.ModelSerializer):
    # 关联对象
    # heros = PrimaryKeyRelatedField(many=True,read_only=True)

    # Heriinfo的__str__要重写,
    # 返回英雄的名称
    # heros = StringRelatedField(many=True,read_only=True)

    # 获取关联对象所有信息
    heros = HeroSerializer(many=True,read_only=True)

    bread = serializers.IntegerField(min_value=0)  # 重写
    class Meta:
        model = Bookinfo
        fields = '__all__'

    # 自动生成create和update方法
