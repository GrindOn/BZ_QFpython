"""
基于requests库作用实现网络请求
基于xpath实现数据提取
"""
import requests
from lxml import etree


class RequestError(Exception):
    """
    请求异常
    """
    pass


class ParseError(Exception):
    """
    解析异常
    """
    pass


def get(url):
    resp = requests.get(url,
                        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'},
                        proxies={'http': 'http://49.77.208.198:9999'})
    if resp.status_code == 200:
        parse(resp.text)
    else:
        raise RequestError('请求失败!')


def parse(html):
    # 使用xpath解析
    root = etree.HTML(html)  # Element元素对象
    divs = root.xpath('//div[@class="li-itemmod"]')  # List[<Element>, <Element>,...]
    print(divs)
    for div in divs:
        # cover_url = div.xpath('.//img/@src')  # list['', ]
        # 提取src的属性值
        cover_url = div.xpath('.//img/@src')[0]  # list['', ]
        title = div.xpath('.//h3/a/text()')[0]

        print(cover_url, title)



if __name__ == '__main__':
    get('https://shanghai.anjuke.com/community/?from=navigation')
