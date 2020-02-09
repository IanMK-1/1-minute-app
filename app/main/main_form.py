from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired


class UpdateBio(FlaskForm):
    bio = TextAreaField('Your bio.', validators=[DataRequired()])
    submit = SubmitField('Submit')
