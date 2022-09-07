#!/usr/bin/python3
# coding: utf-8

import requests
from requests import Response

from urllib.parse import urlencode

url = 'https://shanghai.anjuke.com/community/'

# 变量名后跟 : 类型， 好处是编程时会自动提醒（提示）对象中的属性及方法
# resp: Response = requests.get(url, params={'from': 'navigation'})


# 声明函数时，参数名后 的` :类型 `表示参数值的类型
# 在函数的() 后的 `-> 类型` 表示函数返回的数据（结果）类型
def download(url: str) -> str:
    # resp: Response = requests.get(url, params={'from': 'navigation'})
    resp: Response = requests.request('get', url, params={'from': 'navigation'})
    if resp.status_code == 200:
        return resp.text  # 文本， resp.content 字节码
    return '下载失败'

def get_douban_json():
    # url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&'  # 请求方法是post
    url = 'https://movie.douban.com/j/chart/top_list'  # 请求方法是post

    params = {
        'type': 5,
        'interval_id': '100:90',  # 100:90
        'action': ''
    }

    data = {
        'start': 1,
        'limit': 20,
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    }

    resp = requests.post(url, params=params, data=data, headers=headers)
    assert resp.status_code == 200
    print(resp.url)
    if 'application/json' in resp.headers['content-type']:
        return resp.json()

    return resp.text


# ret = download(url)
ret = get_douban_json()
print(ret)