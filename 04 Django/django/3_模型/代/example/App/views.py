from random import randint

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App.models import User


def handle_data(request):
    # 增加记录
    # user = User(username='tom',password='123')
    # user.save()
    # 便利方法
    # user = {'username':'tom1','password':'33334'}
    # User.objects.create(**user)

    # 批量创建
    # first = ["张","李","赵","周","吴","郑","王"]
    # lastname = ['三','春花','翠花','卫国','二狗']
    # users = []
    # for name in range(100):
    #     username = first[randint(0,6)] + lastname[randint(0,4)]+str(randint(0,10000))
    #     users.append(User(username=username,password=str(randint(11111,999999))))
    # User.objects.bulk_create(users)
    # User.objects.bulk_create([User(username='test1'),User(username='test2')])


    #修改
    # user = User.objects.get(pk=1)
    # user.password = '3333'
    # user.save()

    #删除
    # pk表示主键
    # try:
    #     user = User.objects.get(uid=1)
    #     print(user,type(user))
    #     if user:
    #         user.delete()
    # except Exception as e:
    #     print(e)
    #删除多条记录
    # users = User.objects.filter(uid__gte=2)
    # print(users)
    # users.delete()


    return HttpResponse("增删改")


def find_data(request):
    # all 过滤器 查询所有数据
    # users = User.objects.all()
    # print(data)

    #filter 过滤器  where
    # select * from user where uid=5
    # users = User.objects.filter(uid=5)
    # select * from user where uid>5
    # 过滤器可以串联调用
    users = User.objects.filter(uid__gt=5).filter(uid__lt=50)
    print(users)
    # return HttpResponse("query")
    return render(request,'list.html',locals())