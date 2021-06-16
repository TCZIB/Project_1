from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateField, SubmitField
from wtforms.validators import Length, DataRequired, ValidationError

class Food_Item_Form(FlaskForm):
    food_item = StringField('Food Item: ', validators=[DataRequired(), Length(min=1, max=30)])
    portion_weight = IntegerField('Weight (g): ', validators=[DataRequired()])
    calories = IntegerField('Calories: ', validators=[DataRequired()])
    submit = SubmitField()

    def validate_portion_weight(self, portion_weight):
        if list(str(portion_weight.data))[:-1].lower() == "g":
            raise ValidationError("Please only enter a number")