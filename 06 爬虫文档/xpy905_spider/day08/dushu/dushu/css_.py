#!/usr/bin/python3
# coding: utf-8
import re
from xml.etree import ElementPath

import requests

def download_css():
    resp = requests.get('https://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/6e9d6f5f474a0a9e0c81f77d5c2868f3.css')
    assert resp.status_code == 200
    with open('css/svg2.css', 'w') as f:
        f.write(resp.text)

def download_svg():
    resp = requests.get('https://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/7ca24952204db2e52ba3b19e2cbccab0.svg')
    assert resp.status_code == 200
    with open('gvm.svg', 'w') as f:
        f.write(resp.text)


def css2dict():
    '''
    将svg.css的样式文件转成字典
    :return:
    '''
    with open('css/svg2.css') as f:
        css = f.read()

    ret = re.findall(r'\.(.*?)\{background:-(\d+?)\.0px -(\d+?)\.0px', css)
    return {
        name: (x, y)
        for name, x, y in ret
    }


def find_char(x, y):
    # 根据x和y的坐标查找文字
    with open('css/wqk.svg') as f:
        for line in f:
            ret = re.search(r'<text x="0" y="(\d+?)">(.+?)</text>', line)
            if ret:
                y_, text = ret.groups()
                if int(y_) >= int(y):
                    index = int(x)//14
                    return text[index]

def find_char2(x, y):
    # 根据x和y的坐标查找文字
    with open('css/gvm.svg') as f:
        svg_text = f.read()

    ret = re.findall(r'.*?<path id="(\d+?)" d="M0 (\d+?) H600"/>', svg_text)
    for id_, y_ in ret:
        if int(y_) >= int(y):
            find_id = id_
            break

    # <textPath xlink:href="#1" textLength="308">膝贫占欢掀舱恒给静相棵株猜由水先止赤则屯添叛</textPath>
    ret = re.search(r'.*?<textPath xlink:href="#%s" textLength="\d+?">(.+?)</textPath>' % find_id, svg_text)
    if ret:
        text = ret.groups()[0]
        # print(find_id, text)
        return text[int(x)//14]


if __name__ == '__main__':
    # download_css()
    # download_svg()
    css_dict = css2dict()
    # print(find_char(*css_dict['gvmzif']))
    print(find_char2(*css_dict['gvmoo4']))