#!/usr/bin/python3
# coding: utf-8
import pymysql
from pymysql.cursors import DictCursor


class Connection():
    def __init__(self):
        self.conn = pymysql.Connect(host='localhost',
                                    port=3306,
                                    user='root',
                                    password='root',
                                    db='stu',
                                    charset='utf8')

    def __enter__(self):
        # DictCursor 针对查询的结果进行dict化
        return self.conn.cursor(cursor=DictCursor)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.conn.rollback()  # 回滚事务
            # 日志收集异常信息， 上报给服务器
        else:
            self.conn.commit()  # 提交事务

    def close(self):
        try:
            self.conn.close()
        except:
            pass