from applications import app, db
from applications.models import Users, Meals, Meal_Contents, Food_Items
from flask import render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateField, SubmitField

class DefaultForm(FlaskForm):
    first_name = StringField('First name: ')
    age = IntegerField('Age: ')
    birthdate = DateField('Birthdate: ', format ="%d-%m-%y")
    submit = SubmitField('Submit')

@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return render_template('home.html')

@app.route('/form', methods = ['GET','POST'])
def user_submit():

    form = DefaultForm()

    message = ""

    name = form.first_name.data
    age = str(form.age.data)
    birthdate = str(form.birthdate.data)

    if request.method == 'POST':
        if name == "" or age == "" or birthdate == None:
            message = "All values must be filled"
        else:
            message = f"Welcome {name}, you are {age} and were born on {birthdate}"
    
    return render_template('form.html', form = form, message = message)