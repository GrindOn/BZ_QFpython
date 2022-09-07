"""day12 URL Configuration

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

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('rela/', views.RelatedObjectView.as_view(), name='rela'),
    path('req/', views.RequestView.as_view(), name='req'),
    path('fbv/',views.fbv, name='fbv'),
    path('create/',views.BookCreateView.as_view(),name='create'),
    path('retrive/<int:pk>/',views.BookRetriveView.as_view(),name='retrive'),
]
