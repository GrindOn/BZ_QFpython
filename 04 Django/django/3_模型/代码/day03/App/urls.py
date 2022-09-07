"""day03 URL Configuration

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
from django.urls import path

from App import views

app_name = 'App'  # 应用名空间
urlpatterns = [
    path('', views.index, name='index'),
    path('show/<name>/',views.show, name='show'),
    path('reverse/', views.reverse_url, name='reverse'),
    # 注册
    path('register/',views.register, name='register'),
    path("include/",views.include_div, name='include'),

    # 模板中url
    path("url/",views.handle_url,name='url'),
    path("extends/",views.handle_extend,name='extends'),

    # 静态资源
    # 自己路由不要以static开头
    path('wz/',views.handle_static,name='wz'),

    #jinja2
    path('jin/',views.load_jinja,name='jin'),
    # 图片验证码
    path('vc/',views.generate,name='vc'),

]
