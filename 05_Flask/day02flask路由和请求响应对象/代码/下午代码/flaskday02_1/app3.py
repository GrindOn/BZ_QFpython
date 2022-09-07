from flask import Flask, Response, make_response

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
    s = '''
    <title>服务器内部错误</title>
    <h1>Not Found</h1>
    <p style='color:red;'>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
    '''
    return s, 500


@app.route('/index3')
def index3():
    response = Response('<h1>大家想好中午吃什么了吗？</h1>')  # 返回的Response对象
    print(response.content_type)
    print(response.headers)
    print(response.status_code)  # 200
    print(response.status)  # 200 OK

    response.set_cookie('name', '翔宇')
    return response


@app.route('/index4')
def index4():
    content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>首页</title>
    <style>
        div{
            width: 100%;
            height: 100px;
            border: 2px solid red;
        }
    </style>
</head>
<body>
<h1>欢迎来到京东购物网站</h1>
<div>
    <ul>
        <li>hello</li>
        <li>abc</li>
        <li>world</li>
    </ul>
</div>

</body>
</html>
    '''
    response = make_response(content)  # 返回值就是一个response对象
    # 定制响应头
    response.headers['mytest'] = '123abc'
    response.headers['myhello'] = 'hellohello'
    # 将定制好的response返回

    return response


if __name__ == '__main__':
    app.run()
