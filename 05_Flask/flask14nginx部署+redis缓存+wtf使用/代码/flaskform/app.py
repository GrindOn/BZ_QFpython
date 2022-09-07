from flask import Flask, render_template

from form import UserForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jfkdk73434kjfk3'
app.config['ENV'] = 'development'

@app.route('/')
def hello_world():
    uform = UserForm()
    return render_template('user.html', uform=uform)


if __name__ == '__main__':
    app.run(debug=True)
