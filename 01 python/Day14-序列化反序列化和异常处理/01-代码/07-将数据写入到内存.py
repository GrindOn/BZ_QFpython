# 将数据写入到内存涉及到  StringIO和BytesIO两个类
from io import StringIO, BytesIO
from wsgiref import simple_server

s_io = StringIO()
# s_io.write('hello')  # 把数据写入到了内存里缓存起来了
# s_io.write('good')
# print(s_io.getvalue())
# s = ''
# s += 'hello'
# s += 'word'
# print(s)

# file 需要的是一个文件流对象
# print('hello', file=open('sss.txt', 'w'))
print('good', file=s_io)
print('yes', file=s_io)
print('ok', file=s_io)
print(s_io.getvalue())
s_io.close()

b_io = BytesIO()
b_io.write('你好'.encode('utf8'))
print(b_io.getvalue().decode('utf8'))
b_io.close()
