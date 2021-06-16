from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntergerField, DateField, SubmitField

class DefaultForm(FlaskForm):
    first_name = StringField('First name: ')
    age = IntergerField('Age: ')
    birthdate = DateField()
    Submit =SubmitField()