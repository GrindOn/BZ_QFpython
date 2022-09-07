# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from csv import DictWriter
import os

import sys

from qidian.items import *
from qidian.db import BaseDao


class CSVPipeline(object):
    def __init__(self):
        self.book_csv = 'books.csv'
        self.seg_csv = 'segs.csv'
        self.seg_detail_csv = 'segs_detail.csv'
        self.cnt = 0

    def save_csv(self, item, filename):
        has_header = os.path.exists(filename)
        with open(filename, 'a') as f:
            writer = DictWriter(f, fieldnames=item.keys())
            if not has_header:
                writer.writeheader()

            writer.writerow(item)

    def process_item(self, item, spider):
        print('^'*40)
        if not item: return

        if isinstance(item, BookItem):
            self.save_csv(item, self.book_csv)

        elif isinstance(item, SegItem):
            self.save_csv(item, self.seg_csv)

        else:
            self.save_csv(item, self.seg_detail_csv)

        return item


class DBPipeline():
    def __init__(self):
        self.dao = BaseDao()
        self.book_table = 't_book'
        self.seg_table = 't_seg'
        self.seg_detail_table = 't_seg_detail'

    def process_item(self, item, spider):
        if isinstance(item, BookItem):
            item['tags'] = '/'.join(item['tags'])  # 将list转成字符串
            self.dao.save(self.book_table, **item)

        elif isinstance(item, SegItem):
            self.dao.save(self.seg_table, **item)

        else:
            self.dao.save(self.seg_detail_table, **item)

        return item

