# -*- coding: utf-8 -*-
import scrapy


class AllQySpider(scrapy.Spider):
    name = 'all_qy'
    allowed_domains = ['qichacha.com']
    start_urls = ['http://qichacha.com/']

    def parse(self, response):
        pass
