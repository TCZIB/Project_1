from applications import app, db
from applications.models import Users, Meals, Meal_Contents, Food_Items
from applications.forms import Food_Item_Form
from flask import render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateField, SubmitField
from wtforms.validators import ValidationError


@app.route('/add_item', methods = ['GET','POST'])
def add_item_page():
    form = Food_Item_Form()
    message = ""

    if form.validate_on_submit():
        return str(form.validate_on_submit())
        message = "Item added!"
    
    return render_template('add_items.html', form = form, message = message)