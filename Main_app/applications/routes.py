from applications import app, db
from applications.models import FoodItems
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

        food_item = form.food_item.data
        portion_weight = form.portion_weight.data
        calories = form.portion_calories.data

        new_food_item = FoodItems(food_name = food_item, item_weight = portion_weight, item_calories = calories)
        db.session.add(new_food_item)
        db.session.commit()

        message = "Item added!"
  
    
    return render_template('add_items.html', form = form, message = message)

@app.route('/read')
def read():
    all_food_items = FoodItems.query.all()
    food_string = ""
    for item in all_food_items:
        food_string += str(item.id) + "<br>" + str(item.food_name) + "<br>" + str(item.item_weight) + "<br>" + str(item.item_calories)

    return food_string