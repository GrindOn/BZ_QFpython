"""exaple0 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path

from App import views

urlpatterns = [
    # path第三个参数name是路由的名称，和视图函数参数无关
    # 首页
    path('',views.index,name='index'),


    # 视图函数中的参数必须和路由中参数名称相同
    # int
    # 可以多个路由对应一个视图函数
    path('show/',views.show,name='show1'),
    path('show/<int:age>/',views.show,name='show'),

    # slug
    path('list/<slug:name>/',views.list_user,name='list'),
    #path,如果有多个参数，path类型必须在最后一个
    path('access/<path:path>/',views.access,name='access'),

    # string 默认参数类型
    path('change/<name>/',views.change_name,name='change'),

    # re_path 和path最大区别就是匹配是正则模式串
    re_path(r'^tel/(\d{8})/$',views.get_phone,name='phone'),

    # 命名组  get_tel中参数必须交tel
    re_path(r'^tell/(?P<tel>\d{8})/$',views.get_tel,name='tel'),

    # 响应对象
    path('response/',views.handle_response,name='response'),

    # 重定向
    path('red/',views.handle_redirect,name='red'),

]
