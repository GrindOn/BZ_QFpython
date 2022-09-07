# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest


class ShaanxiSpider(scrapy.Spider):
    name = 'shaanxi'
    allowed_domains = ['ccgp-shaanxi.gov.cn']

    def start_requests(self):
        self.url = 'http://ccgp-shaanxi.gov.cn/notice/noticeaframe.do?noticetype=3&province=province&isgovertment='
        self.data = {
            'page.pageNum': '1'
        }
        self.MAX_PAGE = 1399
        yield FormRequest(self.url, formdata=self.data)

    def parse(self, response):
        trs = response.css('.list-box tbody tr')
        for tr in trs:
            item = {}
            item['id'] = tr.xpath('./td[1]/text()').get()
            item['area'] = tr.xpath('./td[2]/text()').get()
            item['title'] = tr.xpath('./td[3]/a/text()').get()
            item['url'] = tr.xpath('./td[3]/a/@href').get()
            item['date'] = tr.xpath('./td[4]/text()').get()

            yield item

        # 尝试获取最大的页数
        pages = response.css('.pagination').xpath('./li[last()-2]/a/text()').get()
        print('*' * 20, pages, '*' * 20)
        try:
            if all((
                    pages,
                    int(pages) > self.MAX_PAGE
            )):
                self.MAX_PAGE = int(pages)
        except:
            pass

        if int(self.data['page.pageNum']) >= self.MAX_PAGE: return
        self.data['page.pageNum'] = str(int(self.data['page.pageNum']) + 1)

        yield FormRequest(self.url, formdata=self.data)
