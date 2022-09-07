from rest_framework import status
from rest_framework.generics import ListCreateAPIView

# Create your views here.
from rest_framework.response import Response

from axf import settings
from cart.CartPeressions import CartPermission
from cart.MyAuthentications import CartAuthentication
from home.models import AxfOrder, AxfCart, AxfOrdergoods
from order.orderfilters import OrderFilter
from order.orderserializers import OrderSerializer


class OrderListCreateView(ListCreateAPIView):
    queryset = AxfOrder.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = CartAuthentication,
    permission_classes = CartPermission,
    filter_class = OrderFilter

    # 重写父类的list，获取所有订单信息
    def list(self, request, *args, **kwargs):
        queryset = self.queryset.filter(o_user=request.user)
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({'code':200,'msg':'请求成功','data':serializer.data})

    # 生成订单
    def create(self, request, *args, **kwargs):
        # 找到该用户在购物车中所选商品
        carts = AxfCart.objects.filter(c_user=request.user).filter(c_is_select=1)

        # 创建订单
        my_order = AxfOrder()
        my_order.o_status = settings.ORDER_STATUS_NOT_PAY
        my_order.o_user = request.user
        my_order.o_price = self.compute(carts)
        my_order.save()

        # 把购物中商品添加到订单商品表中
        self.add_to_ordergoods(my_order,carts)

        return Response({'code':status.HTTP_200_OK,'msg':'请求成功','order_id':my_order.id})

    # 计算购物中用户所选上商品的总值
    def compute(self, carts):
        total = 0
        for cart in carts:
            total += cart.c_goods_num * cart.c_goods.price
        return total

    def add_to_ordergoods(self, my_order, carts):
        res = []
        for cart in carts:
            order_goods = AxfOrdergoods()  # 实例化订单商品对象
            order_goods.o_goods_num = cart.c_goods_num
            order_goods.o_order = my_order
            order_goods.o_goods = cart.c_goods
            res.append(order_goods)
        AxfOrdergoods.objects.bulk_create(res)
