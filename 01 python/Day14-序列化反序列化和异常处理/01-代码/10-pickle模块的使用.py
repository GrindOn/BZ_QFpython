# python 里存入数据只支持存入 字符串 和 二进制
# json: 将Python里的数据(str/list/tuple/dict/int/float/bool/None)等转换成为对应的json
# pickle: 将Python里任意的对象转换成为二进制

import pickle

# 序列化  dumps:将Python数据转换成为二进制
#         dump:将Python数据转换成为二进制，同时保存到指定文件
# 反序列化 loads:将二进制加载成为Python数据
#         load:读取文件，并将文件的二进制内容加载成为Python数据
names = ['张三', '李四', '杰克', '亨利']


# b_names = pickle.dumps(names)
#
# file = open('names.txt', 'wb')
# file.write(b_names)  # 写入的是二进制，不是存文本
# file.close()
#
# file1 = open('names.txt', 'rb')
# x = file1.read()
# y = pickle.loads(x)
# print(y)
# file1.close()

# file2 = open('names.txt', 'wb')
# pickle.dump(names, file2)
# file2.close()
#
# file3 = open('names.txt', 'rb')
# pickle.load(file3)

class Dog(object):
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def eat(self):
        print(self.name + '正在吃东西')


d = Dog('大黄', '白色')

# 保存到文件里
pickle.dump(d, open('dog.txt', 'wb'))

# 从文件里加载出来
dd = pickle.load(open('dog.txt', 'rb'))
dd.eat()
print(dd.name, dd.color)
