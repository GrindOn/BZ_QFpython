from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View


class UserInfo(View):
    def get(self,request):
        return JsonResponse({'code':1,'msg':'ok'})