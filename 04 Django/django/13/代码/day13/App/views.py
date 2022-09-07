from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

# Create your views here.
from App.MyAuthentications import MyAuthentaion
from App.MyPerssions import MyPermisson
from App.MyThrottle import MyThrottle
from App.models import User
from App.serializers import UserSerializer
from App.util import token_confirm


class UserInfoView(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # 局部认证，只针对当前类
    authentication_classes = (MyAuthentaion,)

    # 授权
    # permission_classes = (MyPermisson,)

    # 节流
    # throttle_classes = (MyThrottle,)

    lookup_field = 'pk'
    def get(self,request,pk):
        obj = self.get_object()  # 获取对象
        us = UserSerializer(instance=obj)  # 序列化
        return Response(us.data)


class UserQueryView(GenericAPIView):
    # 查询结果集
    queryset = User.objects.all()
    # 序列化器
    serializer_class = UserSerializer

    def get(self,request,name):
        data = self.get_queryset()
        data = data.filter(username=name)
        print(data)
        us = UserSerializer(instance=data,many=True)
        return Response(us.data)


class UserToken(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get(self,request):
        # 产生token
        user = User.objects.first()
        # 使用用户id生成token
        token = token_confirm.generate_validate_token(user.id)
        # 把token返回给客户端
        return Response({'token':token})