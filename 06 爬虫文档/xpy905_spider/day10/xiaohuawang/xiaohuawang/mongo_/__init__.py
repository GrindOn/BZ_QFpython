#!/usr/bin/python3
# coding: utf-8
from pymongo import MongoClient

_client = MongoClient('119.3.170.97', 27017)
db = _client.xiaohua  # 打开或创建xiaohua库
