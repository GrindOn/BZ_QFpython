import logging

from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['SECRET_KEY'] = 'hdf6735hjdfh8'

logger = logging.getLogger('app')
logger.setLevel(level=logging.WARNING)
handler = logging.FileHandler("log2.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


@app.route('/')
def index():
    logger.warning('首页的警告！！！！')
    app.logger.warning('首页警告2，。。。。。')
    return render_template('index.html')


@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 验证是否是admin
        username = request.form.get('username')
        if username == 'admin':
            flash('恭喜！验证成功啦！', 'info')
            flash('哈哈哈', 'error')
            flash(username, 'warning')
            return redirect(url_for('index'))
        else:
            # app.logger.debug('这是一个debug测试')
            # app.logger.error('这个是一个error测试')
            app.logger.warning('这个是一个warning测试')
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
