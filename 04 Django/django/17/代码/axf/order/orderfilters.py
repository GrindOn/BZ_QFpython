#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: orderfilters.py
@time: 2020/3/30 1:16 下午
'''
from django_filters import rest_framework as filters

from axf import settings
from home.models import AxfOrder


class OrderFilter(filters.FilterSet):
    o_status = filters.CharFilter(field_name='o_status',method='filter_by_status')
    class Meta:
        model = AxfOrder
        fields = ['o_status']

    def filter_by_status(self,queryset,name,value):
        print(value)
        if value == 'not_pay': # 未付款
            return queryset.filter(o_status=settings.ORDER_STATUS_NOT_PAY)
        elif value == 'not_send':  # 未发货
            return queryset.filter(o_status=settings.ORDER_STATUS_NOT_SEND)
        return queryset