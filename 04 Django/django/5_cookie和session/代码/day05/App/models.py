# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.db.models import Manager


# 扩展Manager管理器功能
class MyManager(Manager):
    # 获取结果集，
    def get_queryset(self):
        # 获取查询结果集
        # data =
        # 把sex不为空显示出来
        # data = filter(sex__isnull=True)
        return super().get_queryset().filter(sex__isnull=False)

    def after(self, date):
        data = User.objects.filter(regtime__gt=date)
        return data



class Detail(models.Model):
    did = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detail'

class User(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=30)
    password = models.CharField(max_length=128)
    regtime = models.DateTimeField()
    sex = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'

    def __str__(self):
        return self.username + str(self.uid)
    # 可以自定义
    objects = Manager()  # 系统管理器
    user_manager = Manager()  #自定义管理器
    sex_manager = MyManager()

    @classmethod
    def after(cls,date):
        return cls.user_manager.filter(regtime__gt=date)

    @classmethod
    def get_sexes(cls):
        return cls.objects.filter(sex__isnull=False)