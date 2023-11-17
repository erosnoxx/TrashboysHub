from wtforms.fields import StringField, SubmitField, DateField, BooleanField, PasswordField, TextAreaField, SelectField, FileField
from wtforms.validators import Email, DataRequired, Length
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


class UserForm(FlaskForm):
    fullname = StringField('Full Name', validators=[DataRequired(), Email(), Length(max=50)])
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=255)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=255)])
    gender = SelectField('Gender', coerce=str, validators=[DataRequired()])
    birth = DateField('Date of Birth', validators=[DataRequired()])
    submit = SubmitField('Register')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        gender_choices = ['Male', 'Female', 'Transgender', 'Non-Binary', 'Other']
        self.gender.choices = [(choice, choice) for choice in gender_choices]


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=15)])
    password = password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=255)])
    submit = SubmitField('Login')