from flask_wtf import FlaskForm
from wtforms import StringField,TextField,TextAreaField,PasswordField,IntegerField,SubmitField
from wtforms.validators import equal_to,email,length,data_required,required,regexp,ValidationError

class myForm (FlaskForm):
    name = StringField("姓名：",validators=[data_required()])
    age = IntegerField("年龄：",validators=[data_required()])
    email = StringField("邮箱")
    password = PasswordField("密码：",validators=[data_required(),length(1,8),regexp('^[A-Za-z][A-Za-z0-9_.]*$',0,'密码必须字母开头由字母数字及下划线组成')])
    confirm = PasswordField("确认密码",validators=[equal_to('password','两次密码不一致')])
    submit = SubmitField('发送')
#自定义验证（例如和数据库比对是否重复）
    def validate_email(form,field):
        if field.data == '':
            raise  ValidationError('邮箱不能为空')


