import uuid
from flask import Flask

# 创建flask对象
app = Flask(__name__)
app.config.from_pyfile('settings.py')


@app.route('/')
def hello_world():
    return 'HELLO hello world!hello kitty!'


@app.route('/product/<uuid:uid>')
def show_uuid(uid):
    # uid = uuid.uuid4()
    print(type(uid))
    return '==========>' + str(uid)


@app.route('/product/<name>')
def show_product1(name):
    return '------>' + name


@app.route('/product/<int:page>')
def show_product(page):
    print(type(page))  # <class 'int'>
    return '当前请求的是第' + str(page) + '页数据！'


@app.route('/product/<float:price>')  # http://127.0.0.1:5000/product/2.9
def show_product2(price):  # price=2.9
    print(type(price))  # <class 'int'>
    return '当前商品的价格是:' + str(price)


@app.route('/product/<path:pp>')
def show_path(pp):
    print(type(pp))
    return '得到的是:' + pp


# d3801297-6be8-4be8-9e10-28d2595c976e
@app.route('/product')
def show_aaa():
    return '=======商品======='


if __name__ == '__main__':
    # 启动flask
    app.run()
