# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request

class DushuPipeline(object):
    def process_item(self, item, spider):
        return item


class BookImagesPipeline(ImagesPipeline):
    DEFAULT_IMAGES_URLS_FIELD = 'cover'
    DEFAULT_IMAGES_RESULT_FIELD = 'path'

    def get_media_requests(self, item, info):
        # 如果一本书只有一张图片时
        return Request(item.get('cover'), meta={'book_name': item['name']})

        # return [
        #     Request(url)
        #     for url in item[self.DEFAULT_IMAGES_URLS_FIELD]
        # ]

    def file_path(self, request, response=None, info=None):
        # 返回是图片的路径
        name = request.meta['book_name'].replace('/', '_')

        return f'{name}.jpg'

    def item_completed(self, results, item, info):
        item['path'] = [v['path'] for k, v  in results if k]

        return item