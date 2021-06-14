from flask_wtf import FlaskForm
from wtforms import TextAreaField, IntegerField
from wtforms.validators import DataRequired, ValidationError


def check_rating(form, field):
    print("Checking if rating is valid", field.data)
    rating = field.data
    if rating > 5 and rating < 1:
        raise ValidationError("Rating value is invalid.")

class ReviewForm(FlaskForm):
    rating = IntegerField('rating', validators=[DataRequired(), check_rating])
    body = TextAreaField('body', validators=[DataRequired()])
    productId = IntegerField('productId', validators=[DataRequired()])
    userId = IntegerField('userId', validators=[DataRequired()])