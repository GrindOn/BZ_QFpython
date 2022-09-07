from flask import Flask

# 创建flask对象

app = Flask(__name__)
app.config.from_pyfile('settings.py')


# 路由+视图函数
@app.route('/')
def hello_world():  # ---->视图函数
    return 'HELLO hello world!hello kitty!'


@app.route('/abc',endpoint='abc1')
def show_abc():
    return '<h1>abc</h1>'

#  route就是将函数与add_url_rule进行了装饰
def show_name():
    return '千锋教育'


app.add_url_rule('/name', view_func=show_name)

if __name__ == '__main__':
    # 启动flask
    app.run()
