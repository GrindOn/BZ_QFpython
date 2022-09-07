#!/usr/bin/python3
# coding: utf-8

import sys

def global_excepthook(except_type, value, traceback):
    print('---global_excepthook----')
    print(value, except_type)
    # print_except(traceback)
    # 上传日志报错的信息


def print_except(tb):
    tf = tb.tb_frame
    print(tf.f_code, tf.f_lineno)
    print(tf.f_locals)

    if tb.tb_next:
        print_except(tb.tb_next)

def div(n, m):
    return n/m


if __name__ == '__main__':
    # 指定解释器最后一层异常处理的勾子函数
    sys.excepthook = global_excepthook
    print(div(10, 0))