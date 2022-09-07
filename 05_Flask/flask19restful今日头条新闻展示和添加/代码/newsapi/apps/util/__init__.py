# 发送短信息
import random

from flask import request, g
from flask_restful import abort

from apps.models.user_model import User
from apps.util.smssend import SecretPair, SmsSendAPIDemo
from exts import cache


def send_duanxin(phone):
    SECRET_ID = "dcc535cbfaefa2a24c1e6610035b6586"  # 产品密钥ID，产品标识
    SECRET_KEY = "d28f0ec3bf468baa7a16c16c9474889e"  # 产品私有密钥，服务端生成签名信息使用，请严格保管，避免泄露
    BUSINESS_ID = "748c53c3a363412fa963ed3c1b795c65"  # 业务ID，易盾根据产品业务特点分配
    secret_pair = SecretPair(SECRET_ID, SECRET_KEY)
    api = SmsSendAPIDemo(BUSINESS_ID, secret_pair)
    # 验证码随机产生
    code = ""
    for i in range(4):
        ran = random.randint(0, 9)
        code += str(ran)

    params = {
        "mobile": phone,
        "templateId": "11732",
        "paramType": "json",
        "params": {"code": code}
    }

    ret = api.send(params)
    return ret, code


def check_user():
    auth = request.headers.get('Authorization')
    if not auth:
        abort(401, msg='请先登录')
    mobile = cache.get(auth)
    if not mobile:
        abort(401, msg='无效令牌')
    user = User.query.filter(User.phone == mobile).first()
    if not user:
        abort(401, msg='此用户已被管理员删除')
    g.user = user


def login_required(func):
    def wrapper(*args, **kwargs):
        check_user()
        return func(*args, **kwargs)
    return wrapper
