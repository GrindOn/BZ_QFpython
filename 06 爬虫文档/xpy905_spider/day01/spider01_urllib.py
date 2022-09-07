"""
  初次使用urllib实现爬虫的数据请求
  urllib.request.urlopen(url) 发起get请求
  urllib.parse.quote() 将中文进行url编码
  urllib.request.urlretrieve(url, filename) 下载url保存到filename
"""

from urllib.request import urlopen, urlretrieve, Request
from urllib.parse import quote

import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def search_baidu(wd='千锋'):
    # 网络资源的接口(URL)
    url = 'https://www.baidu.com/s?wd=%s'

    # 生成请求对象，封装请求的url和头header
    request = Request(url % quote(wd),
                      headers={
                          'Cookie': 'BIDUPSID=16CECBB89822E3A2F26ECB8FC695AFE0; PSTM=1572182457; BAIDUID=16CECBB89822E3A2C554637A8C5F6E91:FG=1; BD_UPN=123253; H_PS_PSSID=1435_21084_30211_30283; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_645EC=6f7aTIObS%2BijtMmWgFQxMF6H%2FhK%2FcpddiytCBDrefRYyFX%2B%2BTpyRMZInx3E',
                          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, '
                                        'like Gecko) Chrome/79.0.3945.88 Safari/537.36'
                      })

    response = urlopen(request)  # 发起请求

    assert response.code == 200
    print('请求成功')

    # 读取响应的数据
    bytes_ = response.read()

    # ?? 当对象进入上下文时，调用对象的哪个方法
    # ?? 当对象退出上下文时，调用对象的哪个方法
    with open('%s.html' % wd, 'wb') as file:
        file.write(bytes_)


def download_img(url):
    # 从url中获取文件名
    filename = url[url.rfind('/') + 1:]
    req = Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, '
                      'like Gecko) Chrome/79.0.3945.88 Safari/537.36'

    })
    # urlretrieve(url, filename)
    resp = urlopen(req)
    with open(filename, 'wb') as file:
        file.write(resp.read())

    print(f'下载 {filename} ok!')


if __name__ == '__main__':
    # search_baidu()
    download_img('https://extraimage.net/images/2019/12/21/c3aacc41cd8c6ab7b905aba8ddee62a9.jpg')
    # download_img('https://www.ygdy8.com/html/gndy/dyzz/20191222/59523.html')
