from applications import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    meals = db.relationship('meals', backref='User')

class Meals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meal_id = db.Column
    meals = db.relationship('Meal_Contents', backref='Meal')

class Meal_Contents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meal_id = db.Column(db.Integer, db.ForeignKey('meals.id'))
    food_item = db.Column(db.Integer, db.ForeignKey('food_items.id'))
    meals_rel = db.relationship('Food_Items', backref='Meal_Contents')

class Food_Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    food_name = db.Column(db.String(30), nullable=False)
    portion_weight = db.Column(db.Integer, nullable=False)    
    calories = portion_weight = db.Column(db.Integer, nullable=False)