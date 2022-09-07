import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('192.168.31.199', 9090))

# s.send('hello'.encode('utf8'))
file_name = input('清输入您要下载的文件名:')
s.send(file_name.encode('utf8'))

with open(file_name, 'wb') as file:
    while True:
        content = s.recv(1024)
        if not content:
            break
        file.write(content)

s.close()
