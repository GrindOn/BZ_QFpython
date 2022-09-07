"""
爬取美女网
- requests
- bs4
- csv 存储
- 扩展 协程 asyncio
"""
import json

import requests
import time
from bs4 import BeautifulSoup, Tag

from utils.header import get_ua

headers = {
    'User-Agent': get_ua()
}


def get(url):
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        resp.encoding = 'utf-8'
        parse(resp.text)


def parse(html):
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

        itempipeline(item)

    # 加载下一页
    post('http://www.meinv.hk/wp-admin/admin-ajax.php')


page = 2

def post(url):
    print('---下一页---', url)
    time.sleep(1)
    global page
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
        parse(ret['postlist'])

        page += 1


def itempipeline(item):
    print(item)


if __name__ == '__main__':
    start_url = 'http://www.meinv.hk/?cat=28'
    get(start_url)
