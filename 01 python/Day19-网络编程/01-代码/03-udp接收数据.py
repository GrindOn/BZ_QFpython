import socket

# 创建一个基于 udp 的网络socket连接
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口号和ip地址
s.bind(('192.168.31.199', 9090))

# recvfrom 接收数据
# content = s.recvfrom(1024)
# print(content)
# 接收到的数据是一个元组，元组里有两个元素
# 第 0 个元素是接收到的数据，第 1 个元素是发送方的 ip地址和端口号

data, addr = s.recvfrom(1024)  # recvfrom是一个阻塞的方法，等待
print('从{}地址{}端口号接收到了消息，内容是:{}'.format(addr[0], addr[1], data.decode('utf8')))

s.close()
