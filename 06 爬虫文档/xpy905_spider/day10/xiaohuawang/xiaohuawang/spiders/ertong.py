# -*- coding: utf-8 -*-
import uuid

import scrapy
from scrapy import Request


class ErtongSpider(scrapy.Spider):
    name = 'ertong'
    allowed_domains = ['gbfzh.com']
    start_urls = ['https://www.gbfzh.com/ertong/']

    def parse(self, response):
        for li in response.css('#chan_newsDetail li'):
            type_name = li.xpath('./b/a/text()').get()
            url, title = li.xpath('./a/@href | ./a/text()').extract()

            yield Request(response.urljoin(url),
                          meta={'type_name': type_name,
                                'title': title},
                          headers={'Referer': response.url},
                          callback=self.parse_item)

        # 下一页
        next_url = response.css('.page_list').xpath('./li[last()-2]/a/@href').get()
        yield Request(response.urljoin(next_url),
                      headers={'Referer': response.url})

    def parse_item(self, response):
        content = response.css('#chan_newsDetail p::text').extract()

        item = {}

        item['_id'] = uuid.uuid4().hex
        item['type_name'] = response.meta['type_name']
        item['title'] = response.meta['title']
        item['content'] = content

        yield item
