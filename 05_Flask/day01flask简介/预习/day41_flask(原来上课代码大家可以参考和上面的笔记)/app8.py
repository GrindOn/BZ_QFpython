from flask import Flask, render_template, request, redirect

# 创建flask对象
# import settings

app = Flask(__name__)
# app.config.from_object(settings)
app.config.from_pyfile('settings.py')

news = []


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        pass
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pass
    return render_template('login.html')


@app.route('/news')
def show_news():
    if not news:
        return render_template('404.html')
        # return redirect('/notfound')


@app.route('/notfound')
def not_found():
    return render_template('404.html')


if __name__ == '__main__':
    # 启动flask
    app.run()
