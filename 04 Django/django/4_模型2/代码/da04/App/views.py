from django.db.models import Q, F
from django.http import HttpResponse
from django.shortcuts import render
from App.models import User

# Create your views here.
def process_data(request):
    # 创建一个对象
    # user = User()
    # user.username = '大侠'
    # user.password = '就是不告诉你密码'
    # user.save()

    # 修改
    # user = User.objects.get(uid=7)
    #     # print(user)
    #     # user.password = '你猜'
    #     # user.save()

    # 删除
    # user = User.objects.get(uid=5)
    # user.delete()

    # 查询结果集QuerySet
    #1 all
    # select * from user
    # data = User.objects.all()

    # print(data)
    # 获取一条，从结果集中取一条
    # data = data.first()

    # filter 过滤结果集
    # data = User.objects.all()
    # # select * from user where uid < 20
    # data = data.filter(uid__lt=20)  # uid < 20
    # data = data.filter(uid__gt=10)
    # print(data)

    # 排序
    # 按username升序排列
    # data = User.objects.order_by('username')
    # for user in data:
    #     print(user.username)

    # 限制结果集  不能用负的下标
    # 切片 取前两条记录
    # data = User.objects.order_by('username')[:2]
    # 从下标为4记录到下标为9的记录
    # data = User.objects.order_by('uid')[4:10]
    # print(data)

    # values 指定字段
    data = User.objects.all().values('username')
    # print(data)
    # for user in data: # user是字典
    #     print(user['username'])

    # 去重  distinct
    # data = User.objects.all().values("password").distinct()[:10]
    # data = User.objects.values("password").distinct()[:10]
    # print(data)

    # 反序
    # data = User.objects.order_by('uid').reverse()
    # print(data)

    return HttpResponse("CURD")


def process_query(request):
    # 非过滤器方法
    # get只能返回一条记录
    # 如果记录不存在：DoesNotExist
    # 如果多于一条记录: MultipleObjectsReturned
    # user = User.objects.get(uid__gt=1)
    # print("111")
    # print(user)

    # 2 first 返回一个模型对象
    # user = User.objects.first()
    # print(user)

    # 3 last最后一条记录
    # user = User.objects.last()
    # print(user)

    #4 结果集中的记录数: 必须是QuerySet才能调用count
    # num = User.objects.filter(uid__lt=10).count()
    # print(num)

    # 5 判断结果集是否为空
    # flag = User.objects.all().exists()
    # flag = User.objects.filter(uid__lt=5).exists()
    # print(flag)


    return HttpResponse("query")

# 查询条件的写法
def process_filter(request):
    # 关系运算
    """

    >=     uid__gte=2  uid>=2
    >      uid__gt=2   uid>2
    <      uid__lt=2   uid<2
    <=     uid__lte=2  uid<=2
    ==       uid=2     uid==2  判等
    """
    # filter中多个条件做逻辑与连接
    # data = User.objects.filter(uid__lt=20)
    # uid >=10 and uid < 20
    # data = User.objects.filter(uid__lt=20,uid__gte=10)
    # print(data)

    # in 集合运算
    # data = User.objects.filter(uid__in=[9,12,50])
    # print(data)

    # is null 判断空
    # data = User.objects.filter(sex__isnull=True)
    # data = User.objects.exclude(sex__isnull=True)
    # print(data)

    # 字符串操作
    # startwith 以...开头
    # data = User.objects.filter(username__startswith='张')
    # username__endswith 以..结尾
    # data = User.objects.filter(username__endswith='1')
    # username__contains 包含
    # data = User.objects.filter(username__contains='1')
    # for user in data:
    #     print(user)

    # regex正则匹配
    # print(1111)
    # data = User.objects.filter(username__regex=r'3$')
    # for user in data:
    #     print(user)

    # 日期查询
    # data = User.objects.filter(regtime__year=2020)
    data = User.objects.filter(regtime="2020-03-11")
    print(data)

    return HttpResponse("查询条件的写法")


def handle_group(request):
    from django.db.models import Max,Min,Avg,Sum,Count
    # 统计函数用法
    # select max(uid) from user
    # uid = User.objects.aggregate(Max('uid'))
    # print(uid,type(uid))

    # 分组
    # select sex,count(uid) from user group by sex
    # data = User.objects.values('sex').annotate(Count('uid'))
    # select sex,count(uid) from user group by sex having sex=1
    # data = User.objects.values('sex').annotate(Count('uid')).filter(sex=1)

    # Q对象：构造逻辑或、逻辑非
    # 查询uid>30或者sex=1

    # data = User.objects.filter(Q(uid__gt=30)|Q(sex=1))  # | 逻辑或

    # data = User.objects.filter(~Q(uid__gt=30))  # | 逻辑非
    # data = User.objects.filter(~Q(sex=1))  # 不能处理null

    # print(data)
    #
    # for user in data:
    #     print(user)

    # F对象: 把sex看成User的一个列名
    # data = User.objects.filter(uid=F('sex'))


    # print(data)


    return HttpResponse("group")


def handle_sql(request):
    # 原生sql
    # 返回一个RawQuerySet
    # data = User.objects.raw("select * from user")
    # print(list(data)) # [obj1,obj2]

    # 多表联合查询
    # data = User.objects.raw("select * from user ,detail where user.uid =detail.uid;")
    # print(list(data))


    tmp =  input("用户名：")
    # sdkjfksjdf' or '1
    # users = User.objects.raw("select * from user where username='{}'".format(tmp))

    # 防止sql注入
    users = User.objects.raw("select * from user where username=%s", ["'sddfsdf' or '1'"])
    print(list(users),type(users))
    return HttpResponse("原生sql")