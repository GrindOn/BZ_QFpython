from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from App02.forms import RegisterForm
from App02.models import User


def register(request):
    if request.method == "POST":
        # 用提交的数据生成表单
        form =RegisterForm(request.POST)
        # 能通过验证，返回True，否则返回False
        if form.is_valid():
            # 进行业务处理
            data = form.cleaned_data
            data.pop("confirm")
            # 获取指定字段
            # username = form.cleaned_data.get('username','')
            # print(data,type(data))
            # 如果forms中表单的字段名和models模型的字段名一致
            res = User.objects.create(**data)
            # 如果forms中表单的字段名和models模型的字段名不一致
            # res = User.objects.create(username=username,password=form.cleaned_data.get('password'))
            if res:
                return HttpResponse("注册成功")
        else:
            print(form.__dict__)
            # 验证不成功，把错误信息渲染到前端页面
            return render(request, "register.html",{'form':form})
    return render(request,"register.html")


def user_register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data.pop("confirm")
            # 把用户写入数据库
            # 密码会做签名，不能手动签名加密password
            user = User.objects.create_user(**data)
            if user:
                return HttpResponse("注册成功")
            else:
                return render(request, "register.html",{'form':form})
        else:
            return render(request, "register.html", {'form': form})
    # get请求
    return render(request, "register.html")


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')

        # 用户验证，如果用户名和密码正确，返回User的对下，否则返回None
        user = authenticate(request,username=username,password=password)
        if user:
            # 记录用户登录状态，参数是请求对象和用户对象
            login(request,user)

            return redirect(reverse("App02:index"))
        else:
            return render(request,'login.html',{'msg':'用户名和密码错误'})
    return render(request,'login.html')


def user_logout(request):
    # 退出登录
    logout(request)
    return redirect(reverse("App02:index"))


def index(request):
    # 在后端判断是否登录
    print(request.user.is_authenticated)
    return render(request,'index.html')

# 路由保护
@login_required
def publish_article(request):
    return HttpResponse("发表文章")


def change_password(request):
    # 修改密码
    user = User.objects.get(pk=1)
    user.set_password('123')
    user.save()
    return HttpResponse("修改密码")


def handle_captcha(request):
    return None