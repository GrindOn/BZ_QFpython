"""da04 URL Configuration

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
    path('curd/',views.process_data,name='curd'),
    path('query/',views.process_query,name='query'),
    path('filter/',views.process_filter,name='filter'),
    # 统计分组
    path("group/",views.handle_group, name='group'),

    # 原始sql
    path("raw/",views.handle_sql, name='raw'),
]
