from flask import Flask

# 创建flask对象

app = Flask(__name__)
app.config.from_pyfile('settings.py')

products = [{'name': 'huawei p30', 'price': '5999', 'color': '黑色'},
            {'name': 'mi mate30', 'price': '3999', 'color': '红色'}, {
                'name': 'iphone 11', 'price': '10999', 'color': '黑色'}]


@app.route('/')
def hello_world():
    return 'HELLO hello world!hello kitty!'


@app.route('/product/<name>')
def get_product(name):
    for product in products:
        value = product.get('name')
        if name in value:
            return product


if __name__ == '__main__':
    # 启动flask
    app.run()
