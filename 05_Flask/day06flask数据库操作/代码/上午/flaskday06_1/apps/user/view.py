import hashlib

from flask import Blueprint, render_template, request, redirect, url_for

from apps.user.models import User
from exts import db

user_bp = Blueprint('user', __name__)


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        phone = request.form.get('phone')
        if password == repassword:
            # 注册用户
            user = User()
            user.username = username
            user.password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            user.phone = phone
            # 添加并提交
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('user.user_center'))

    return render_template('user/register.html')


@user_bp.route('/')
def user_center():
    # 查询数据库中的数据
    users = User.query.all()  # select * from user;
    print(users)  # [user_objA,user_objB,....]
    return render_template('user/center.html', users=users)


@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # 关键  select * from user where username='xxxx';
        new_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        # 查询
        user_list = User.query.filter_by(username=username)

        for u in user_list:
            # 此时的u表示的就是用户对象
            if u.password == new_password:
                return '用户登录成功！'
        else:
            return render_template('user/login.html', msg='用户名或者密码有误！')

    return render_template('user/login.html')


@user_bp.route('/test')
def test():
    username = request.args.get('username')  # zhangsan
    user = User.query.filter_by(username=username).first()
    print(user.username, user.rdatetime)

    user = User.query.filter_by(username=username).last()
    print(user.username, user.rdatetime)
    return 'test'


@user_bp.route('/select')
def user_select():
    user = User.query.get(2)  # 根据主键查询用户使用get（主键值）返回值是一个用户对象
    # user1 = User.query.filter(User.username == 'wangwu').all()  # all(), first()
    user_list = User.query.filter(User.username.contains('z')).all()  # select * from user where username like 'z%';

    return render_template('user/select.html', user=user, users=user_list)


'''
______
______
  登录
  
提交过来： username + password

跟数据库中数据进行匹配
-----
----
-----
-----
-----

'''
