#!/usr/bin/python3
# coding: utf-8

import asyncio
import csv
import json

import os
import requests
import sys
from bs4 import BeautifulSoup, Tag

from utils.header import get_ua

headers = {
    'User-Agent': get_ua()
}


async def get(url):
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        resp.encoding = 'utf-8'
        await parse(resp.text)


async def post(url, page=2):
    print('---下一页---', url, page)
    await asyncio.sleep(0.5)
    resp = requests.post(url, data={
        "total": 14,
        "action": "fa_load_postlist",
        "paged": page,
        "category": 28,
        "wowDelay": "0.3s"
    }, headers=headers)

    if resp.status_code == 200:
        resp.encoding = 'utf-8'
        ret = json.loads(resp.text[1:])
        print(ret)
        if ret['code'] == 200:
            await parse(ret['postlist'])
            await post(url, page + 1)


async def parse(html):
    root = BeautifulSoup(html, 'lxml')
    content_boxs = root.select('.content-box')

    for content_box in content_boxs:
        item = {}
        img: Tag = content_box.find('img')
        item['name'] = img.attrs.get('alt')
        item['cover'] = img.attrs.get('src')
        info = content_box.select('.posts-text')[0].get_text()
        print(info)
        try:
            _, birthday, city = [txt.strip() for txt in info.split('/')]
            item['birthday'], item['city'] = birthday[2:].strip(), city[2:].strip()
        except:
            item['birthday'], item['city'] = ('', '')

        await itempipeline(item)


async def itempipeline(item):
    await save_csv(item)
    await save_img(item['cover'], item['name'])


async def save_csv(item):
    has_header = os.path.exists(csv_filepath)

    with open(csv_filepath, 'a') as f:
        writer = csv.DictWriter(f, fieldnames=item.keys())
        if not has_header:
            writer.writeheader()

        writer.writerow(item)


async def save_img(url, name):
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        type_ = resp.headers['content-type']  # 获取图片类型
        ext_name = 'png' if type_.startswith('image/png') else '.jpg'
        with open(f'images/{name}{ext_name}', 'wb') as f:
            f.write(resp.content)


if __name__ == '__main__':
    # sys.argv是命令行参数列表， 0位置脚本名，1是脚本名 后的第一个参数
    csv_filepath = sys.argv[1]

    loop = asyncio.get_event_loop()
    # 起始协程是单个
    # loop.run_until_complete(get(''))
    # 起始多个协程
    loop.run_until_complete(asyncio.wait((
        get('http://www.meinv.hk/?cat=28'),
        post('http://www.meinv.hk/wp-admin/admin-ajax.php')
    )))
