from flask_wtf import FlaskForm
from wtforms import StringField, FloatField

class AddSnackForm(FlaskForm):
  """form for adding snacks"""
  name = StringField("Snack name")
  price = FloatField("Price in USD")