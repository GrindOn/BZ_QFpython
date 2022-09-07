from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return HttpResponse("首页")


def show(request,age=0):
    print(type(age))
    return HttpResponse(str(age))


def list_user(request,name):
    print(name,type(name))
    return HttpResponse(name)


def access(request,path):
    # path 可以包含任何字符，包括/
    return HttpResponse(path)

# 视图函数第一个参数就请求对象，由django传递
def get_phone(request,phone):
    # request常用属性
    # get传参的获取
    # print(request.GET)  # GET quersetDict
    # # 获取单一值
    # print(request.GET.get('username'))
    # print(request.GET.getlist('age'))  # 返回值是一个列表 ['20', '23']

    # POST
    # print(request.POST.get('username'))
    # print(request.POST.getlist('hobby'))

    # 获取请求方法
    print(request.method) # 返回方法是大写的GET\POST

    # 获取请求路径
    print(request.path)

    # 其他请求属性
    # print(request.META)
    #
    # # 客户端地址
    # print(request.META.get('REMOTE_ADDR'))
    #
    # # 来源页面
    # print(request.META.get('HTTP_REFERER'))

    # 常用方法
    print(request.get_full_path())  #/user/tel/12345678/?name=2222

    print(request.get_host()) #127.0.0.1:9012

    print(request.build_absolute_uri()) #http://127.0.0.1:9012/user/tel/12345678/?name=2222


    # 获取请求参数的字典 QueryDict=>dict
    print(request.GET.dict()) # {'name': '2222'}


    return HttpResponse(phone)  # 返回给用户的是响应对象


def get_tel(request,tel):
    return HttpResponse("命名组")


def change_name(request,name):
    return HttpResponse(name)


def handle_response(request):
    # res = HttpResponse("响应对象")
    # res.content_type = "text/html"
    # res.status_code = 400  # 设置状态码
    # return res

    # render返回响应对象
    # res = render(request,'example.html')
    # return res

    # jsonresponse 可以返回json字符串
    # jsonresponse一般是可以把字典、列表转换为json返回给前端
    # 字典、列表只能包含内置类型
    # return JsonResponse({'name':'tom'})
    # 如果参数表示字典，必须把safe设置为False
    return JsonResponse([1,2,3,4,5],safe=False)


def handle_redirect(request):
    # HttpResponseRedirect重定向到指定路由地址，参数就是路由
    # return HttpResponseRedirect("/user/")
    # redirect是HttpResponseRedirect的快捷方式
    return redirect("/user/")