#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: MyMiddleware.py
@time: 2020/3/17 3:59 下午
'''
import sys

from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from django.views.debug import technical_500_response


class MyMiddleware(MiddlewareMixin):
    def process_request(self,request):
        # print(request.method)
        # 全局路由保护
        print(request.path)
        # username = request.session.get('username')
        # if username:
        #     return
        # elif request.path not in ['/login/']:  # 请求的不是登录界面
        #     return redirect("/login/")

    def process_response(self,request,response):
        print("process_response")
        return response   # 必须返回相应对象

    def process_view(self,request,view_func,view_args,view_kwargs):
        print("在自己的视图函数之前执行")

    # 异常处理
    def process_exception(self, request, exception):
        print("exception")
        # 对管理员展示错误页面，一般用户只能看到404,500等页面
        ip = request.META.get('REMOTE_ADDR')
        if ip == '127.0.0.9':
            return technical_500_response(request, *sys.exc_info())
        return redirect(reverse("App02:index"))


