from flask import Flask, Response

import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route('/index')
def index():
    return {'a': '<h1>北京</h1>', 'b': '上海', 'c': '深圳'}  # application/json


@app.route('/index1')
def index1():
    return '<h1>北京</h1>'  # Content-Type:text/html; charset=utf-8


# return 后面返回的字符串其实也是做了一个response对象的封装。最终的返回结果还是response对象


@app.route('/index2')
def index2():
    return ('beijing', 'shanghai', 'shenzhen')


@app.route('/index3')
def index3():
    return Response('<h1>大家想好中午吃什么了吗？</h1>')  # 返回的Response对象


if __name__ == '__main__':
    app.run()
