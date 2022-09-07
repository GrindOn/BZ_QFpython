#!/usr/bin/python3
# coding: utf-8

from dao.base import BaseDao
from entity import Student


class StuDao(BaseDao):
    def query(self, where=None, args=None):
        ret = super(StuDao, self).query('Student', 'sn', 'name', 'sex', 'age',
                                        where=where, args=args)
        return [
            Student(item['sn'], item['name'], item['age'], item['sex'])
            for item in ret
        ]


if __name__ == '__main__':
    dao = StuDao()
    print(dao.query(where=' where sex=%(a)s', args={'a': '男'}))