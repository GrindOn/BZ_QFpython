import pymysql, hashlib

username = input('请输入用户名:')
password = input('请输入密码:')

# 进行 md5 加密
h = hashlib.md5()
h.update(password.encode('utf8'))
password = h.hexdigest()

db = pymysql.connect(host='localhost',
                     user='root',
                     password='abcd1234',
                     database='python201',
                     port=3306,
                     charset='utf8')
cursor = db.cursor()

sql = 'select * from user where name="%s" and password="%s"'
print(sql)
# 执行sql语句
cursor.execute(sql, (username, password))

cursor.close()
db.commit()
db.close()

result = cursor.fetchone()
if not result:
    print('用户名或者密码错误')
else:
    print('欢迎回来{},您的信息是{}'.format(username, result))
