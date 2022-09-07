from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash

from apps.user.models import User
from exts import db

user_bp1 = Blueprint('user', __name__, url_prefix='/user')


@user_bp1.route('/')
def index():
    return render_template('base.html')


@user_bp1.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        phone = request.form.get('phone')
        email = request.form.get('email')
        if password == repassword:
            # 注册用户
            user = User()
            user.username = username
            # 使用自带的函数实现加密：generate_password_hash
            user.password = generate_password_hash(password)
            print(password)
            user.phone = phone
            user.email = email
            # 添加并提交
            db.session.add(user)
            db.session.commit()
            return '注册成功！'
    return render_template('user/register.html')
