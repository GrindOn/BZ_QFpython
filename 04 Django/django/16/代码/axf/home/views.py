from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from home.homeserializers import *
from home.models import *


class HomeListView(GenericAPIView):
    """
    get：
    获取首页数据
    """
    serializer_class = WheelSerializer
    queryset = AxfWheel.objects.all()
    def get(self,request):
        # 数据查询
        nav_queryset = AxfNav.objects.all()
        shop_querset = AxfShop.objects.all()
        mainshow_queyset = AxfMainshow.objects.all()
        mustbuy_querset = AxfMustbuy.objects.all()

        # 序列化
        nav_data = NavSerializer(nav_queryset,many=True)
        shop_data = ShopSerializer(shop_querset,many=True)
        mainshow_data = MainShowSerializer(mainshow_queyset,many=True)
        wheel_data = self.serializer_class(self.queryset.all(),many=True)
        mustbuy_data = MustBuySerializer(mustbuy_querset,many=True)
        return Response({
            'code':200,
            'msg':'请求成功',
            'data':{
                'main_wheels':wheel_data.data,
                'main_navs':nav_data.data,
                'main_mustbuys':mustbuy_data.data,
                'main_shops':shop_data.data,
                'main_shows':mainshow_data.data
            }
        })

