"""day02 URL Configuration

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

from App02 import views
app_name = "App02"  # 应用的名空间
urlpatterns = [
    path("",views.index, name='index'),
    path("example/",views.process_template, name='example'),
    path("render/",views.load_template, name='render'),
    # 变量
    path('var/',views.handle_var, name='var'),
    # 过滤器
    path('filter/',views.handle_filter, name='filter'),
    # 内建标签
    path('tag/',views.handle_tag, name='tag'),
    #csrf保护
    path("csrf/",views.login, name='login'),
    path('ajax/',views.handle_ajax,name='ajax'),
]
