import pymysql

# host 指的是数据库服务器的主机地址
# user 连接数据库的用户

# 打开一个数据库的连接，获取一个db对象
# db = pymysql.connet()  # 结果是一个Connection类型的对象
# db.cursor()   获取到一个cursor对象，用它来操作数据库

# with 语句上下文管理器，会调用对象的 __enter__ 方法，获取enter方法的执行结果
# with pymysql.connect() as x  # x的结果就是一个cursor对象

db = pymysql.connect(host='localhost',
                     user='root',
                     password='abcd1234',
                     database='python201',
                     port=3306,
                     charset='utf8')
cursor = db.cursor()
cursor.execute('select * from student')
cursor.close()
db.commit()
db.close()

for info in cursor.fetchall():
    print(info)
