import socket


class MyServer(object):
    def __init__(self, ip, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((ip, port))
        self.socket.listen(128)

    def run_forever(self):
        while True:
            client_socket, client_addr = self.socket.accept()
            data = client_socket.recv(1024).decode('utf8')

            path = ''
            if data:
                path = data.splitlines()[0].split(' ')[1]

            response_header = 'HTTP/1.1 200 OK\n'

            if path == '/login':
                response_body = '欢迎来到登录页面'
            elif path == '/register':
                response_body = '欢迎来到注册页面'
            elif path == '/':
                response_body = '欢迎来到首页'
            else:
                response_header = 'HTTP/1.1 404 Page Not Found\n'
                response_body = '对不起，您要查看的页面不存在!!!'

            response_header += 'content-type:text/html;charset=utf8\n'
            response_header += '\n'

            response = response_header + response_body
            client_socket.send(response.encode('utf8'))


server = MyServer('0.0.0.0', 9090)
server.run_forever()
