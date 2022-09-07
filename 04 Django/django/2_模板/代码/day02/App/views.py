from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse


def index(request):
    return HttpResponse("首页")


def show(request,name,age):
    return HttpResponse(name + ":"+str(age))


def call(request,phone):
    # return HttpResponse(phone)
    return render(request,'call.html')


def req_res(request):
    print(request.method)
    # print(request.GET.get("username")) # 如果username不存在，会返回None
    # print(request.GET["username"])  # 如果username不存在，会报错
    # url只能ascii码，不是ascii必须要转义
    # print(request.GET.getlist('username'))
    #post
    # print(request.POST.getlist('username'))

    # print(request.path)
    # 来源页面
    # http://127.0.0.1:9001/user/call/0998-12345678/
    # print(request.META.get("HTTP_REFERER"))
    # print(request.META.get("REMOTE_ADDR"))

    # 响应对象
    # res = HttpResponse("ok")
    # res.status_code = 300
    # res.content = b"123"

    # res = render(request,'call.html')
    # return res

    # JsonResponse
    # return JsonResponse({'code':1})
    # return JsonResponse([1,2,3,4,5],safe=False)

    # 重定向
    # return HttpResponseRedirect("/user/")
    # return redirect("/user/")
    # return redirect("/user/show/{}/{}/".format('tom',30))
    # return redirect("/user/show/admin/50/")
    # 应用内跳转可以不写http://127.0.0.1:9003
    # return redirect("http://127.0.0.1:9003/user/show/admin/50/")
    # 应用外跳转
    # return redirect("https://www.baidu.com/")

    # 反向定位:由应用命名空间:name来确定路由
    # print(reverse("App:index"))
    # return redirect(reverse("App:index"))  # 不带参数

    # 如果参数有名字，必须使用关键字传参的方式
    # print(reverse("App:show",kwargs={'name':'admin','age':20}))
    # return redirect(reverse("App:show",kwargs={'name':'admin','age':20}))
    # print(1 / 0)
    print(reverse("App:call",args=('0311-58931234',)))
    return redirect(reverse("App:call",args=('0311-58931234',)))
