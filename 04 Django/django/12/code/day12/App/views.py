from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.mixins import CreateModelMixin
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, CreateAPIView,RetrieveAPIView
from rest_framework.response import Response
# Create your views here.
from App.models import Bookinfo
from App.serializers import BookSerializer


class IndexView(APIView):
    def get(self,request):

        # 正向序列化
        # books = Bookinfo.objects.all()
        # books = BookSerializer(instance=books,many=True)
        # print(books.data)
        # return Response(data=books.data)

        # 反向序列化: 将前端传过来的数据生成对象，可以保存到数据库
        book = {'btitle':'庆余年2','bpub_date':'2020-3-10',
                'bread':10,'bcomment':30,'bimage':'static/1.jpg'}
        bs = BookSerializer(data=book)
        # 验证
        if bs.is_valid():
            # 保存到数据
            bs.save()
            print(bs.data)
            return Response({'code':2,'msg':'保存成功'})
        else:
            print(bs.errors)
            return Response({'code':1,'msg':bs.errors})


        # 更新
        # data = {'bimage': 'static/1.jpg'}
        # bimageook = Bookinfo.objects.get(pk=10)

        # 把对象赋值instance，把要更新的属性字典赋值给data
        # bs = BookSerializer(instance=book,data=data)
        # 验证
        # if bs.is_valid():
        #     # 保存到数据
        #     bs.save()
        #     print(bs.data)
        #     return Response({'code': 2, 'msg': '保存成功'})
        # else:
        #     print(bs.errors)
        #     return Response({'code': 1, 'msg': bs.errors})

        # 部分更新
        # for key, value in data.items():
        #     if hasattr(book, key):
        #         setattr(book, key, value)
        # book.save()
        # return Response({'code': 2, "msg": 'update success'})
        #


class RelatedObjectView(APIView):
    def get(self,request):
        # 序列化
        books = Bookinfo.objects.all()
        bs = BookSerializer(instance=books,many=True)
        print(bs.data)

        return Response(data=bs.data)


class RequestView(APIView):
    # 自己指定解析器
    parser_classes = (JSONParser,)
    def get(self,request):
        # 非GET
        print(request.data)
        # GET传参
        print(request.query_params)
        # Response可以将内置类型转换为字符串
        return Response([1,2,3])


@api_view(['GET','POST'])
def fbv(request):
    return Response("ok")

# 创建一本图书
# class BookCreateView(CreateModelMixin,GenericAPIView):
#     serializer_class = BookSerializer
#     def post(self,request):
#         return self.create(request)

class BookCreateView(CreateAPIView):
    serializer_class = BookSerializer

# 获取指定对象
class BookRetriveView(RetrieveAPIView):
    queryset = Bookinfo.objects.all()
    serializer_class = BookSerializer