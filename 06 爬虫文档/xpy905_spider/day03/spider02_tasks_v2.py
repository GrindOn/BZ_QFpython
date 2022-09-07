"""
基于进程+线程实现多任务的爬虫程序
"""
import time
import uuid
from multiprocessing import Queue, Process
from threading import Thread
from queue import Queue as TQueue

import requests
from lxml import etree

from utils.header import get_ua

headers = {
    'User-Agent': get_ua()
}


class DownloadThread(Thread):
    def __init__(self, task_queue, result_queue):
        super().__init__()
        self.task_queue: TQueue = task_queue  # 线程队列
        self.result_queue: Queue = result_queue  # 进程队列

    def run(self):
        while True:
            try:
                url = self.task_queue.get(timeout=10)
                content = self.get(url)
                self.result_queue.put((url, content))
            except:
                break

    def get(self, url):
        print('开始下载', url)
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            resp.encoding = 'utf-8'

        print(url, '下载完成')
        return resp.text


class DownloadProcess(Process):
    """
    下载进程
    """

    def __init__(self, url_q, html_q):
        self.url_q: Queue = url_q
        self.html_q = html_q
        super().__init__()

        # 用户于进程内部的多个线程之间的通信队列
        self.task_queue = TQueue()

    def run(self):
        # 启动子线程下载任务
        ts = [DownloadThread(self.task_queue, self.html_q)
              for i in range(2)]

        for t in ts:
            t.start()

        while True:
            try:
                url = self.url_q.get(timeout=30) # 主进程，用于进程间通信
                self.task_queue.put(url)  # 当前进程， 用于线程间通信
            except:
                break

        for t in ts:
            t.join()
        print('--下载进程 Over--')


class ParseThread(Thread):
    def __init__(self, html, url_q, parent_url):
        self.html = html
        self.parent_url = parent_url
        self.url_q = url_q

        super(ParseThread, self).__init__()

    def run(self):
        root = etree.HTML(self.html)
        imgs = root.xpath('//div[contains(@class, "picblock")]//img')

        for img in imgs:
            item = {}
            item['id'] = uuid.uuid4().hex
            item['name'] = img.xpath('./@alt')[0]
            try:
                item['cover'] = img.xpath('./@src2')[0]
            except:
                item['cover'] = img.xpath('./@src')[0]
            print(item)
            # 将item数据写入到ES索引库中

        # 获取下一页的连接
        next_page = root.xpath('//a[@class="nextpage"]/@href')
        if next_page:
            next_url = self.parent_url + next_page[0]
            self.url_q.put(next_url)  # 将新的下载任务添加到下载队列中


class ParseProcess(Process):
    # 解析进程
    def __init__(self, url_q, html_q):
        self.url_q = url_q
        self.html_q = html_q
        super(ParseProcess, self).__init__()

    def run(self):
        while True:
            try:
                url, html = self.html_q.get(timeout=60)
                print('开始解析', url)
                parent_url = url[:url.rindex('/') + 1]

                # 启动解析线程
                ParseThread(html, self.url_q, parent_url).start()
                
            except:
                break

        print('解析进程Over')


if __name__ == '__main__':
    task1 = Queue()  # 下载任务队列
    task2 = Queue()  # 解析任务队列

    # 起始爬虫任务
    task1.put('http://sc.chinaz.com/tupian/shuaigetupian.html')

    p1 = DownloadProcess(task1, task2)
    p2 = ParseProcess(task1, task2)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('---over----')
