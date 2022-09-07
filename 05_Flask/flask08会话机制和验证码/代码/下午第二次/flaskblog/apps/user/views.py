from flask import Blueprint, render_template, request, redirect, url_for, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash

from apps.user.models import User
from exts import db

user_bp1 = Blueprint('user', __name__, url_prefix='/user')


# 首页
@user_bp1.route('/')
def index():
    # 1。cookie获取方式
    # uid = request.cookies.get('uid', None)
    # 2。session的获取,session底层默认获取
    uid = session.get('uid')
    if uid:
        user = User.query.get(uid)
        return render_template('user/index.html', user=user)
    else:
        return render_template('user/index.html')


# 用户注册
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
            # print(password)
            user.phone = phone
            user.email = email
            # 添加并提交
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('user.index'))
    return render_template('user/register.html')


# 手机号码验证
@user_bp1.route('/checkphone', methods=['GET', 'POST'])
def check_phone():
    phone = request.args.get('phone')
    user = User.query.filter(User.phone == phone).all()
    print(user)
    # code: 400 不能用    200 可以用
    if len(user) > 0:
        return jsonify(code=400, msg='此号码已被注册')
    else:
        return jsonify(code=200, msg='此号码可用')


# 用户登录
@user_bp1.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        users = User.query.filter(User.username == username).all()
        for user in users:
            # 如果flag=True表示匹配，否则密码不匹配
            flag = check_password_hash(user.password, password)
            if flag:
                # 1。cookie实现机制
                # response = redirect(url_for('user.index'))
                # response.set_cookie('uid', str(user.id), max_age=1800)
                # return response
                # 2。session机制,session当成字典使用
                session['uid'] = user.id
                return redirect(url_for('user.index'))

        else:
            return render_template('user/login.html', msg='用户名或者密码有误')
    return render_template('user/login.html')


@user_bp1.route('/logout')
def logout():
    response = redirect(url_for('user.index'))
    # 通过response对象的delete_cookie(key),key就是要删除的cookie的key
    # response.delete_cookie('uid')
    # del session['uid']
    session.clear()
    return response
