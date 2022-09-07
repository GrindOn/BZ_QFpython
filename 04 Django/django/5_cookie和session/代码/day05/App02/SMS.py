#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: SMS.py
@time: 2020/3/3 3:05 下午
'''
import random
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest

ACCESS_KEY_ID = "LTAIDHOYSjYcvyVt"  #用户AccessKey  需要根据自己的账户修改
ACCESS_KEY_SECRET = "qrEgykmXX4e6GUMFOqzuiLZ5gsUxSC"  #Access Key Secret  需要根据自己的账户修改

class SMS:
    def __init__(self,signName,templateCode):
        self.signName = signName  #签名
        self.templateCode = templateCode  #模板code
        self.client = client = AcsClient(ACCESS_KEY_ID, ACCESS_KEY_SECRET, 'cn-hangzhou')

    def send(self,phone_numbers,template_param):
        request = CommonRequest()
        request.set_accept_format('json')
        request.set_domain('dysmsapi.aliyuncs.com')
        request.set_method('POST')
        request.set_protocol_type('https')  # https | http
        request.set_version('2017-05-25')
        request.set_action_name('SendSms')

        request.add_query_param('RegionId', "cn-hangzhou")
        request.add_query_param('PhoneNumbers', phone_numbers)
        request.add_query_param('SignName', self.signName)
        request.add_query_param('TemplateCode', self.templateCode)
        request.add_query_param('TemplateParam', template_param)
        response = self.client.do_action_with_exception(request)
        return response
# 短语发送对象
sms = SMS("成少雷","SMS_102315005")
