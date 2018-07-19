from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,TextAreaField
from wtforms.validators import DataRequired


class EditForm(FlaskForm):
    title=StringField('Tilte',validators=[DataRequired()])
    text=TextAreaField('Text',validators=[DataRequired()])
    submit=SubmitField('Submit')



