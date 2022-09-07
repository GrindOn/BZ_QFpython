from random import randint

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from App.models import User
from App02.models import Publisher, Book, Student, Archives


def index(request):
    #创建一个出版社
    # pub = Publisher(pname="机械工业出版社")
    # pub.save()
    # 创建图书
    # book = Book(bname="五军之战")
    # book.save()

    # 把图书所属的出版社赋值
    # book = Book.objects.get(pk=3)
    # pub = Publisher.objects.get(pk=2)
    # book.pub = pub  # pub必须是出版社对象
    # book.save()

    # 通过出版社管理图书
    # pub = Publisher.objects.get(pk=3)
    #增加图书
    # pub.books.create(bname='地上大蝙蝠')

    # 级联删除
    # pub = Publisher.objects.get(pk=3)
    # pub.delete()

    # 更新
    # pub = Publisher.objects.get(pk=2)
    # pub.books.update(bname="特不靠谱")

    # book = Book.objects.get(pk=3)
    # book.pub.pname = '五道口职业技术学院'
    # book.pub.save()
    # print(book.pub)

    # 查询
    # pub = Publisher.objects.get(pk=2)
    # # pub.books是一个查询管理器对象 = objects
    # print(pub.books.all())
    # # 由图书查出版社
    # book = Book.objects.get(pk=3)
    # print(book.pub.pname)

    # 复杂查询
    # pub = Publisher.objects.filter(books__bname='特不靠谱')
    # pub = Publisher.objects.filter(books__id=3)
    # print(pub[0].pname)

    return HttpResponse("ok")


def one2one(request):
    student = Student.objects.get(pk='002')
    print(student.sname)
    # 查档案
    print(student.archive)
    # 看学生信息
    arc = Archives.objects.get(pk=1)
    print(arc.student.sno)
    return HttpResponse("one2one")


def send_sms(request):
    from App02.SMS import sms
    # 模板参数一定要是这个格式
    # 一定要注意模板变量number
    para = "{'number':%d}"%(randint(1000,100000))
    print(para)
    res = sms.send('15116905290',para)
    print(res.decode("utf-8"))
    return HttpResponse("ok")


def fenye(request,page=1):
    users = User.objects.all()
    # 产生分页器
    paginator = Paginator(users,10)
    # 分页对象
    # page表示当前页
    pager = paginator.page(page)
    for user in paginator.object_list:
        print(user,type(user))
    return render(request,"userlist.html",locals())