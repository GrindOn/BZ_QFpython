#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: goodfilters.py
@time: 2020/3/27 11:43 上午
'''
from django_filters import rest_framework as filters

from home.models import AxfGoods


class GoodsFilter(filters.FilterSet):
    typeid = filters.CharFilter(field_name='categoryid',lookup_expr='exact')
    childcid = filters.CharFilter(field_name='childcid',method='filter_child_type')
    order_rule = filters.CharFilter(field_name='order_rule',method='order_goods')
    class Meta:
        model = AxfGoods
        fields = ['categoryid']

    def filter_child_type(self,queryset,name,value):
        print(value,type(value))
        if int(value) > 0:  # value大于0，说明要进行子类过滤
            return queryset.filter(childcid=int(value))
        # 如果value为0，说明没有子类
        return queryset

    def order_goods(self,queryset,name,value):
        value = int(value)
        print(value)

        if value == 1:
            queryset = queryset.order_by("price")
        elif value == 2:
            queryset = queryset.order_by('-price')
        elif value == 3:
            queryset = queryset.order_by('productnum')
        elif value == 4:
            queryset = queryset.order_by("-productnum")
        return queryset