from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateField, SubmitField


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db" 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

class DefaultForm(FlaskForm):
    first_name = StringField('First name: ')
    age = IntegerField('Age: ')
    birthdate = DateField()
    Submit =SubmitField()

from applications import routes