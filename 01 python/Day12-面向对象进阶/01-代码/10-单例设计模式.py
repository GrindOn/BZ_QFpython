class Singleton:
    __instance = None  # 类属性
    __is_first = True

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            # 申请内存，创建一个对象，并把对象的类型设置为cls
            cls.__instance = object.__new__(cls)

        return cls.__instance

    def __init__(self, a, b):
        if self.__is_first:
            self.a = a
            self.b = b
            self.__is_first = False


# 调用 __new__ 方法申请内存
# 如果不重写 __new__ 方法，会调用 object 的 __new__ 方法
# object的 __new__ 方法会申请内存
# 如果重写了 __new__ 方法，需要自己手动的申请内存
s1 = Singleton('呵呵', '嘿嘿嘿')
s2 = Singleton('哈哈', '嘻嘻嘻')
s3 = Singleton('嘎嘎', '嘤嘤嘤')

print(s1 is s2)  # True
print(s1.a, s1.b)
