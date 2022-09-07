from django.db.models import Count, Q
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App.models import User


def index(request):
    #字段查询
    # users = User.objects.filter(username__contains='1',uid__lt=30)
    # users = User.objects.filter(uid__range=[10,20])

    # 嵌套查询，data只能返回一个字段
    # data = User.objects.filter(uid__gt=15,uid__lt=20).values('uid')
    # users = User.objects.filter(uid__in = data)

    #select count('uid') from user
    # users = User.objects.aggregate(Count('uid'))
    # select sex,count('sex') form user group by sex
    # users = User.objects.values('sex').annotate(Count('sex'))

    # Q
    # users = User.objects.filter(Q(uid__gt=10)&Q(uid__lt=20))
    # users = User.objects.filter(Q(uid__gt=10)|Q(uid__lt=20))

    # for user in users:
    #     print(user)
    # print(users)

    # 原始sql查询
    # 可以执行任何sql语句和user无关，
    # 查询结果必须包含主键列
    # data = User.objects.raw("select * from detail")
    username = "oireiot' or '1"
    # sql = "select * from user where username='{}'".format(username)
    # 防止sql注入
    sql = "select * from user where username=%s"
    # sql = "select count(*) from user"
    # print(sql)
    # data = User.objects.raw(sql,[username])

    # data = User.objects.raw("select count(*) from user")

    # print(list(data))
    # print(data.__dict__)

    # for value in data:
    #     print(value,type(value))
    # from App.tools import query

    # data = query("select * from user")
    #带参数
    # data = query("select * from user where uid=%s",10)
    # print(data)
    return HttpResponse("ok")


def manage(request):
    # 使用自定义管理器查询
    # data = User.user_manager.all()
    # data = User.sex_manager.all()
    # print(data)
    # for user in data:
    #     print(user.sex)

    # 调用自己的类方法
    # data = User.after('2020-03-11')
    # print(data)

    # 调用管理器的方法sex_manager
    data = User.sex_manager.after('2020-03-11')
    print(data)

    return HttpResponse("自定义管理器")