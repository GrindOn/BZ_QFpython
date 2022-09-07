from django.db import models

# Create your models here.
# class BaseModel(models.Model):
#     create_time = models.DateTimeField(auto_now_add=True)
#     class Meta:
#         abstract = True

class User(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30,null=False)
    password = models.CharField(max_length=128,null=False)
    regtime = models.DateTimeField(auto_now=True)
    sex = models.IntegerField()

    def __str__(self):
        return self.username+":"+ str(self.uid)

    class Meta:
        db_table = 'user'

class Detail(models.Model):
    did = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=30)
    uid = models.IntegerField()

    class Meta:
        db_table = 'detail'