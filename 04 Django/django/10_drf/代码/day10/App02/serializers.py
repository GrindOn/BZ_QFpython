#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: serializers.py
@time: 2020/3/20 2:44 下午
'''
import re

from rest_framework import serializers

# 自定义的序列化器
# class BookSerializer(serializers.Serializer):
#     bid = serializers.IntegerField()
#     btitle = serializers.CharField(max_length=100)
#     bpub_date = serializers.DateField()
#     bread = serializers.IntegerField(min_value=0)
#     bcomment = serializers.IntegerField(min_value=0)
#     bimage = serializers.CharField(max_length=300)


# 通过模型生成序列化器
from App.models import Bookinfo

# 验证函数
def check_comment(value):
    if value > 10000:
        raise serializers.ValidationError("评论数量异常")

class BookSerializer(serializers.ModelSerializer):
    bcomment = serializers.IntegerField(min_value=0,validators=[check_comment])
    class Meta:
        model = Bookinfo
        # fields = ['btitle','bread','bcomment']
        # fields = "__all__"  # 所有字段
        exclude = ['bid']  # 除去bid外，包括其他所有字段

    # 单字段验证
    def validate_bread(self,value):
        print(value,type(value))
        if int(value) < 10:
            raise serializers.ValidationError("读者人数不能小于10")
        return value
    # 多个字段验证
    def validate(self, attrs):
        print(attrs)
        if re.search(r'反政府',attrs['btitle']):
            raise serializers.ValidationError("书名不正确")
        if attrs['bread'] > 1000:
            raise serializers.ValidationError("读者数量异常")
        return attrs