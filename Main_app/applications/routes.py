from applications import app, db
from applications.models import FoodItems
from applications.forms import Food_Item_Form
from flask import render_template, request, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateField, SubmitField
from wtforms.validators import ValidationError

@app.route('/')
def home_page():

    return render_template('index.html')

@app.route('/add_item', methods = ['GET','POST'])
def add_item_page():
    form = Food_Item_Form()
    message = ""

    if form.validate_on_submit():

        food_item = form.food_item.data
        portion_weight = form.portion_weight.data
        calories = form.portion_calories.data

        new_food_item = FoodItems(food_name = food_item, item_weight = portion_weight, item_calories = calories)
        db.session.add(new_food_item)
        db.session.commit()

        message = "Item added!"

    if form.validate_on_submit():
        print("Done")
  
    return render_template('add_items.html', form = form, message = message, items = FoodItems.query.all())

@app.route('/view_meals')
def view_meals():
    return "Meals"

@app.route('/food_items')
def food_items():

    return render_template('food_items.html', items = FoodItems.query.all())