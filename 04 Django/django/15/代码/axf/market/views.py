from rest_framework.response import Response
from rest_framework.views import APIView
from home.models import *
# Create your views here.
from market.markserializers import GoodTypeSerializer


class GoodTypeListView(APIView):
    def get(self,request):
        # 获取商品类型
        queryset = AxfFoodtype.objects.all()
        # 序列化
        goodtype_serializer = GoodTypeSerializer(queryset,many=True)
        return Response({
            'code':200,
            'msg':'请求成功',
            'data':goodtype_serializer.data
        })