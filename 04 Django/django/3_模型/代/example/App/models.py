from django.db import models

# Create your models here.
# 自定义模型必须继承Model
class User(models.Model):
    # 字段名：不能是python的关键字；不能使用连续的下划线;
    #db_column:数据库表中的字段名称
    uid = models.AutoField(primary_key=True)
    # CharField类型必须指明长度max_length
    username = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=128)
    regtime = models.DateTimeField(auto_now_add=True)

    class Meta: # 元数据,模型本身的信息
        #默认表名：应用名_模型名
        db_table = 'user'  # 表名
        ordering = ['username']  # 排序


