from flask import Blueprint, request, render_template, redirect

from apps.user.model import User

user_bp = Blueprint('user', __name__)

# 列表保存的是一个一个的用户对象
users = []


@user_bp.route('/')
def user_center():
    return render_template('user/show.html', users=users)


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # 获取post提交的数据
        username = request.form.get('username')
        password = request.form.get('password')
        phone = request.form.get('phone')
        repassword = request.form.get('repassword')
        if password == repassword:
            # 用户名唯一
            for user in users:
                if user.username == username:
                    return render_template('user/register.html', msg='用户名已存在')
            # 创建user对象
            user = User(username, password, phone)
            # 添加到用户列表
            users.append(user)
            return redirect('/')

    return render_template('user/register.html')


@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    return '用户登录'


@user_bp.route('/del')
def del_user():
    # 获取你传递的username
    username = request.args.get('username')
    # 根据username找到列表中的user对象
    for user in users:
        if user.username == username:
            # 删除user
            users.remove(user)
            return redirect('/')
    else:
        return '删除失败'


@user_bp.route('/logout', methods=['GET', 'POST'])
def logout():
    return '用户退出'
