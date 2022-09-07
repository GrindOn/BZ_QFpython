from django.shortcuts import render

# Create your views here.
from App.models import Category, Article
from App.tools import BaiduPaginator

def index(request):
    return render(request,'index.html')

# 左边导航栏
def public_left(request):
    return render(request,"public_left.html")


def public_header(request):
    return render(request,'public_header.html')


# 文章管理
def public_main(request,cid=-1,page=1):
    categories = Category.objects.all()
    # 获取所有分类id
    postion = [cat.cid for cat in categories]
    if request.method == "POST":
        cid = int(request.POST.get('cid',-1))
        keyword = request.POST.get('keyword','')
        # 文章检索
        articles = Article.objects.filter(cid=cid,title__icontains=keyword)
    else:
        # 检索分类
        if cid < 0:
            first_category = categories.first() # 查询第一个分类
            cid = first_category.cid  # 第一个分类的cid

        # 文章检索
        articles = Article.objects.filter(cid=cid)

    pos = postion.index(cid)

    # 分页
    paginator = BaiduPaginator(articles,10)
    pager = paginator.page(page)
    pager.page_range = paginator.custom_range(paginator.num_pages,page,5)

    return render(request,"wenzhang_xinwen.html",locals())

