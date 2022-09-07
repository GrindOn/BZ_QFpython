https://flask-wtf.readthedocs.io/en/stable/#
https://wtforms.readthedocs.io/en/2.3.x/

wtform
flask-wtf:集成了wtform，csrf的保护和文件上传功能，图形验证码。

使用：
1。安装：
pip3 install Flask-WTF

2。定义form.py:
在文件中中添加：

class UserForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])