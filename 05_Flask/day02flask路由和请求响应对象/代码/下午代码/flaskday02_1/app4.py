from flask import Flask, request, make_response

import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route('/index')
def index():
    # make_response()
    print(request.headers)  # request对象 对象访问属性，也可以调用方法
    print(request.path)
    print(request.full_path)
    print(request.base_url)
    print(request.url)

    return 'welcome everyone！'


if __name__ == '__main__':
    app.run()
