from applications import app, db
from applications.models import Users, Meals, Meal_Contents, Food_Items
from flask import render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateField, SubmitField

class DefaultForm(FlaskForm):
    first_name = StringField('First name: ')
    age = IntegerField('Age: ')
    birthdate = DateField('Birthdate: ', format='%dd-%mm-%yyyy')
    submit = SubmitField('Submit')

@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return render_template('home.html')

@app.route('/form', methods = ['GET','POST'])
def form():
    form = DefaultForm()
    message = ""

    name = form.first_name.data
    age = form.age.data
    birthdate = form.birthdate.data

    if request.method == 'POST':
        if len(name) == 0 and len(form.age.data) == 0 and len(form.birthdate.data) == 0:
            message = "All values must be filed"
        else:
            message = f"Welcome {name}, you are {age} and were born on {birthdate}"
    
    return render_template('form.html', form = DefaultForm(), message = message)