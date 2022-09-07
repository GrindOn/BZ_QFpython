# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class BaseMode(models.Model):
    class Meta:
        abstract = True


class Book(BaseMode):
    id = models.AutoField(primary_key=True)
    bname = models.CharField(max_length=200, blank=True, null=True)
    # ForeignKey第一个参数：参照的模型名
    # on_delete CASCADE级联删除
    # db_column  表中字段名
    # related_name 从出版社查询图书引用的名字
    pub = models.ForeignKey('Publisher', on_delete=models.CASCADE, related_name="books", db_column='pid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book'


class Publisher(models.Model):
    pname = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'publisher'


class Student(models.Model):
    sno = models.CharField(primary_key=True, max_length=6)
    sname = models.CharField(max_length=100)
    ssex = models.CharField(max_length=2, blank=True, null=True)
    sage = models.IntegerField(blank=True, null=True)
    sclass = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'
        # abstract = True  # 父类不生成表

class Archives(models.Model):
    idcard = models.CharField(unique=True, max_length=18)
    address = models.CharField(max_length=200, blank=True, null=True)
    student = models.OneToOneField('Student', models.CASCADE, unique=True, related_name='archive')

    class Meta:
        managed = False
        db_table = 'archives'

class Graduate(Student):
    # 如果父类是抽象的，子类会获取到父类所有属性，生成表
    age = models.IntegerField()
