import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from django.views.generic import View

# Create your views here.
from App.models import Bookinfo


def index(request):

    return HttpResponse("ok")

# 前后端分离，非DRF版
# 后端需要向前端提供JSON数据
class BooksView(View):
    # 查询所有图书
    def queryset_to_list(self,querset):
        res = []
        for obj in querset:
            res.append(obj.to_dict())
        return res


    def get(self,request,*args,**kwargs):
        books = Bookinfo.objects.all()
        print(books)
        # 如果参数不是字典，safe应该设置为false
        return JsonResponse(self.queryset_to_list(books),safe=False)

    # 增加图书
    def post(self,request,*args,**kwargs):
        data = request.POST.dict()
        Bookinfo.objects.create(**data)
        print(data)
        return JsonResponse({
            'code':1,
            'msg':"创建成功"
        })

    def put(self,request,bid):
        # print(bid)
        book = Bookinfo.objects.get(pk=bid)
        # book.__dict__.pop("_state")

        # 获取put传参 ,参数必须是json格式
        data = request.body.decode()
        print(data)
        # # 把json字符串转换为字典
        data = json.loads(data)
        print(data)

        # 更新对象
        book.__dict__.update(data)
        print(book.__dict__)
        book.save()
        return JsonResponse({
            'code': 1,
            'msg': "修改成功"
        })

    def delete(self,request):
        pass