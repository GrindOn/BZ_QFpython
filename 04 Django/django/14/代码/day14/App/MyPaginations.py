#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: MyPaginations.py
@time: 2020/3/25 10:59 上午
'''
from collections import OrderedDict

from django.core.paginator import InvalidPage
from rest_framework.exceptions import NotFound
from rest_framework.pagination import PageNumberPagination

#http://127.0.0.1:9008/book/?page=1&page_size=6
from rest_framework.response import Response


class BookListPager(PageNumberPagination):
    page_size = 5  # 每页5条记录
    page_size_query_param = 'page_size'  # 每页记录数的参数名字


    # 自定义分页形式
    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('page_range', list(self.page.paginator.page_range)),  # 页码范围
            ('has_next', self.page.has_next()),
            ('has_prious', self.page.has_previous()),
            ('next_page_number', self.page.next_page_number()),
            ('results', data)
        ]))