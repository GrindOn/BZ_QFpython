from flask import Flask

app = Flask(__name__)
# print(app.config)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True



@app.route('/')
def index():
    return '欢迎大家！～～～～hhahhaha'


if __name__ == '__main__':
    app.run(port=8080)
