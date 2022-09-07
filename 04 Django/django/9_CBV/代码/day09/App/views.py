from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator

from django.views.generic import View

# Create your views here.
# Function Based View  FBV
# 简单，易懂
# 缺点：不能继承，不容易代码复用
from django.views.generic import TemplateView, ListView, DetailView,CreateView

from App.models import User


def index(request):
    return HttpResponse("首页")

# CBV Class Based View 基于类的视图
# 优点：有继承，代码可复用、可维护性更强;一个请求对应一个方法，无需判断
# 缺点：比较抽象，不易懂
class RegisterView(View):
    a = 10
    def get(self,request):
        print(self.a)
        return HttpResponse("GET")

    def post(self,request):
        return HttpResponse("POST")

    def put(self,request):
        return HttpResponse("PUT")

    def delete(self,request):
        return HttpResponse("DELETE")


class MyTemplateView(TemplateView):
    # 模板文件名
    template_name = 'example.html'
    # 获取模板中数据
    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs['name'] = '意大利'
        kwargs['title'] = "欧洲新冠王者"
        return kwargs


class UserListView(ListView):
    # 模板文件名
    template_name = 'userlist.html'
    paginate_by = 5  # 每页记录个数
    ordering = ("uid",)    # 排序字段列表
    # 查询结果集
    # queryset = User.objects.all()

    # 获取查询数据
    def get_queryset(self):
        data = User.objects.filter(uid__gt=20)
        ordering = self.get_ordering()
        if ordering:
            if isinstance(ordering, str):
                ordering = (ordering,)
            data = data.order_by(*ordering)

        return data


class UserDetailView(DetailView):
    template_name = 'userdetail.html'
    queryset = User.objects.all()
    context_object_name = 'user'


class UserCreateView(CreateView):
    # template_name = 'userregister.html'
    # model = User
    # # 字段列表，用于创建用户时设定用户属性
    # fields = ['username','password']
    # success_url = '/'  # 创建成功后跳转的页面
    def get(self,request):
        return render(request,'userregister.html')
    def post(self,request):
        data = request.POST.dict()
        data.pop('csrfmiddlewaretoken')
        User.objects.create(**data)
        return redirect("/")


def check_login(func):
    def inner(request,*args,**kwargs):
        if request.session.get('usename'):
            return func(request,*args,**kwargs)
        return redirect("/")
    return inner

# 对所有请求方法起作用
# @method_decorator(check_login,name='dispatch')
class ArticlePulishView(View):
    def get(self,request):
        return HttpResponse("文章展示")

    @method_decorator(check_login)
    def post(self,request):
        return HttpResponse("发表文章")


class DemoView(View):
    def get(self,request):
        object_list = User.objects.all()
        pagitor = Paginator(object_list,10)
        pager = pagitor.page(1)
        object_list = pager.object_list
        return render(request,'userlist.html',locals())
