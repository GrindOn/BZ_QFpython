# -*- coding: utf-8 -*-
import uuid

import scrapy
from scrapy.http import Response, HtmlResponse, Request
from scrapy.selector import SelectorList, Selector

from qidian.items import *

class WanbenSpider(scrapy.Spider):
    name = 'wanben'
    allowed_domains = ['qidian.com']
    start_urls = ['https://www.qidian.com/finish']

    def parse(self, response: Response):
        if response.status == 200:
            # 解析数据
            lis = response.css('.all-img-list li')  # SelectorList

            for li in lis:
                item = BookItem()
                item['book_id'] = uuid.uuid4().hex

                # li 对象类型是Selector , 注意： Selector没有x()函数
                a = li.xpath('./div[1]/a')

                item['book_url'] = a.xpath('./@href').get()
                item['book_cover'] = a.xpath('./img/@src').get()

                item['book_name'] = li.xpath('./div[2]/h4//text()').get()

                item['author'], *item['tags'] = li.css('.author a::text').extract()
                item['summary'] = li.css('.intro::text').get()

                yield item
                # 请求小说的详情
                yield Request('https://' + item['book_url'],
                              callback=self.parse_info, priority=10,
                              meta={'book_id': item['book_id']})


            # 获取下一页的连接
            next_url = response.css('.lbf-pagination-item-list').xpath('./li[last()]/a/@href').get()
            if next_url.find('javascript') == -1:  # 存在下一页
                yield Request('https:'+next_url, priority=100)  # 优先级值越高，会优先下载

    def parse_info(self, response:Response):
        book_id = response.meta['book_id']

        seg_as = response.xpath('//div[@class="volume-wrap"]/div[position()>1]').css('.cf li>a')
        for a in seg_as:
            # a-> Selector

            item = SegItem()
            item['seg_id'] = uuid.uuid4().hex
            item['book_id'] = book_id
            item['title'] = a.css('::text').get()
            item['url'] = 'https:' + a.xpath('./@href').get()

            yield item

            # 下载章节内容
            yield Request(item['url'],
                          callback=self.parse_seg,
                          priority=1,
                          meta={'seg_id': item['seg_id']})

    def parse_seg(self, response):
        """章节内容"""
        item = SegDetailItem()
        item['seg_id'] = response.meta['seg_id']
        contents = ''.join(response.css('.read-content p::text').extract())
        item['content'] = contents.replace('\u3000', '').replace('\n','')

        yield item







