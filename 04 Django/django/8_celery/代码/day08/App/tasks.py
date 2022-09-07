#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    celery任务模块
@author:  
@contact: 
@file: tasks.py
@time: 2020/3/18 2:53 下午
'''

from celery.signals import task_success
from celery import shared_task
import time

from celery.signals import task_success
from django.core.mail import send_mail
from day08.settings import EMAIL_FROM


@shared_task
def hello_world(n):
    for i in range(n):
        print("Hello world")
        time.sleep(2)

# 异步发送邮件
@shared_task
def mail_send(mail):
    """
    subject, message, from_email, recipient_list
    :param mail: 字典  {'subject':'hello'}
    :return:
    """
    send_mail(**mail,from_email=EMAIL_FROM)



@shared_task
def sum_even(n):
    result = 0
    for i in range(0,n+1,2):
        result += i
    return result

# 获取异步任务的结果
@task_success.connect(sender=sum_even)
def complete(sender=None,  result=None,**kwargs):
    print(result)
    print(1111111)

@shared_task
def do():
    print("今日事今日毕")