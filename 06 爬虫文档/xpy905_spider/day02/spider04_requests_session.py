"""
1. 下载验证码的图片
2. 图片验证码的打码- 获取图片上的验证码
3. 登录
4. 获取个人的收藏信息
"""
import uuid
from lxml import etree

import requests

from utils.header import  get_ua
from utils.chaojiying import rec_code

# 创建session对象
# 获取验证码接口和登录接口必须在同一个session中请求
session = requests.session()


def download_code():
    resp = session.get('https://so.gushiwen.org/RandCode.ashx',
                       headers={'User-Agent': get_ua()})
    with open('code.png', 'wb') as f:
        f.write(resp.content)


def get_code_str():
    download_code()
    return rec_code('code.png')

def login():
    resp = session.post('https://so.gushiwen.org/user/login.aspx',
                        data={
                            'email': '610039018@qq.com',
                            'pwd': 'disen8888',
                            'code': get_code_str()  # 验证码
                        })

    if resp.status_code == 200:
        collect()

    else:
        print('-'*30)
        print(resp.text)


def collect():
    resp = session.get('https://so.gushiwen.org/user/collect.aspx')
    parse(resp.text)

def parse(html):
    root = etree.HTML(html)  # 获取html的根元素 Element
    divs = root.xpath('//div[@class="left"]/div[@class="sons"]') # list[<Element>, ..]
    item = {}
    for div in divs:
        item['id'] = uuid.uuid4().hex
        item['name'] = div.xpath('.//p[1]//text()')[0]
        item['author'] = ' '.join(div.xpath('.//p[2]/a/text()'))
        item['content'] = '<br>'.join(div.xpath('.//div[@class="contson"]/text()'))
        item['tags'] = ','.join(div.xpath('./div[last()]/a/text()'))

        print(item)

if __name__ == '__main__':
    login()