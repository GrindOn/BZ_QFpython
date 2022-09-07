import json
from wsgiref.simple_server import make_server


def demo_app(environ, start_response):
    path = environ['PATH_INFO']
    # print(environ.get('QUERY_STRING'))  # QUERY_STRING ==> 获取到客户端GET请求方式传递的参数
    # POST 请求数据的方式后面再说

    status_code = '200 OK'
    if path == '/':
        response = '欢迎来到我的首页'
    elif path == '/test':
        response = json.dumps({'name': 'zhangsan', 'age': 18})
    elif path == '/demo':
        with open('pages/xxxx.txt', 'r', encoding='utf8') as file:
            response = file.read()
    elif path == '/hello':
        with open('pages/hello.html', 'r', encoding='utf8') as file:
            response = file.read()
    elif path == '/info':
        # 查询数据库，获取到用户名
        name = 'jack'
        with open('pages/info.html', 'r', encoding='utf8') as file:
            # '{username}, 欢迎回来'.format(username=name)
            # flask  django  模板，渲染引擎
            response = file.read().format(username=name, age=18, gender='男')
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
