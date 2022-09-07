# print(__name__)
from flask import Flask

app = Flask(__name__)


# 装饰器

@app.route('/')   # 路由  URL  http://127.0.0.1:5000/
def index():  # 视图函数   mtv： view 视图   函数
    return '哈哈哈哈哈哈'


# WSGI: Python Web Server Gateway Interface  是为Python语言定义的Web服务器和Web应用程序或框架之间的一种简单而通用的接口
app.run()
# flask 内置服务器   nginx

# pip install flask
