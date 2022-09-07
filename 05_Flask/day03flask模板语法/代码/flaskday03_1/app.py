import json

from flask import Flask, render_template, request, redirect, url_for

import settings

app = Flask(__name__)
app.config.from_object(settings)

users = []


@app.route('/', endpoint='index')
def index():
    return render_template('index.html')


@app.route('/add/<int:n1>/<int:n2>')
def add(n1, n2):
    if n1 > 0 and n2 > 0:
        r = n1 + n2
        return '运算结果是：' + str(r)
    return '输入的两个数必须大于零'


@app.route('/register', methods=['GET', 'POST'])
def register():
    print(request.method)
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        # 用户密码一致性验证
        if password == repassword:
            # 保存用户
            user = {'username': username, 'password': password}
            users.append(user)
            return redirect(url_for('index'))  # 有两次响应：1。302状态码 + location  2。 返回location请求地址内容
        else:
            return '两次密码不一致'

    return render_template('register.html')


@app.route('/show')
def show():
    # users[] ----> str''   json字符串
    j_str = json.dumps(users)
    return j_str


@app.route('/test')
def test():
    url = url_for('index')  # 路径反向解析
    print(url)  # /
    return 'test'


if __name__ == '__main__':
    app.run(port=5001)
