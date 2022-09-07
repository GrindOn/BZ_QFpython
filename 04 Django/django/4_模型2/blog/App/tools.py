#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: tools.py
@time: 2020/3/13 11:54 下午
'''

# 自定义分页页码范围
import math

from django.core.paginator import Paginator


class BaiduPaginator(Paginator):
    def custom_range(self,num_pages,page,per_range):
        """
        :param page: 当前页号
        :param per_range: 每页显示多少个页码
        :return: range对象，页码范围
        """
        self.num_pages = num_pages
        # 页码数大于总页数
        if per_range > self.num_pages:
            return range(1,self.num_pages+1)
        elif page <= per_range // 2:
            return range(1, per_range+1)
        elif page + per_range // 2  > self.num_pages:
            return range(self.num_pages-per_range+1, self.num_pages+1)
        else:
            return range(page - per_range//2,page + math.ceil(per_range/2))

