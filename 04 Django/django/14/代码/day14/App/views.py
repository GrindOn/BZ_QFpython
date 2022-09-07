from collections import OrderedDict

from django.core.paginator import Paginator
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView,ListAPIView
# Create your views here.
from rest_framework.pagination import PageNumberPagination

from App.MyFilters import BookFilter
from App.MyPaginations import BookListPager
from App.models import Bookinfo
from App.serializers import BookinfoSerializer

# PageNumberPagination.page_size_query_param = 'page_size'

class BookListView(GenericAPIView):
    """"
    get:
    获取图书列表
    """


    queryset = Bookinfo.objects.all()
    serializer_class = BookinfoSerializer
    pagination_class = BookListPager

    def get(self,request,*args,**kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class BooksView(ListAPIView):
    """
    图书分页显示
    """
    queryset = Bookinfo.objects.all()
    serializer_class = BookinfoSerializer
    #过滤字段
    # filter_fields = ('btitle','bread')
    # 指定过滤类
    filter_class = BookFilter