from typing import Any
from wtforms.fields import StringField, SubmitField, BooleanField, TextAreaField, SelectField, FileField
from flask_wtf import FlaskForm
from app.models import Category

class CategoryForm(FlaskForm):
    name = StringField('Name')
    submit = SubmitField('Save')


class PostForm(FlaskForm):
    title = StringField('Title')
    text = TextAreaField('Text')
    published = BooleanField('Published')
    categories = SelectField('Category', coerce=int)
    image = FileField('Image')
    submit = SubmitField('Save')

    def __init__(self):
        super(PostForm, self).__init__()
        self.categories.choices = [(c.id, c.name) for c in Category.query.all()]