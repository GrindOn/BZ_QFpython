from flask import session
from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, ValidationError, EqualTo, Regexp
import re


class UserForm(FlaskForm):
    name = StringField(label='用户名', validators=[DataRequired(), Length(min=6, max=12, message='用户名长度必须在6～12位之间')])
    password = PasswordField(label='密码', validators=[DataRequired(), Length(min=6, max=12, message='密码长度必须在6～12位之间')])
    confirm_pwd = PasswordField(label='确认密码',
                                validators=[DataRequired(), Length(min=6, max=12, message='密码长度必须在6～12位之间'),
                                            EqualTo('password', '两次密码不一致')])
    phone = StringField(label='手机号码', validators=[DataRequired(), Length(min=11, max=11, message='手机号码必须11位长度')])
    icon = FileField(label='用户头像', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'gif'], message='必须是图片文件格式')])
    recaptcha = StringField(label='验证码')

    def validate_recaptcha(self, data):
        input_code = data.data
        code = session.get('valid')
        if input_code.lower() != code.lower():
            raise ValidationError('验证码错误')

    def validate_name(self, data):
        # print('----->', type(self.name))
        # print('=====>', type(data))
        if self.name.data[0].isdigit():
            raise ValidationError('用户名不能以数字开头')

    def validate_phone(self, data):
        phone = data.data
        if not re.search(r'^1[35678]\d{9}$', phone):
            raise ValidationError('手机号码格式错误')
