"""day08 URL Configuration

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
app_name='App'
urlpatterns = [
    path('', views.index,name='index'),
    path('all/',views.cache_all1, name='all'),
    path('cachedata/',views.cache_data1,name='cache_data'),

    # 邮件验证
    path('checkuser/',views.check_user,name='checkuser'),
    path('active/<token>/',views.active_user,name='activeuser'),


    # celery 测试
    path('task/',views.exec_tasks,name='task'),

    # 日志
    path('log/',views.handle_log, name='log'),
]
