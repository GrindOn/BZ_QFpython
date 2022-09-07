#!/usr/bin/python3
# coding: utf-8
import random


# 声明cookies池
cookie_txts = [
    'login=flase; ASP.NET_SessionId=dvvv44h4g5q5gmmq35aoognm; Hm_lvt_04660099568f561a75456483228a9516=1577252223,1577259943,1577769631,1577780076; codeyzgswso=9099dcfaa4e7fdd1; gsw2017user=218038%7c17DCCCFC9CFB3C545385F467342A11CE; login=flase; gswZhanghao=610039018%40qq.com; gswEmail=610039018%40qq.com; idsShiwen2017=%2c71137%2c71138%2c71139%2c7722%2c49386%2c71250%2c64945%2c; Hm_lpvt_04660099568f561a75456483228a9516=1577780185',

]

def get_cookie():
    cookie = random.choice(cookie_txts)
    # ret = {}
    # for c in cookie.split(';'):
    #     k, v = c.split('=')
    #     ret[k ] = v
    #
    return {
        c.split('=')[0].strip(): c.split('=')[1].strip()
        for c in cookie.split(';')
    }

if __name__ == '__main__':
    print(get_cookie())