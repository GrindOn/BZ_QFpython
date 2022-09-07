from django.shortcuts import render

# Create your views here.
def index(request):
    num = 10
    title = "中文"
    return render(request,'index.html',locals())