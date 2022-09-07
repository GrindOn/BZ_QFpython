# app.py 与 模板的结合使用

from flask import Flask, request, render_template

import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route('/register1')
def register1():
    s = '''   
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>首页</title>
    <style>
        div{
            width: 100%;
            height: 200px;
            border: 2px solid red;
        }
    </style>
</head>
<body>
<h1>欢迎注册京东用户</h1>
<div>

    <form action="" method="get">
        <p><input type="text" placeholder="请输入用户名"></p>
        <p><input type="text" placeholder="请输入地址"></p>
        <p><input type="submit" value="提交"></p>
    </form>
</div>

</body>
</html>
    '''

    return s  # 自动封装成response对象


@app.route('/register')
def register():
    r = render_template('register.html')  # 默认去模板文件夹中找文件夹的，怎么就知道文件夹就是templates？
    # print(r)
    return r


@app.route('/register2', methods=['GET', 'POST'])
def register2():  # 获取页面提交的内容
    print(request.full_path)  # /register2?username=zhangsan&address=Beijing
    print(request.path)  # /register2
    print(request.args)  # dict类型  d = {'a':'aaa','b':'7878'}  d.get('b')  只能取到get请求的
    # print(request.args.get('username'))   # 获取值
    # print(request.args.get('address'))
    print(request.form)  # 如果请求方法是post则需要通过request.form取值
    print(request.form.get('username'))
    print(request.form.get('address'))
    return '进来了'


if __name__ == '__main__':
    print(app.url_map)  # 路由规则表
    app.run()
