# 加密: md5  sha1  sha256  sha512

import hashlib

#
msg = 'hello world'
md5 = hashlib.md5(msg.encode('utf-8'))
print(md5)  # 32
r = md5.hexdigest()
print(r)

sha1 = hashlib.sha1(msg.encode('utf-8')).hexdigest()
print(sha1)  # 40

sha256 = hashlib.sha256(msg.encode('utf-8')).hexdigest()
print(sha256)  # 64

sha512 = hashlib.sha512(msg.encode('utf-8')).hexdigest()
print(sha512)  # 128
