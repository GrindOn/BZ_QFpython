from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from home.models import *
# Create your views here.
from market.goodfilters import GoodsFilter
from market.markserializers import GoodTypeSerializer, GoodsSerializer


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


# class GoodsListView(APIView):
#     def get(self,request,*args,**kwargs):
#         params = request.query_params
#         # print(params)
#         tid = request.query_params.get('typeid')
#         # 商品列表
#         goods_list = AxfGoods.objects.filter(categoryid=int(tid))
#         print(tid,type(tid))
#
#         # 过滤子类商品
#         childcid = int(request.query_params.get('childcid',0))
#         if childcid > 0:
#             goods_list = goods_list.filter(childcid=childcid)
#
#         # 对结果排序
#         rule_type = request.query_params.get('order_rule','0')
#         if rule_type == '1':
#             goods_list = goods_list.order_by("price")
#         elif rule_type == '2':
#             goods_list = goods_list.order_by('-price')
#         elif rule_type == '3':
#             goods_list = goods_list.order_by('productnum')
#         elif rule_type == '4':
#             goods_list = goods_list.order_by("-productnum")
#
#         # 序列化
#         goods_serializer = GoodsSerializer(instance=goods_list,many=True)
#         goods_list = goods_serializer.data
#         print(goods_list)
#
#         # 商品分类的子类列表
#         goodtype = AxfFoodtype.objects.filter(typeid=int(tid)).first()
#         childtypenames = goodtype.childtypenames # 子类名称
#         # [{'child_name':全部分类', 'child_value': '0'}]
#         childtypenames = childtypenames.split("#")
#         childtypenames = [value.split(":") for value in childtypenames]
#         childtypenames = [{'child_name':elem[0],'child_value':elem[1]} for elem in childtypenames]
#         print(childtypenames)
#         return Response({
#             'code':200,
#             'msg':'查询成功',
#             'data':{
#                 'goods_list':goods_list,
#                 'order_rule_list':settings.ORDER_RULE_LIST,
#                 'foodtype_childname_list':childtypenames
#             }
#             })

class GoodsListView(ListAPIView):
    queryset = AxfGoods.objects.all()
    serializer_class = GoodsSerializer
    filter_class = GoodsFilter  # 过滤器
    def list(self, request, *args, **kwargs):
        # filter_queryset使用过滤器对查询结果集过滤
        queryset = self.filter_queryset(self.get_queryset())
        # 序列化
        serializer = self.get_serializer(queryset, many=True)

        # 商品分类的子类列表
        tid = request.query_params.get('typeid')
        goodtype = AxfFoodtype.objects.filter(typeid=int(tid)).first()
        childtypenames = goodtype.childtypenames # 子类名称
        childtypenames = childtypenames.split("#")
        childtypenames = [value.split(":") for value in childtypenames]
        childtypenames = [{'child_name':elem[0],'child_value':elem[1]} for elem in childtypenames]
        return Response({
                    'code':200,
                    'msg':'查询成功',
                    'data':{
                        'goods_list':serializer.data,
                        'order_rule_list':settings.ORDER_RULE_LIST,
                        'foodtype_childname_list':childtypenames
                        }
                    })

