from applications import app, db
from applications.models import Users, Meals, Meal_Contents, Food_Items
from flask import render_template

@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return render_template('index.html')
