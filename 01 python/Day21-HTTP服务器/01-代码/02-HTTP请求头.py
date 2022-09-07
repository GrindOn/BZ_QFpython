import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('192.168.31.199', 8090))
server_socket.listen(128)
while True:
    client_socket, client_addr = server_socket.accept()
    data = client_socket.recv(1024).decode('utf8')
    print('接收到{}的数据{}'.format(client_addr[0], data))
    """
    # GET 请求方式，GET/POST/PUT/DELETE... ...
    # /index.html?name=jack&age=18 请求的路径以及请求参数
    # HTTP/1.1  HTTP版本号
    GET /index.html?name=jack&age=18 HTTP/1.1
    
    Host: 192.168.31.199:8090   # 请求的服务器地址
    
    Upgrade-Insecure-Requests: 1
    # UA 用户代理，最开始设计的目的，是为了能从请求头里辨识浏览器的类型
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
    Accept-Encoding: gzip, deflate
    Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
    Connection: close
    """

    client_socket.send('HTTP/1.1 200 OK\n'.encode('utf8'))
    client_socket.send('content-type:text/html\n'.encode('utf8'))
    client_socket.send('\n'.encode('utf8'))

    client_socket.send('<h1 style="color:red">hello world</h1>'.encode('utf8'))
