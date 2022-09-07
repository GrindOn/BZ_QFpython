import hashlib
import hmac

# 这两个模块都是用来进行数据加密
# hashlib模块里主要支持两个算法  md5 和  sha 加密
# 加密方式: 单向加密:只有加密的过程，不能解密md5/sha   对称加密   非对称加密rsa

# 需要将要加密的内容转换成为二进制
x = hashlib.md5('y239ym23r9b!'.encode('utf8'))  # 生成一个md5对象
# x.update('y239ym23r9b!'.encode('utf8'))
print(x.hexdigest())  # 900150983cd24fb0d6963f7d28e17f72
# 'abc'  ==>  900150983cd24fb0d6963f7d28e17f72


h1 = hashlib.sha1('123456'.encode())
print(h1.hexdigest())  # 7c4a8d09ca3762af61e59520943dc26494f8941b
h2 = hashlib.sha224('123456'.encode())  # 224位  一个十六进制占4位
print(h2.hexdigest())  # f8cdb04495ded47615258f9dc6a3f4707fd2405434fefc3cbf4ef4e6
h3 = hashlib.sha256('123456'.encode())
print(h3.hexdigest())  # 8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92
h4 = hashlib.sha384('123456'.encode())
print(
    h4.hexdigest())  # 0a989ebc4a77b56a6e2bb7b19d995d185ce44090c13e2984b7ecc6d446d4b61ea9991b76a4c2f04b1b4d244841449454

# hmac 加密可以指定秘钥
h = hmac.new('h'.encode(), '你好'.encode())
result = h.hexdigest()
print(result)  # 获取加密后的结果
