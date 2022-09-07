from rest_framework import status
from rest_framework.generics import GenericAPIView,CreateAPIView
from rest_framework.response import Response

# Create your views here.
from home.models import AxfUser
from user.userserializers import UserSerializer, UserRegisterSerializer, LoginSerializer

from user.util import token_confirm

class UserShowView(GenericAPIView):
    queryset = AxfUser.objects.all()
    serializer_class = UserSerializer

    def get(self,request):
        # 获取token
        token = request.query_params.get('token')
        try:
            uid = token_confirm.confirm_validate_token(token)
        except Exception as e:
            print(e)
            return Response({
                'code':107,
                'msg':'token失效，请重新登录',
                'data':{}
            })
        # 获取到了uid
        try:
            user = AxfUser.objects.get(pk=uid)
        except Exception as e:
            print(e)
            return Response({
                'code':107,
                'msg':'该用户不存在',
                'data':{}
            })

        # 序列化
        serializer = UserSerializer(instance=user)
        return Response({
             'code':200,
            'msg':'查询成功',
            'data':{
                'user_info':serializer.data
            }
        })


class UserRegisterView(GenericAPIView):
    queryset = AxfUser.objects.all()
    serializer_class = UserRegisterSerializer

    def post(self,request):
        # 反向序列化
        serializer = self.get_serializer(data=request.data)
        # 验证
        if serializer.is_valid():
            # 保存
            user = serializer.save()
            print(user)
            return Response({
                'code':200,
                'msg':'注册成功',
                'data':{'user_id':user.id}
            })
        return Response({
            'code': 105,
            'msg': '注册失败',
            'data':{'info':serializer.errors}
        })


class UserLoginrView(CreateAPIView):
    queryset = AxfUser.objects.all()
    serializer_class = LoginSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print("kkkk")
        # 验证通过
        if serializer.is_valid():
            # 1 产生token
            username = serializer.data.get('u_username')
            user = AxfUser.objects.filter(u_username=username).first()
            # 生成token
            token = token_confirm.generate_validate_token(user.id)
            print(token)
            return Response({'code':status.HTTP_200_OK,
                             'msg':'登录成功',
                             'data':{'user_id':user.id,'token':token}})
        else: # 验证没通过
            print(serializer.errors)
            return Response({'code':1004,'msg':'校验参数错误',
                             'data':{'error':serializer.errors,'token':None}})
