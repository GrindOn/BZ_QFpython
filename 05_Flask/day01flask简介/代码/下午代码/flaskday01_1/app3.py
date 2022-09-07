from flask import Flask

import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route('/')
def index():
    return '大家好！哈哈哈哈哈'


if __name__ == '__main__':
    app.run(port=8080)  # 设置端口号最好在启动之前设置
