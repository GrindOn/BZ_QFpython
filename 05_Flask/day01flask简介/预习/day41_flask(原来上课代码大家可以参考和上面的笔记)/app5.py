from flask import Flask, url_for

# 创建flask对象
# import settings

app = Flask(__name__)
# app.config.from_object(settings)
app.config.from_pyfile('settings.py')


@app.route('/', endpoint='index')
def hello_world():
    return 'HELLO hello world!hello kitty!'


@app.route('/hello', endpoint='hello')  # 默认endpoint是函数名
def show_hello():
    return 'HELLO HELLO!'


@app.route('/abc')
def show_abc():
    result = url_for('hello')  # 反向解析路由
    print(result)  # /hello
    return 'show======>abc'


if __name__ == '__main__':
    # 启动flask
    app.run()
