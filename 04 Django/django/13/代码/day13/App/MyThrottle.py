#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: MyThrottle.py
@time: 2020/3/24 4:05 下午
'''
from rest_framework.throttling import SimpleRateThrottle

class MyThrottle(SimpleRateThrottle):
    rate = '5/m'  # 请求次数/时间段 （s,m,h,d）
    scope = 'MyThrottle'
    def get_cache_key(self, request, view):
        print("dddddd")
        # print(request.user.__dict__)
        #根据用户ID,登录不限制，不登录限制每分钟5次
        if request.user and request.user.id:
            print(1111)
            return None  # 返回None，没有次数限制
        else:
            print(22222)
            return 1   # 未登录用户