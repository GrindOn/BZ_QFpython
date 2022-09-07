# Python爬虫第一课

本课讲解关于爬虫相关的知识点，包含以下内容:

- 什么是爬虫(Spider)
- 爬虫与Web后端服务之间的关系
- Python爬虫技术的相关库
- 常见反爬虫的策略
- 爬虫库urllib【重要】

## 一、什么是爬虫

### 1.1 爬虫Spider的概念

爬虫用于爬取数据， 又称之为**数据采集程序**。

爬取的数据来源于网络，网络中的数据可以是由**Web服务器**（Nginx/Apache）、数据库服务器(MySQL、Redis)、索引库（ElastichSearch）、大数据（Hbase/Hive）、视频/图片库(FTP)、云存储等(OSS)提供的。

爬取的数据是公开的、非盈利的。

### 1.2 Python爬虫

使用Python编写的爬虫脚本(程序)可以完成定时、定量、指定目标（Web站点）的数据爬取。主要使用多（单）线程/进程、网络请求库、数据解析、数据存储、任务调度等相关技术。

Python爬虫工程师，可以完成接口测试、功能性测试、性能测试和集成测试。

## 二、 爬虫与Web后端服务之间的关系

爬虫使用网络请求库，相当于客户端请求， Web后端服务根据请求响应数据。

爬虫即向Web服务器发起HTTP请求，正确地接收响应数据，然后根据数据的类型（Content-Type）进行数据的解析及存储。

爬虫程序在发起请求前，需要伪造浏览器（User-Agent指定请求头），然后再向服务器发起请求， 响应200的成功率高很多。

## 三、Python爬虫技术的相关库

网络请求：

- urllib
- requests / urllib3
- selenium(UI自动测试、动态js渲染)
- appium(手机App 的爬虫或UI测试)

数据解析：

- re正则
- xpath
- bs4
- json

数据存储:

- pymysql
- mongodb
- elasticsearch

多任务库：

