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


def demo_app(environ, start_response):
    path = environ['PATH_INFO']

    status_code = '200 OK'
    if path == '/':
        response = '欢迎来到我的首页'
    elif path == '/test':
        response = json.dumps({'name': 'zhangsan', 'age': 18})
    elif path == '/demo':
        response = load_file('xxxx.txt')
    elif path == '/hello':
        response = load_file('hello.html')
    elif path == '/info':
        response = load_file('info.html', username='zhangsan', age=19, gender='male')
    else:
        status_code = '404 Not Found'
        response = '页面走丢了'

    start_response(status_code, [('Content-Type', 'text/html;charset=utf8')])
    return [response.encode('utf8')]


if __name__ == '__main__':
    httpd = make_server('', 8080, demo_app)
    sa = httpd.socket.getsockname()
    print("Serving HTTP on", sa[0], "port", sa[1], "...")
    httpd.serve_forever()
