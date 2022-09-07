#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: tools.py
@time: 2020/3/13 10:32 上午
'''

def query(sql,*args):
    from django.db import connection

    # with语句相当与cursor= connection.cursor() 和 cursor.close(),简化了语
    with connection.cursor() as cursor:
        cursor.execute(sql,args)
        columns = [col[0] for col in cursor.description]
        res = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return res
