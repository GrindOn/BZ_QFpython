import sys

# sys.stdin  接收用户的输入，说白了就是读取键盘里输入的数据

# stdout和stdin默认都是控制台
# sys.stdout 标准输出
# sys.stderr 错误输出

s_in = sys.stdin  # input就是读取 sys.stdin 里的数据

# while True:
#     content = s_in.readline().rstrip('\n')  # hello\n  ==>hello   \n==> ''
#     if content == '':
#         break
#     print(content)
m = open('stdout.txt', 'w', encoding='utf8')
sys.stdout = m
print('hello')
print('yes')
print('good')
m.close()

# err == > error 错误
x = open('stderr.txt', 'w', encoding='utf8')
sys.stderr = x
print(1 / 0)
x.close()
