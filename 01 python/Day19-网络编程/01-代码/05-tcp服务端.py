import socket

# 创建一个socket连接
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.31.199', 9090))

s.listen(128)  # 把socket变成一个被动监听的socket

# (
# <socket.socket fd=512, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('192.168.31.199', 9090), raddr=('192.168.31.185', 38096)>,
# ('192.168.31.185', 38096)
# )
# 接收到的结果是一个元组，元组里有两个元素
# 第 0 个元素是客户端的socket连接，第 1 个元素是客户端的 ip 地址和端口号
# x = s.accept()  # 接收客户端的请求

client_socket, client_addr = s.accept()

# udp里接收数据，使用的recvfrom
data = client_socket.recv(1024)  # tcp里使用recv获取数据
print('接收到了{}客户端{}端口号发送的数据，内容是:{}'.format(client_addr[0], client_addr[1], data.decode('utf8')))
