# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class QySpider(CrawlSpider):
    name = 'qy'
    allowed_domains = ['qichacha.com']
    start_urls = ['https://www.qichacha.com/g_AH.html']

    rules = (
        Rule(LinkExtractor(allow=r'g_[A-Z]{2,}\.html',
                           deny=r'g_[A-Z]{2,}_\d+\.html'),
             callback='parse_item', follow=False),

        Rule(LinkExtractor(restrict_css='.pagination'),
             'parse_item', follow=True),

        Rule(LinkExtractor(r'/firm_\w+?\.html'), 'parse_detail', follow=False)
    )

    def parse_item(self, response):

        trs = response.css('.m_srchList tr')
        for tr in trs:
            item = {}
            item['cover']=tr.xpath('./td[1]/img/@src').get()
            item['name'] = tr.xpath('./td[2]/a/text()').get()

            yield item

    def parse_detail(self, response):
        pass
