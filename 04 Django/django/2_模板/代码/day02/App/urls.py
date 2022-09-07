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

from App import views
app_name = "App"  # 应用的名空间
urlpatterns = [
    path('', views.index, name='index'),
    path('show/<name>/<int:age>/',views.show, name='show'),
    re_path(r'^call/(\d{4}-\d{8})/$',views.call,name='call'),

    # 请求对象===响应对象
    path('req/',views.req_res,name='reqres'),

]
