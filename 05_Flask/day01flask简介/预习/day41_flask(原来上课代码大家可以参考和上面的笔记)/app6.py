from flask import Flask, request, render_template

# 创建flask对象

# app = Flask(__name__,template_folder='templates')
app = Flask(__name__)
app.config.from_pyfile('settings.py')


@app.route('/')
def hello_world():
    print(request)  # <Request 'http://127.0.0.1:5000/?name=admin' [GET]>

    '''
    path
    full_path
    script_root
    url
    base_url
    url_root
    '''
    print(request.path)  # /
    print(request.full_path)  # /?name=admin
    print(request.url)  # http://127.0.0.1:5000/?name=admin
    print(request.base_url)  # http://127.0.0.1:5000/
    print(request.url_root)
    print(request.method)  # 'GET'
    print(request.query_string)  # b'name=admin'

    return 'HELLO hello world!hello kitty!'


black_list = ['10.0.102.118', '10.0.102.94']


@app.route('/login', methods=['GET', 'POST'])
def user_login():
    print(request.remote_addr)
    if request.remote_addr in black_list:
        return '哈哈哈你什么都看不到啦'
    # request.method 获取请求的方式
    if request.method == 'GET':
        print(request.args.get('a'))  # ?a=100&b=99    request.args 字典对象  request.args.get('a')  ---->100
        return render_template('register.html')
    else:
        # 获取提交的数据
        # print(request.form)
        # print(request.values)
        username = request.form.get('username')
        password = request.form.get('password')
        # result = request.get_json()
        # result = request.get_data()
        # print(result)
        return 'username：' + username + ',password:' + password
        # return 'POST!'


if __name__ == '__main__':
    # 启动flask
    app.run(host='0.0.0.0')
