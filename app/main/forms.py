from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired

class GroupForm(FlaskForm):
    name =  StringField('Category Name', validators=[DataRequired()])
    submit = SubmitField('Create')

class PitchForm(FlaskForm):
    pitch_content =  StringField('One Minute Pitch', validators=[DataRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment_content =  TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Submit')

