from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from App.models import Article, Category


def delete_article(request,aid,cid=-1,page=1):
    """

    :param request:
    :param aid: 文章id
    :param cid: 类别id
    :param page: 当前页码
    :return:
    """
    arcticle = Article.objects.get(pk=aid)
    if arcticle:
        arcticle.delete()

    return redirect(reverse("App:main2", kwargs={'cid':cid,'page':page}))



def publish_article(request,cid=-1):
    if request.method == "POST":
        data = request.POST.dict()
        data.pop('csrfmiddlewaretoken')
        data.pop('photo')
        Article.add(**data)
        return redirect(reverse("App:main"))
    else:
        cid = cid if cid > 0 else Category.first_category().cid

        return render(request,'wenzhang_xinwen_fabu.html',locals())


def update_article(request,cid,aid):
    article = Article.objects.get(pk=aid)

    return render(request,'wenzhang_xinwen_info.html',locals())


