import random

from flask import Blueprint, jsonify, session
from flask_restful import Api, Resource, reqparse, inputs, fields, marshal
from werkzeug.security import generate_password_hash, check_password_hash

from apps.models.user_model import User
from apps.util import send_duanxin
from exts import cache, db

user_bp = Blueprint('user', __name__)

api = Api(user_bp)

sms_parser = reqparse.RequestParser()
sms_parser.add_argument('mobile', type=inputs.regex(r'^1[356789]\d{9}$'), help='手机号码格式错误', required=True,
                        location=['form', 'args'])


# 发送手机验证码类视图
class SendMessageApi(Resource):
    def post(self):
        args = sms_parser.parse_args()
        mobile = args.get('mobile')
        ret, code = send_duanxin(mobile)
        # 验证是否发送成功
        if ret is not None:
            if ret["code"] == 200:
                # cache.set(key,value,timeout=second)
                cache.set(mobile, code, timeout=1800)
                return jsonify(code=200, msg='短信发送成功！')
        else:
            print("ERROR: ret.code=%s,msg=%s" % (ret['code'], ret['msg']))
            return jsonify(code=400, msg='短信发送失败！')


# 输入
lr_parser = sms_parser.copy()
lr_parser.add_argument('code', type=inputs.regex(r'^\d{4}$'), help='必须输入四位数字验证码', required=True, location='form')

# 输出
user_fields = {
    'id': fields.Integer,
    'username': fields.String
}


# 用户的登录和注册
class LoginAndRegisterApi(Resource):

    def post(self):
        args = lr_parser.parse_args()
        mobile = args.get('mobile')
        code = args.get('code')
        cache_code = cache.get(mobile)
        print('code:', code)
        print('cache_code:', cache_code)
        if cache_code and code == cache_code:
            # 数据库中查找是否存在此mobile
            user = User.query.filter(User.phone == mobile).first()
            # 列表中是否存在用户
            if not user:
                # 注册处理
                user = User()
                user.phone = mobile
                s = ''
                for i in range(13):
                    ran = random.randint(0, 9)
                    s += str(ran)

                user.username = '用户' + s
                db.session.add(user)
                db.session.commit()
                #
            # 登录处理，记录登录状态：session，cookie，cache（redis）
            cache.set(mobile + "_", 1)
            return marshal(user, user_fields)  # 输出的内容
        else:
            return {'errmsg': '验证码错误', 'status': 400}


# 忘记密码
class ForgetPasswordApi(Resource):
    def get(self):
        s = 'QWERTYUIOPLKJHGFDSAZXCVBNMzxcvbnmlkjhgfdsaqwertyuiop1234567890'
        code = ''
        for i in range(4):
            ran = random.choice(s)
            code += ran
        # 保存code
        # cache.set('',code)
        session['code'] = code
        return {'code': code}


# 申请重置密码的输入
reset_parser = sms_parser.copy()
reset_parser.add_argument('imageCode', type=inputs.regex(r'^[a-zA-Z0-9]{4}$'), help='必须输入正确格式的验证码')


class ResetPasswordApi(Resource):
    def get(self):
        args = reset_parser.parse_args()
        mobile = args.get('mobile')
        imageCode = args.get('imageCode')
        code = session.get('code')
        if code and imageCode.lower() == code.lower():
            # 判断手机号码
            user = User.query.filter(User.phone == mobile).first()
            if user:
                # 发送手机验证码
                ret, smscode = send_duanxin(mobile)
                if ret is not None:
                    if ret["code"] == 200:
                        # cache.set(key,value,timeout=second)
                        cache.set(mobile, smscode, timeout=180)
                        return jsonify(status=200, msg='短信发送成功！')
                else:
                    print("ERROR: ret.code=%s,msg=%s" % (ret['code'], ret['msg']))
                    return jsonify(status=400, msg='短信发送失败！')
            else:
                return {'status': 400, 'msg': '此用户未注册，请注册'}
        else:
            return {'status': 400, 'msg': '验证码输入有误或者超时'}


# 更新密码
# 客户端要传入的信息
update_parser = lr_parser.copy()
update_parser.add_argument('password'
                           , type=inputs.regex(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[a-zA-Z0-9]{8,10}$')
                           , help='必须包含大小写字母和数字的组合，不能使用特殊字符'
                           , location='form')
update_parser.add_argument('repassword'
                           , type=inputs.regex(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[a-zA-Z0-9]{8,10}$')
                           , help='必须包含大小写字母和数字的组合，不能使用特殊字符'
                           , location='form')

# 登录设置需要前端传入的内容
password_login_parser = sms_parser.copy()
password_login_parser.add_argument('password', type=str, help='必须输入密码', required=True, location='form')


class UserApi(Resource):
    def post(self):
        args = password_login_parser.parse_args()
        mobile = args.get('mobile')
        password = args.get('password')
        # 判断用户
        user = User.query.filter(User.phone == mobile).first()
        if user:
            if check_password_hash(user.password, password):
                # 说明用户是登录成功的
                cache.set(mobile + '_', 1)
                return {'status': 200, 'msg': '用户登录成功'}

        return {'status': 400, 'msg': '账户名或者密码有误！'}

    def put(self):
        args = update_parser.parse_args()
        code = args.get('code')
        mobile = args.get('mobile')
        cache_code = cache.get(mobile)
        # 判断验证码是否输入正确
        if cache_code and cache_code == code:
            user = User.query.filter(User.phone == mobile).first()
            password = args.get('password')
            repassword = args.get('repassword')
            # 判断密码是否输入一致
            if password == repassword:
                user.password = generate_password_hash(password)
                db.session.commit()
                return {'status': 200, 'msg': '设置密码成功'}
            else:
                return {'status': 400, 'msg': '两次密码不一致'}
        else:
            return {'status': 400, 'msg': '验证码有误'}


api.add_resource(SendMessageApi, '/sms')
api.add_resource(LoginAndRegisterApi, '/codelogin')
api.add_resource(ForgetPasswordApi, '/forget')
api.add_resource(ResetPasswordApi, '/reset')
api.add_resource(UserApi, '/user')
