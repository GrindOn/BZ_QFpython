# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models




class Bookinfo(models.Model):

    btitle = models.CharField(max_length=200)
    bpub_date = models.DateField(blank=True, null=True)
    bread = models.IntegerField()
    bcomment = models.IntegerField()
    bimage = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bookinfo'


class Heroinfo(models.Model):
    hid = models.AutoField(primary_key=True)
    hname = models.CharField(max_length=50)
    book = models.ForeignKey(Bookinfo, models.CASCADE, db_column='bid', blank=True, null=True,related_name='heros')

    class Meta:
        managed = False
        db_table = 'heroinfo'

    def __str__(self):
        return self.hname


class User(models.Model):
    username = models.CharField(unique=True, max_length=150)
    password = models.CharField(max_length=128)
    usertype = models.IntegerField()
    email = models.CharField(max_length=254, blank=True, null=True)
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user'
