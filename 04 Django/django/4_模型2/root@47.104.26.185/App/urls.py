"""blog URL Configuration

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
app_name = 'App'
urlpatterns = [
    path('', views.index, name='index'),
    # 左边导航栏
    path('left/',views.public_left, name='left'),

    # 右边的标题栏
    path('header/', views.public_header, name='header'),

    # 主窗口，内容展示
    path('main/',views.public_main, name='main'),
    path('main/<int:cid>/',views.public_main, name='main'),
    path('main/<int:cid>/<int:page>/',views.public_main, name='main2'),
]
