# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest, Request


class ShaanxiSpider(scrapy.Spider):
    name = 'shaanxi2'
    allowed_domains = ['ccgp-shaanxi.gov.cn']
    # start_urls = ['http://ccgp-shaanxi.gov.cn/notice/noticeaframe.do?noticetype=3&province=province&isgovertment=']
    start_urls = ['http://ccgp-shaanxi.gov.cn/notice/list.do?noticetype=3&province=province']

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

        # 获取下一页数据
        if len(trs) == 15:
            yield Request(response.request.url,
                          meta={'next_page': True}, dont_filter=True)