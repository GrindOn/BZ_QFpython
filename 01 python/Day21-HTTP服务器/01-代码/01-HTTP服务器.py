import socket

# HTTP 服务器都是基于TCP的socket链接
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('192.168.31.199', 9090))
server_socket.listen(128)

# 获取的数据是一个元组，元组里有两个元素
# 第 0 个元素是 客户端的socket链接
# 第 1 个元素是 客户端的ip地址和端口号
while True:
    client_socket, client_addr = server_socket.accept()

    # 从客户端的 socket 里获取数据
    data = client_socket.recv(1024).decode('utf8')
    print('接收到{}的数据{}'.format(client_addr[0], data))

    # 返回内容之前，需要先设置HTTP响应头

    # 设置一个响应头就换一行
    client_socket.send('HTTP/1.1 200 OK\n'.encode('utf8'))
    client_socket.send('content-type:text/html\n'.encode('utf8'))

    # 所有的响应头设置完成以后，再换行
    client_socket.send('\n'.encode('utf8'))

    # 发送内容
    client_socket.send('<h1 style="color:red">hello world</h1>'.encode('utf8'))
