import hashlib

from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy import or_, and_, not_

from apps.user.models import User
from exts import db

user_bp = Blueprint('user', __name__)


# 注册
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


# 用户中心
@user_bp.route('/')
def user_center():
    # 查询数据库中的数据
    users = User.query.filter(User.isdelete == False).all()  # select * from user;
    print(users)  # [user_objA,user_objB,....]
    return render_template('user/center.html', users=users)


# 登录
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


# 检索
@user_bp.route('/search')
def search():
    keyword = request.args.get('search')  # 用户名 | 手机号
    # 查询
    user_list = User.query.filter(or_(User.username.contains(keyword), User.phone.contains(keyword))).all()
    return render_template('user/center.html', users=user_list)


# 用户删除
@user_bp.route('/delete', endpoint='delete')
def user_delete():
    # 获取用户id
    id = request.args.get('id')
    # 1. 逻辑删除 （更新）
    # # 获取该id的用户
    # user = User.query.get(id)
    # # 逻辑删除：
    # user.isdelete = True
    # # 提交
    # db.session.commit()
    # 2. 物理删除
    user = User.query.get(id)
    # 将对象放到缓存准备删除
    db.session.delete(user)
    # 提交删除
    db.session.commit()

    return redirect(url_for('user.user_center'))


# 用户信息更新
@user_bp.route('/update', endpoint='update', methods=['GET', 'POST'])
def user_update():
    if request.method == 'POST':
        username = request.form.get('username')
        phone = request.form.get('phone')
        id = request.form.get('id')
        # 找用户
        user = User.query.get(id)
        # 改用户信息
        user.phone = phone
        user.username = username
        # 提交
        db.session.commit()
        return redirect(url_for('user.user_center'))

    else:
        id = request.args.get('id')
        user = User.query.get(id)
        return render_template('user/update.html', user=user)


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
    # user_list = User.query.filter(User.username.like('z%')).all()  # select * from user where username like 'z%';
    # 舒肤佳沐浴露柠檬清新1000ml 果香清爽 无皂基 新老包装随机发货
    # user_list = User.query.filter(or_(User.username.like('z%'), User.username.contains('i'))).all()
    # select * from user where username like 'z%' or username like '%i%';
    # user_list = User.query.filter(and_(User.username.contains('i'), User.rdatetime.__gt__('2020-05-25 10:30:00'))).all()
    # user_list = User.query.filter(and_(User.username.contains('i'), User.rdatetime > '2020-05-25 10:30:00')).all()
    # user_list = User.query.filter(not_(User.username.contains('i'))).all()
    # user_list = User.query.filter(User.phone.in_(['15810106788','13801011299'])).all()
    # user_list = User.query.filter(User.username.contains('z')).order_by(-User.rdatetime).all()
    # # user_list = User.query.order_by(-User.id).all()

    # limit的使用 + offset
    # user_list = User.query.limit(2).all()
    user_list = User.query.offset(4).limit(2).all()
    return render_template('user/select.html', user=user, users=user_list)


@user_bp.route('/test1')
def test1():
    return render_template('user/test.html')

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
