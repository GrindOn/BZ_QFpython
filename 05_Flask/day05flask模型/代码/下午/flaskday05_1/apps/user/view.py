from flask import Blueprint, url_for

user_bp = Blueprint('user', __name__)


@user_bp.route('/')
def user_center():
    print(url_for('user.register'))  # 反向解析
    return '用户中心'


@user_bp.route('/register')
def register():
    return '用户注册'
