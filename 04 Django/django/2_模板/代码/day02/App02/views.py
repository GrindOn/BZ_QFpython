from datetime import datetime

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.views.decorators.csrf import csrf_exempt


def index(request):

    # html = """
    # <html>
    # <head>
    # <meta charset='utf-8'>
    # </head>
    # <body>
    # <table border='1' cellspacing='0'>
    #
    # """
    # other = """
    # </table>
    # </body>
    # </html>
    # """
    # users = [{'username':'admin'},{'username':'hello'}]
    # for user in users:
    #     html += "<tr><td>"+user['username']+"</td></tr>"
    # html += other

    # return HttpResponse(html)

    # 使用模板引擎
    users = [{'username': 'admin'}, {'username': 'hello'}]
    return render(request,"app02/index.html",context=locals())


def process_template(request):
    return render(request,"example.html")


def load_template(request):
    # # 1.加载模板文件，生成模板对象
    # obj = loader.get_template("example.html")
    # print(obj,type(obj))
    # # 2.渲染
    # res = obj.render({'name':'admin'})
    # # 渲染的结果生成html源文件（字符串）
    # print(res)
    # return HttpResponse(res)

    # render加载和渲染一块进行，是一种快捷方式
    return render(request,'example.html',context={'name':'admin'})


def handle_var(request):
    num = 10
    name = "伟大的意大利左后卫"
    students = [10,20,30,[50,60]]
    student = {'name':'马尔蒂尼','age':30}
    return render(request,"变量.html",locals())


def handle_filter(request):
    num = 10
    name = "伟大的意大利左后卫"
    # age = None
    t1 = datetime.now()
    content = "<h1>自动转义功能，把<和>转义普通字符</h1>"
    return render(request,'过滤器.html',locals())


def handle_tag(request):
    l1 = [10,20,30,40]
    num = 21
    return render(request,'tag.html',locals())

# 局部禁用csrf保护
@csrf_exempt
def login(request):
    if request.method == "POST":
        print(request.POST.get('username'))

    return render(request,"login.html")


def handle_ajax(request):
    print(1111)
    if request.is_ajax():
        return JsonResponse({"code":0,'msg':"登录成功"})
    print(2222)
    return render(request,"ajax1.html")