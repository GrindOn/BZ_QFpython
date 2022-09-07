from flask import Flask

import settings

app = Flask(__name__)
app.config.from_object(settings)

data = {'a': '北京', 'b': '上海', 'c': '深圳'}


@app.route('/')
def index():
    return '我是首页'


@app.route('/getcity/<key>')  # key就是一个变量名，默认是字符串类型的
def get_city(key):
    print(type(key))
    return data.get(key)


@app.route('/add/<int:num>')
def add(num):
    print('--->', type(num))
    result = num + 10
    return str(result)


@app.route('/add1/<float:money>')
def add1(money):
    print('====>', type(money))
    return str(money)


@app.route('/index/<path:p>')
def get_path(p):
    print('******>', type(p))  # str类型
    print(p)
    return p


@app.route('/test/<uuid:uid>')  # 必须传递uuid的格式，uuid模块， uuid.uuid4() ---->UUID类型
def test(uid):
    print('#######>>>>>', type(uid))
    return '获取唯一的标识码'


if __name__ == '__main__':

    app.run()