- 多线程 (threading）、线程队列 queue
- 协程（asynio、 gevent/eventlet）

爬虫框架

- scrapy
- scrapy-redis 分布式（多机爬虫）

## 四、常见反爬虫的策略

- UA（User-Agent）策略
- 登录限制（Cookie）策略
- 请求频次（IP代理）策略
- 验证码（图片-云打码，文字或物件图片选择、滑块）策略
- 动态js（Selenium/Splash/api接口）策略

## 五、爬虫库urllib【重要】

### 5.1 urllib.request模块

#### 5.1.1 简单的请求

```python
from urllib.request import urlopen

# 发起网络请求
resp = urllopen('http://www.hao123.com')
assert resp.code == 200
print('请求成功')
# 保存请求的网页
# f 变量接收open()函数返回的对象的__enter__()返回结果
with open('a.html', 'wb') as f:
     f.write(resp.read())
```

urlopen(url, data=None)可以直接发起url的请求, 如果data不为空时，则默认是POST请求，反之为GET请求。

resp是http.client.HTTPResponse类对象。

#### 5.1.2 带请求头的请求

```python
from urllib.request import Request

def search_baidu():
    # 网络资源的接口(URL)
    url = 'https://www.baidu.com'

    # 生成请求对象，封装请求的url和头header
    request = Request(url,
                      headers={
                          'Cookie': 'BIDUPSID=16CECBB89822E3A2F26ECB8FC695AFE0; PSTM=1572182457; BAIDUID=16CECBB89822E3A2C554637A8C5F6E91:FG=1; BD_UPN=123253; H_PS_PSSID=1435_21084_30211_30283; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_645EC=6f7aTIObS%2BijtMmWgFQxMF6H%2FhK%2FcpddiytCBDrefRYyFX%2B%2BTpyRMZInx3E',
                          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
                      })

    response = urlopen(request)  # 发起请求

    assert response.code == 200
    print('请求成功')

    # 读取响应的数据
    bytes_ = response.read()
    
    # 将响应的数据写入文件中
    with open('index.html', 'wb') as file:
        file.write(bytes_)
```

<font color=red size=5>任务1：收集Http协议的报文头的哪些Key</font>

### 5.2 urllib.parse模块

此模块有两个核心的函数:

- quote() 仅对中文字符串进行url编码；
- urlencode() 可以针对一个字典中所有的values进行编码，然后转成key=value&key=value的字符串。

```python
"""
复杂的GET请求，多页面请求下载
"""
from urllib.request import Request, urlopen
from urllib.parse import urlencode

import ssl

import time

ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.baidu.com/s?'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    'Cookie': 'BIDUPSID=16CECBB89822E3A2F26ECB8FC695AFE0; PSTM=1572182457; BAIDUID=16CECBB89822E3A2C554637A8C5F6E91:FG=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1573184257; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; H_PS_PSSID=1435_21084_30211_30283; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; PSINO=1; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; APPGUIDE_8_2_2=1; yjs_js_security_passport=0927713bf2c240ca607108086d07729426db4dbb_1577084843_js; __yjsv5_shitong=1.0_7_c3620451e4363f4aed30cbe954abf8942810_300_1577084847314_223.255.14.197_2d7151e0; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D',
    'x-requested-with': 'XMLHttpRequest'
}

params = {
    'wd': '',
    'pn': 0  # 0, 10, 20, 30 ...  = (n-1)*10
}

def pages_get(wd):
    params['wd'] = wd
    for page in range(1, 101):
        params['pn'] = (page-1)*10

        page_url = url+urlencode(params)
        resp = urlopen(Request(page_url,
                               headers=headers))

        assert resp.code == 200
        file_name = 'baidu_pages/%s-%s.html' % (wd, page)
        with open(file_name, 'wb') as f:
            bytes_ = resp.read()
            f.write(bytes_)
            print(f'{file_name} 写入成功!')
            time.sleep(0.5)

    print('下载 %s 100页成功!' % wd)


if __name__ == '__main__':
    pages_get('Python3.6')
```





### 5.3 HTTP处理器

urllib的请求处理器，主要用于`urllib.request.build_opener()`函数参数，表示构造一个由不同处理组成的伪浏览器。

#### 5.3.1 HTTPHandler

处理Http协议的请求处理。

#### 5.3.2 HTTPCookieProcessor

处理Cookie的处理器，创建类实例时，需要提供`http.cookiejar.CookieJar`类的实例对象。

#### 5.3.3 ProxyHandler



## 六、时间规划及作业规范

### 6.1 时间规划

早 8: 30 - 9： 00 晨读

中午： 13：40 - 14： 00 分享

默写： 14：00 - 14： 10 

晚自习补课（1小时）：  周一、周三、 周五 

### 6.2 作业规范

每天晚12： 00 之间，作业发给 讲师、就业和班主任的邮箱，邮件标题： 2019-12-21-xpy1905班-张佳-爬虫第一天作业

邮件正文： 

```
Disen, 您好！
   今天的作业已完成90%， 遇到如下问题：
   1. urllib库的知识点太多，需要多记，多练习！
   2. baidu.com网页的反爬太强，需要3个小时间爬虫10页数据
   
   [代码截图1]
   [结果截图1]
   
   详细请看附件， 谢谢！
```

邮件：  610039018@qq.com





## 七、中午默写

- 写出Python上下文的两个核心函数

  ```python
  __enter__(self)
  __exit__(self, except_type, except_value, except_tb)
  ```

  

- 写出正则中的(), [] , {} 三个符号的作用

  ```
  ( ) 用于分组的符号
  [ ] 指定匹配字符的范围，如 [a-c_B-F]
  { } 指定匹配的长度(量词表示)
  ```

  

- 写出pymysql.Connect()连接数据库的核心参数

  ```python
  Connect(host,
  				port=3306,
          user,
          password,
          db,
          charset)
  ```

  



## 八、作业

- 豆瓣动作电影排行榜
- 肯德基店铺位置

