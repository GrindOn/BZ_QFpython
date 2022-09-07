#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: userserializers.py
@time: 2020/3/27 3:15 下午
'''
from django.contrib.auth.hashers import make_password, check_password
from rest_framework import serializers

from home.models import AxfUser

# 用户序列化器
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AxfUser
        fields = "__all__"


class UserRegisterSerializer(serializers.Serializer):
    u_username = serializers.CharField(required=True)
    u_password = serializers.CharField(min_length=3,max_length=12,
                                       error_messages={
                                           'max_length':'最大长度不超过12个字符',
                                           'min_length':'最小长度不能少于3个字符'
                                       })
    u_password2 = serializers.CharField(min_length=3, max_length=12,
                                       error_messages={
                                           'max_length': '最大长度不超过12个字符',
                                           'min_length': '最小长度不能少于3个字符'
                                       })
    u_email = serializers.EmailField(required=True)

    # 验证用户名是否唯一
    def validate_u_username(self, attrs):
        print(attrs)
        user = AxfUser.objects.filter(u_username=attrs).first()
        if user:
            raise serializers.ValidationError("用户名已经存在")
        return attrs

    # 全局验证
    def validate(self, attrs):
        password = attrs.get('u_password')
        password2 = attrs.get('u_password2')
        if password != password2:
            raise serializers.ValidationError({'u_password':"两次密码不一致"})
        return attrs

    def create(self, validated_data):
        user = AxfUser()
        password = validated_data.get('u_password')
        password = make_password(password)  # 对密码加密
        user.u_username = validated_data.get('u_username')
        user.u_password = password
        user.u_email = validated_data.get('u_email')
        user.is_active = 1  # 活动用户
        user.is_delete = 0  # 未删除
        user.save()
        return user

# 登录序列化
class LoginSerializer(serializers.Serializer):
    u_username = serializers.CharField(min_length=3,required=True)
    u_password = serializers.CharField(required=True,min_length=3)

    def validate(self, attrs):
        username = attrs.get('u_username')
        password = attrs.get('u_password')
        user = AxfUser.objects.filter(u_username=username)
        # 判断用户是否存在
        if not user.exists():
            raise serializers.ValidationError('用户不存在')
        # 用户存在
        user = user.first()
        #check_password(明文密码，签名的密码) 如果二者相等返回True，否则返回Fase
        if not check_password(password,user.u_password):
            raise serializers.ValidationError('用户名或密码错误')
        return attrs