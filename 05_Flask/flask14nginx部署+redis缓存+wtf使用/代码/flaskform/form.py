from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField
from wtforms.validators import DataRequired, Length


class UserForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(), Length(min=6, max=12, message='用户名长度必须在6～12位之间')])
    password = PasswordField('password',validators=[DataRequired(), Length(min=6, max=12, message='密码长度必须在6～12位之间')])
