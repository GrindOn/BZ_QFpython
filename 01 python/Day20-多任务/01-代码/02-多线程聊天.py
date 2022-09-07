import socket, sys
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('192.168.31.199', 8080))


def send_msg():
    while True:
        msg = input('请输入您要发送的内容:')
        s.sendto(msg.encode('utf8'), ('192.168.31.199', 9090))
        if msg == 'exit':
            break


def recv_msg():
    while True:
        # data的数据类型是一个元组
        # 元组里第0个元素是接收到的数据
        # 元组里第1个元素是发送方的ip地址和端口号
        data, addr = s.recvfrom(1024)
        print('接收到了{}地址{}端口的消息:{}'.format(addr[0], addr[1], data.decode('utf8')),
              file=open('消息记录.txt', 'a', encoding='utf8'))


t1 = threading.Thread(target=send_msg)
t2 = threading.Thread(target=recv_msg)

t1.start()
t2.start()
