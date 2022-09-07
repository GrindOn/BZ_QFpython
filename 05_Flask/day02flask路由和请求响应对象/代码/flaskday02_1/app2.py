from flask import Flask

import settings

app = Flask(__name__)
app.config.from_object(settings)


# 所有的路由搜索规则都是自上而下搜索，在写路由的是有定义的路由是唯一的。

@app.route('/projects')  # 请求路由中如果添加了/：http://127.0.0.1:5000/about/  显示Not Found
def about():
    return 'The about page'


@app.route('/projects/')  # 路由中定义'/'，无论请求的URL是否带有/，都可以执行视图函数。如果请求的是有/，浏览器做了一次重定向
def projects():
    return 'The project page'


if __name__ == '__main__':
    app.run()
