#!/usr/bin/python3
# coding: utf-8
from . import Connection


class BaseDao:
    def __init__(self):
        self.conn = Connection()

    def query(self, table_name, *columns, where=None, args=None):
        sql = 'select %s from %s '
        sql = sql % ( ','.join(columns) , table_name)
        if where:
            sql += where

        with self.conn as c:
            if args:
                # args 可以是tuple, 与sql中的%s对应
                #      可以是dict , 与sql中的 %(xxx)s  对应
                c.execute(sql, args)
            else:
                c.execute(sql)

            ret = c.fetchall()  # list[<dict>, <dict> ]

        return ret

    def save(self, table_name, instance):
        pass

    def update(self, table_name, instance, where, whereargs):
        pass

    def delete(self, table_name, where, whereargs):
        pass

