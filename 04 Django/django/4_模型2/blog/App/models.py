import re

from django.db import models

# Create your models here.


class Article(models.Model):
    aid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    intro = models.CharField(max_length=100,null=True)
    content = models.CharField(max_length=10000, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    cid = models.ForeignKey('Category', models.DO_NOTHING, db_column='cid',related_name='articles', null=True)
    hits = models.IntegerField(blank=True, null=True)
    comments = models.IntegerField(blank=True, null=True)
    photo = models.CharField(max_length=300, blank=True, null=True,db_column='picture')

    class Meta:
        managed = False
        db_table = 'article'

    @classmethod
    def add(cls, **kwargs):
        cid = kwargs.pop('cid')
        tag = kwargs.pop('tag')
        obj = cls(**kwargs)
        obj.cid = Category.objects.get(pk=cid)
        obj.save()
        tags = re.split(r'[, ]+',tag)
        Tag.add(obj,tags)

        return obj

class Category(models.Model):
    cid = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)
    num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'

    @classmethod
    def first_category(cls):
        return cls.objects.first()




class Mark(models.Model):
    mid = models.AutoField(primary_key=True)
    content = models.CharField(max_length=1000, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    uid = models.ForeignKey('User', models.DO_NOTHING, db_column='uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mark'


class Tag(models.Model):
    tid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    aid = models.ForeignKey(Article, models.DO_NOTHING, db_column='aid', related_name='tags', null=True)

    class Meta:
        managed = False
        db_table = 'tag'

    @classmethod
    def add(cls,article,tags):
        if len(tags) > 0:
            for t in tags:
                tag = Tag(name=t)
                tag.aid = article
                tag.save()


class User(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=30)
    password = models.CharField(max_length=128)
    phone = models.CharField(max_length=11, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    portrait = models.CharField(max_length=300, blank=True, null=True)
    regtime = models.DateTimeField(blank=True, null=True)
    isforbid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'