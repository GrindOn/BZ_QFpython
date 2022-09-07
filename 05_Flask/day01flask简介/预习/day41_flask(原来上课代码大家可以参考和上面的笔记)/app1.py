from flask import Flask
# 创建flask对象
# import settings

app = Flask(__name__)
# app.config.from_object(settings)
app.config.from_pyfile('settings.py')

@app.route('/')
def hello_world():
    return 'HELLO hello world!hello kitty!'


if __name__ == '__main__':
    # 启动flask
    app.run()
