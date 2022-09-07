#!/usr/bin/env python
# encoding: utf-8
'''
@desc:    
@author:  
@contact: 
@file: utils.py
@time: 2020/3/17 11:42 上午
'''
import os
from datetime import datetime
from random import randint


class FileUpload:
    def __init__(self, file, exts=('png','jpg','jpeg'), size=1024*1024,is_randomname=False):
        """
        :param file: 文件上传对象
        :param exts: 文件类型
        :param size: 文件大小，默认1M
        :param is_randomname: 是否是随机文件名，默认是否
        """
        self.file = file
        self.exts = exts
        self.size = size
        self.is_randomname = is_randomname

    #文件上传
    def upload(self,dest):
        """

        :param dest: 文件上传的目标目录
        :return:
        """
        #1 判断文件类型是否匹配
        if not self.check_type():
            return -1
        #2 判断文件大小是否符合要求
        if not self.check_size():
            return -2
        #3 如果是随机文件名，要生成随机文件名
        if self.is_randomname:
            self.file_name = self.random_filename()
        else:
            self.file_name = self.file.name
        #4 拼接目标文件路径
        path = os.path.join(dest,self.file_name)
        #5 保存文件
        self.write_file(path)
        return 1

    def check_type(self):
        ext = os.path.splitext(self.file.name)
        if len(ext) > 1:
            ext = ext[1].lstrip('.')
            if ext in self.exts:
                return True
        return False

    def check_size(self):
        if self.size < 0:
            return False
        #如果文件大小于给定大小，返回True，否则返回False
        return self.file.size <= self.size

    def random_filename(self):
        filename = datetime.now().strftime("%Y%m%d%H%M%S")+str(randint(1,10000))
        ext = os.path.splitext(self.file.name)
        #获取文件后缀
        ext = ext[1] if len(ext)>1 else ''
        filename += ext
        return  filename

    def write_file(self,path):
        with open(path,'wb') as fp:
            if self.file.multiple_chunks():
                for chunk in self.file.chunks():
                    fp.write(chunk)
            else:
                fp.write(self.file.read())