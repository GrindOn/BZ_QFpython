from wsgiref.simple_server import make_server


def demo_app(environ, start_response):
    path = environ['PATH_INFO']
    print('path= {}'.format(path))
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf8'), ('sss', 'dddd')])
    return ['你好'.encode('utf8')]


if __name__ == '__main__':
    httpd = make_server('', 8080, demo_app)
    sa = httpd.socket.getsockname()
    print("Serving HTTP on", sa[0], "port", sa[1], "...")
    httpd.serve_forever()
