"""day05 URL Configuration

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

from App02 import views
app_name = 'App02'
urlpatterns = [
    path('index/',views.index,name='index'),
    path('one2one/',views.one2one,name='one2one'),
    # 短信验证
    path('send/',views.send_sms, name='send'),
    # 分页
    path('page/',views.fenye, name='page'),
    path('page/<int:page>/',views.fenye, name='page'),

]
