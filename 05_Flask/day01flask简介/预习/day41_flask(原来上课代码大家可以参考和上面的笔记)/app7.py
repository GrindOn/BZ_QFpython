from flask import Flask, make_response, jsonify

# 创建flask对象
# import settings

app = Flask(__name__)
# app.config.from_object(settings)
app.config.from_pyfile('settings.py')


@app.route('/')
def hello_world():
    return 'HELLO hello world!hello kitty!'  # response对象


@app.route('/abc')
def show_abc():
    s = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
        <style>
           h1{
             color:red;
           }
        </style>
    </head>
    <body>
        <h1>ABC</h1>
    </body>
    </html>
    '''
    # response = make_response(s)
    # response.headers['name']='mytest'
    # return response
    return s


@app.route('/ab')
def show_ab():
    dict1 = {'name': 'admin', 'age': 20}
    list1 = [{'school': '100phone', 'students': [{'name': 'admin1', 'age': 19}, {'name': 'admin2', 'age': 20}]}, 1000]
    return jsonify(list1)


if __name__ == '__main__':
    # 启动flask
    app.run()
