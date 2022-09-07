https://flask-wtf.readthedocs.io/en/stable/#
https://wtforms.readthedocs.io/en/2.3.x/

wtform
flask-wtf:集成了wtform，csrf的保护和文件上传功能，图形验证码。

使用：
1。安装：
pip3 install Flask-WTF

全局使用csrf保护，
csrf = CSRFProtect(app=app)
必须需要设置SECRET_KEY这个配置项
app.config['SECRET_KEY'] = 'fgfhdf4564'


2。定义form.py:
在文件中中添加：

class UserForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])

各种：Field类型
StringField
PasswordField
IntegerField
DecimalField
FloatField
BooleanField
RadioField
SelectField
DatetimeField

各种的验证：
DataRequired
EqualTo
IPAddress
Length
NumberRange
URL
Email
Regexp



3.使用：
 视图中：
   .....
   form =UserForm()
   return render_template('user.html',form=form)

 模板中：
    <form action='' method=''>
      {{form.csrf_token}}
      {{form.name}}
      {{form.password}}
      <input type='submit' value=''/>
    </form>

4. 提交验证：
@app.route('/',methods=['GET','POST'])
def hello_world():
    uform = UserForm()
    if uform.validate_on_submit():   ------->主要通过validate_on_submit进行校验
        print(uform.name)
        print(uform.password)
        return '提交成功！'

    return render_template('user.html', uform=uform)


文件上传：
1。定义form
class UserForm(FlaskForm):
    。。。。。。
    # 上传使用的就是FileField，如果需要指定上传文件的类型需要使用：FileAllowed
    icon = FileField(label='用户头像', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif'], message='必须是图片文件格式')])

2。模板中的使用同其他类型的字段，但是必须在form上面：enctype="multipart/form-data"

3。视图函数中如果验证成功，通过：
        icon = uform.icon.data   -----》icon是FileStorage类型
        filename = secure_filename(icon.filename)
        icon.save(os.path.join(UPLOAD_DIR, filename))


