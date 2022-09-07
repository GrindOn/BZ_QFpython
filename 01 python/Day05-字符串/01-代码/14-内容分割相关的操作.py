# split rsplit splitlines  partition  rpartition

# 字符串类型的数据
x = 'zhangsan-lisi-wangwu-jerry-henry-merry-jack-tony'
# ['zhangsan','lisi','wangwu','jerry','henry','merry','jack','tony']
# 使用split方法，可以将一个字符串切割成一个列表
y = x.split('-')
print(x)
print(y)  # 切割以后的结果就是一个列表

z = x.rsplit('-')
print(z)

print(x.split('-', 2))
print(x.rsplit('-', 2))

# partition 指定一个字符串作为分隔符，分为三部分
# 前面   分隔符   后面
print('abcdefXmpXqrst'.partition('X'))  # ('abcdef', 'X', 'mpXqrst')
print('abcdefXmpXqrst'.rpartition('X'))  # ('abcdefXmp', 'X', 'qrst')

# 获取文件名和后缀名
file_name = '2020.2.14拍摄不要打开.mp4'
print(file_name.rpartition('.'))
