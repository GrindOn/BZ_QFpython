#!/usr/bin/python3
# coding: utf-8


class Student:
    def __init__(self, sn, name, age, sex):
        self.sn = sn
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self):
        return "%s->%s(%s) " % (self.sn, self.name, self.sex)

    def __repr__(self):
        return self.__str__()