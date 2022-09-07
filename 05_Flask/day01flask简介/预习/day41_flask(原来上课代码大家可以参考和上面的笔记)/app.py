from flask import Flask

app = Flask(__name__)
print(app.config)
app.config['ENV'] = 'development'


@app.route('/')
def hello_world():
    return 'HELLO hello world!hello kitty!lalallalalal'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
