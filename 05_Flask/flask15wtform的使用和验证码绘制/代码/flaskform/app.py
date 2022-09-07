import os
from io import BytesIO

from flask import Flask, render_template, request, make_response, session
from flask_bootstrap import Bootstrap
from flask_wtf import CSRFProtect
from werkzeug.utils import secure_filename

from form import UserForm
from util import generate_image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')
UPLOAD_DIR = os.path.join(STATIC_DIR, 'upload')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jfkdk73434kjfk3'
app.config['ENV'] = 'testing'
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'
app.config['RECAPTCHA_PRIVATE_KEY	'] = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'
app.config['RECAPTCHA_PARAMETERS'] = {'hl': 'zh', 'render': 'explicit'}
app.config['RECAPTCHA_DATA_ATTRS'] = {'theme': 'dark'}

csrf = CSRFProtect(app=app)
bootstrap = Bootstrap(app=app)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    uform = UserForm()
    if uform.validate_on_submit():
        name = uform.name.data
        password = uform.password.data
        phone = uform.phone.data
        icon = uform.icon.data
        filename = secure_filename(icon.filename)
        icon.save(os.path.join(UPLOAD_DIR, filename))
        return '提交成功！'

    return render_template('user.html', uform=uform)


@app.route('/image')
def get_image():
    im, code = generate_image(4)
    # 将image对象转成二进制
    buffer = BytesIO()
    im.save(buffer, "JPEG")
    buf_bytes = buffer.getvalue()
    # 保存到session中
    session['valid'] = code
    response = make_response(buf_bytes)
    response.headers['Content-Type'] = 'image/jpg'
    return response

# form与bootstrap结合使用
@app.route('/user',methods=['GET', 'POST'])
def boot_form_user():
    uform = UserForm()
    return  render_template('user1.html',uform=uform)



if __name__ == '__main__':
    app.run(debug=True)
