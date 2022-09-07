from datetime import datetime, timedelta

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from App.models import User

# 装饰器，路由保护
def check_login(func):
    def inner(*args,**kwargs):
        print(args,kwargs)
        if args[0].COOKIES.get('username'):
            return func(*args,**kwargs)
        else:
            return redirect('/user/login/')
        # return func(*args,**kwargs)
    return inner



def login(request):
    if request.method == "POST":
        userinfo = request.POST.dict()
        userinfo.pop("csrfmiddlewaretoken")
        print(userinfo)
        user = User.objects.filter(**userinfo).first()
        user = User.objects.filter(username=userinfo.get('username'),password=userinfo.get('password')).first()
        if user:
            response = redirect('/user/')
            # cookie
            # # 三天以后过期
            # future = datetime.now() + timedelta(days=3)
            # # 将cookie协会客户端
            # response.set_cookie('username',user.username,expires=future)

            # session
            request.session['username'] = user.username
            request.session['uid'] = user.uid


            return response
        # print(user.__query)


    return render(request,"app03/login.html")


def home(request):
    # 获取cookies 中指定键值对
    # username = request.COOKIES.get('username')

    #获取session
    username = request.session.get('username')
    uid = request.session.get('uid')
    print(uid)
    return render(request,'app03/index.html',locals())




def logout(request):
    res = redirect('/user/')
    # 删除cookie
    # res.delete_cookie("username")

    # 清楚session
    # request.session.clear() # 清除所有session键值对,不清空sessionid
    # request.session.flush() # 清除所有session键值对,清空sessionid,并清空数据库对应的记录
    del request.session['username'] # 清除指定session键值对
    return res

@check_login
def list_article(request):
    return HttpResponse("文章列表")