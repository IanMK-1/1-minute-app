from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from ..models import User


class UserRegistration(FlaskForm):
    username = StringField('Enter username', validators=[DataRequired()])
    email = StringField('Enter your email', validators=[DataRequired(), Email()])
    user_password = PasswordField('Enter password',
                                  validators=[DataRequired(),
                                              EqualTo('confirm_password', message='Password does not match')])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')
