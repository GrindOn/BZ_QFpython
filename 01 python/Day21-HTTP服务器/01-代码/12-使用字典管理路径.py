import json
from wsgiref.simple_server import make_server


def load_file(file_name, **kwargs):
    try:
        with open('pages/' + file_name, 'r', encoding='utf8') as file:
            content = file.read()
            if kwargs:  # kwargs = {'username':'zhangsan','age':19,'gender':'male'}
                content = content.format(**kwargs)
                # {username},欢迎回来,你今年{age}岁了,你的性别是{gender}.format(**kwargs)
            return content
    except FileNotFoundError:
        print('文件未找到')


def index():
    return '欢迎来到我的首页'


def show_test():
    # return json.dumps({'name': 'zhangsan', 'age': 18})
    return json.dumps(['zhangsan', 'lisi', 'wangwu', 'jack'])


def show_demo():
    return load_file('xxxx.txt')


def show_hello():
    return load_file('hello.html')


def show_info():
    return load_file('info.html', username='zhangsan', age=19, gender='male')


def show_foo():
    return '我是foo'


url = {
    '/': index,
    '/test': show_test,
    '/demo': show_demo,
    '/hello': show_hello,
    '/info': show_info,
    '/foo': show_foo
}


def demo_app(environ, start_response):
    path = environ['PATH_INFO']
    status_code = '200 OK'

    method = url.get(path)
    if method:
        response = method()
    else:
        status_code = '404 Not Found'
        response = '页面走丢了'

    start_response(status_code, [('Content-Type', 'text/html;charset=utf8')])
    return [response.encode('utf8')]


if __name__ == '__main__':
    httpd = make_server('', 8090, demo_app)
    sa = httpd.socket.getsockname()
    print("Serving HTTP on", sa[0], "port", sa[1], "...")
    httpd.serve_forever()
