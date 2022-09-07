"""day09 URL Configuration

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
from django.contrib import admin
from django.urls import path

from App import views

app_name = 'App'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.RegisterView.as_view(a=90), name='register'),
    path('template/',views.MyTemplateView.as_view(),name='template'),
    # ListView
    path('list/',views.UserListView.as_view(), name='list'),
    path('detail/<int:pk>/',views.UserDetailView.as_view(), name='detail'),
    # 创建用户
    path('create/',views.UserCreateView.as_view(),name='create'),

    # 路由保护
    path('publish/',views.ArticlePulishView.as_view(),name='publish'),
    path('demo/',views.DemoView.as_view(),name='demo')
]
