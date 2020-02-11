from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, StringField, SelectField
from wtforms.validators import DataRequired


class UpdateBio(FlaskForm):
    bio = TextAreaField('Your bio.', validators=[DataRequired()])
    submit = SubmitField('Submit')


class UserPitchForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    pitch = TextAreaField('Write your Pitch', validators=[DataRequired()])
    type = SelectField('Type', choices=[('product', 'Product pitch'), ('pick up lines', 'Pick Up lines pitch'),
                                        ('interview', 'Interview pitch'), ('promotion', 'Promotion pitch')])
    submit = SubmitField('Submit')


class UserCommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('submit')
