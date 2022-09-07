from django.db import models

# Create your models here.

class Detail(models.Model):
    did = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    uid = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'detail'

class User(models.Model):
    uid = models.AutoField(primary_key=True)
    # verbose_name 后台管理中显示中文
    username = models.CharField(unique=True, max_length=30,verbose_name='用户名')
    password = models.CharField(max_length=128,verbose_name='密码')
    regtime = models.DateTimeField()
    ssex = models.IntegerField(blank=True, null=True,db_column='sex')

    class Meta:
        db_table = 'user'
        verbose_name = '用户表'

    def __str__(self):
        return self.username + str(self.uid)

    def sex(self):
        if self.ssex:
            return '男'
        else:
            return '女'
