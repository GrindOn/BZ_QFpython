# {} 也可以进行占位

# {} 什么都不写，会读取后面的内容，一一对应填充
x = '大家好，我是{},我今年{}岁了'.format('张三', 18)
print(x)

# {数字} 根据数字的顺序来进行填入。数字从 0 开始
y = '大家好，我是{1},我今年{0}岁了'.format(20, 'jerry')
print(y)

# {变量名}
z = '大家好，我是{name},我今年{age}岁了,我来自{addr}'.format(age=18, name='jack', addr='襄阳')
print(z)

# 混合使用  {数字}  {变量}
a = '大家好，我是{name},我今年{1}岁了,我来自{0}'.format('泰国', 23, name='tony')
print(a)

# {}什么都不写  {数字} 不能混合使用

d = ['zhangsan', 18, '上海', 180]
# b = '大家好，我是{},我今年{}岁了,我来自{},身高{}cm'.format(d[0], d[1], d[2], d[3])
b = '大家好，我是{},我今年{}岁了,我来自{},身高{}cm'.format(*d)
print(b)

info = {'name': 'chris', 'age': 23, 'addr': '北京', 'height': 190}
c = '大家好，我是{name},我来自{addr},身高{height}cm,我今年{age}岁了'.format(**info)
print(c)
