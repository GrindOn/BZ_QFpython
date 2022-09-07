from flask import Flask

import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route('/')
def hello_world1():
    return 'Hello World111111!'


@app.route('/index')
def hello_world2():
    return 'Hello World222222!'


@app.route('/test')
def hello_world3():
    return '<font color="red"> Hello World333333! </font>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
