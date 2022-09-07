from flask import Blueprint
from flask_restful import Resource, marshal_with, fields

from apps.user.model import User
from exts import api

user_bp = Blueprint('user', __name__, url_prefix='/api')

user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'password': fields.String,
    'udatetime': fields.DateTime
}


# 定义类视图
class UserResource(Resource):
    # get 请求的处理
    @marshal_with(user_fields)
    def get(self):
        users = User.query.all()
        # userList = []
        # for user in users:
        #     userList.append(user.__dict__)
        return users

    # post
    def post(self):
        return {'msg': '------>post'}

    # put
    def put(self):
        return {'msg': '------>put'}

    # delete
    def delete(self):
        return {'msg': '------>delete'}


api.add_resource(UserResource, '/user')
