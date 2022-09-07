#!/usr/bin/python3
# coding: utf-8

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    'Referer': 'https://www.dushu.com/book/1114_13.html'
}

resp = requests.get('https://img.dushu.com/2007/05/11/00022487592387.jpg_142.jpg',
                    headers=headers)

assert resp.status_code == 200
with open('t1.jpg', 'wb') as f:
    f.write(resp.content)