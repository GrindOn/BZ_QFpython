import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 8090))
server_socket.listen(128)

while True:
    client_socket, client_addr = server_socket.accept()
    data = client_socket.recv(1024).decode('utf8')

    path = ''
    if data:  # # 浏览器发送过来的数据有可能是空的
        path = data.splitlines()[0].split(' ')[1]
        print('请求的路径是{}'.format(path))

    response_body = 'hello world'

    # 响应头
    response_header = 'HTTP/1.1 200 OK\n'  # 200 OK 成功了

    if path == '/login':
        response_body = '欢迎来到登录页面'
    elif path == '/register':
        response_body = '欢迎来到注册页面'
    elif path == '/':
        response_body = '欢迎来到首页'
    else:
        # 页面未找到   404 Page Not Found
        response_header = 'HTTP/1.1 404 Page Not Found\n'
        response_body = '对不起，您要查看的页面不存在!!!'

    response_header += 'content-type:text/html;charset=utf8\n'
    response_header += '\n'

    # 响应
    response = response_header + response_body
    # 发送给客户端
    client_socket.send(response.encode('utf8'))
