from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

# Create your views here.
from rest_framework.views import APIView

from App.models import Bookinfo
from App02.serializers import BookSerializer


class BookInfoView(GenericAPIView):
    queryset = Bookinfo.objects.all()
    def get(self,request,bid=-1):
        # 所有图书信息
        # books = Bookinfo.objects.all()
        # 序列化：把对象或queryset直接转换为字典或者是列表套字典
        # 如果是queryset则必须将many设置为True，如果对象，则不用设置
        # bs = BookSerializer(instance=self.queryset.all(),many=True)
        # print(bs.data)
        # return Response(data=bs.data)
        if bid < 0:
            return self.find_many(request)
        return self.find_one(request,bid)

    def find_many(self,request):
        bs = BookSerializer(instance=self.queryset.all(), many=True)
        return Response(data=bs.data)
    def find_one(self,request,bid):
        book = self.queryset.get(bid=bid)
        bs = BookSerializer(instance=book)  # 序列化
        return Response(bs.data)


class BookAddView(APIView):
    # queryset = Bookinfo.objects.all()
    serializer_class = BookSerializer
    def post(self,request):
        # print(request.data)
        # 反序列化:字符串转换为对象
        # 把前端传过来的数据赋值给data
        bs = BookSerializer(data=request.data)
        if bs.is_valid():  # 数据验证
            print(bs.validated_data) # 获取验证数据
            bs.save()  # 保存到数据库
            return Response({'code': 1,'msg':'增加成功'})
        else:
            print(bs.errors)
            return Response({'code': 0,'msg':bs.errors})


    def put(self,request):
        print(request.data)
        return Response({'code':1})