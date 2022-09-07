"""day06 URL Configuration

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

app_name = "App"
urlpatterns = [
    path("cap/",views.handle_captcha, name='cap'),
    path("refresh/",views.refresh,name='refresh'),
    path('send/',views.mail_send,name='send'),
    path('test/',views.test_pass,name='send'),
    path('yzm/',views.output_yzm,name='yzm'),
]
