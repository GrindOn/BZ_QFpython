from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    num = 10
    name = "方舟子"
    list1 = [12,30,34,40]
    return render(request,'app/index.html',locals())


def reverse_url(request):
    # return redirect(reverse("App:index"))
    return redirect(reverse("App:show",kwargs={'name':'tom'}))


def show(request,name):
    return HttpResponse(name)

# 局部禁止
@csrf_exempt
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        # 返回ajax请求
        return JsonResponse({'code':1})
    return render(request,"app/register.html")


def include_div(request):
    return render(request,"app/list.html")


def handle_url(request):
    return render(request,"app/menu.html")


def handle_extend(request):
    return render(request,'app/child.html',{'title':'继承'})


def handle_static(request):
    return render(request,'app/wenzhang_xinwen.html')


def load_jinja(request):
    return render(request,"index1.html")


def generate(request):
    from App.verifycode import vc
    data = vc.generate()

    # res.content_type = "image/png"
    return HttpResponse(data,'image/png')