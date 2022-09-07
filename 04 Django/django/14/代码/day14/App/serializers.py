#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: serializers.py
@time: 2020/3/25 10:08 上午
'''
from rest_framework import serializers

from App.models import Bookinfo


class BookinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookinfo
        fields = "__all__"
        extra_kwargs = {
            'bread': {
                'required': True,
                'help_text': '阅读量'
            },
            'btitle':{
                'required':True,
                'help_text':'评论量'
            }
        }

