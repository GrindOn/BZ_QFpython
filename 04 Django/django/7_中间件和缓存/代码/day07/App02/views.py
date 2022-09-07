import os

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App02.utils import FileUpload
from day07 import settings


def edit(request):
    print(1/0)
    if request.method == 'POST':
        print(request.POST.get('content'))
    return render(request,'article.html')


def handle_upload(request):
    if request.method == "POST":
        # 获取文件上传对象
        fobj = request.FILES.get('photo')
        # path = os.path.join(settings.STATICFILES_DIRS[0],'upload')
        # path = os.path.join(path,fobj.name)
        # if fobj:
        #     print(fobj.name,fobj.size)
        #     # 文件读写
        #     with open(path,'wb') as target:
        #         # 源文件是否大于2.5M
        #         if fobj.multiple_chunks():
        #             for data in fobj.chunks():
        #                 target.write(data)
        #         else:
        #             target.write(fobj.read())

        # 使用自定义文件上传类
        path = settings.MDEIA_ROOT
        fp = FileUpload(fobj)
        if fp.upload(path):
            return HttpResponse("文件上传成功")

    return render(request,'portrait.html')


def user_login(request):
    return HttpResponse("登录")


def index(request):
    return HttpResponse("首页")