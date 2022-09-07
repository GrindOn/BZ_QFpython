import socket

# 不同电脑之间的通信需要使用socket
# socket可以在不同的电脑间通信;还可以在同一个电脑的不同程序之间通信

# 1. 创建socket,并连接
# AF_INET:表示这个socket是用来进行网络连接
# SOCK_DGRAM:表示连接是一个 udp 连接
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. 发送数据
# data:要发送的数据，它是二进制的数据
# address:发送给谁，参数是一个元组，元组里有两个元素
# 第0个表示目标的ip地址，第1个表示程序的端口号

# 给 192.168.31.199 这台主机的 9000 端口上发送了 hello
# 端口号:0~65536  0~1024 不要用，系统一些重要的服务在使用
# 找一个空闲的端口号
s.sendto('下午好'.encode('utf8'), ('192.168.31.199', 9090))

# 3. 关闭socket
s.close()
