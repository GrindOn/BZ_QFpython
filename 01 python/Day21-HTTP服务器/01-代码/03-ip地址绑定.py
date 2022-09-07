import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# ip地址只能通过ip地址访问
# server_socket.bind(('192.168.31.199', 8090))

# 能够通过 127.0.0.1 和 localhost 来访问
# server_socket.bind(('127.0.0.1', 8090))

# 127.0.0.1 和 0.0.0.0 都表示本机
# 0.0.0.0 表示所有的可用的地址
server_socket.bind(('0.0.0.0', 8090))

server_socket.listen(128)

while True:
    client_socket, client_addr = server_socket.accept()

    data = client_socket.recv(1024).decode('utf8')
    print('接收到{}的数据{}'.format(client_addr[0], data))

    client_socket.send('HTTP/1.1 200 OK\n'.encode('utf8'))
    client_socket.send('content-type:text/html\n'.encode('utf8'))
    client_socket.send('\n'.encode('utf8'))

    client_socket.send('<h1 style="color:red">hello world</h1>'.encode('utf8'))
