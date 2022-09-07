#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: MyFilters.py
@time: 2020/3/25 2:53 下午
'''
from django_filters import rest_framework as filters

from App.models import Bookinfo




class BookFilter(filters.FilterSet):
    # 查询字段名不要求和模型中一模一样
    # field_name 模型中的字段名
    # method 查询方法
    # http://127.0.0.1:9090/list/?comment=50
    comment = filters.NumberFilter(field_name='bcomment', method='find_comment')

    class Meta:
        model = Bookinfo

        fields = {
            # 运算符和ORM中运算符一模一样
            #http://127.0.0.1:9008/list/?btitle__icontains=%E5%85%AB
            'btitle':['icontains','startswith','iendswith'],  # 不区分大小写的包含
            # http://127.0.0.1:9008/list/?bread__gt=10&bread__lt=50
            'bread':['exact','lt','gt','lte','in'],
        }

    def find_comment(self,queryset,name,value):
        """
        :param queryset:
        :param name: 查询字段名
        :param value: 查询的值
        :return: queryset
        """
        print(name,value)
        return queryset.filter(bcomment__lt=value)
