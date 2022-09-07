import socket, os

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('192.168.31.199', 9090))
server_socket.listen(128)

# 接收客户端的请求
client_socket, client_addr = server_socket.accept()
file_name = client_socket.recv(1024).decode('utf8')

# print('接收到了来自{}地址{}端口的数据，内容是:{}'.format(client_addr[0], client_addr[1], data))
if os.path.isfile(file_name):
    # print('读取文件，返回给客户端')
    with open(file_name, 'rb') as file:
        content = file.read()
        client_socket.send(content)
else:
    print('文件不存在')
