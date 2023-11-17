from flask import Blueprint, render_template, flash, redirect, url_for
from flask import current_app
from flask_login import login_user, logout_user
from app.forms import LoginForm
from app.models import User
from app.extensions import lm


@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


login = Blueprint('login', __name__)


@login.route('/login', methods=['get', 'post'])
def login_():
    form = LoginForm()
    if form.validate_on_submit():
        current_app.logger.info("Form passed validation!")
        user = User.query.filter_by(username=form.username.data).first()
        current_app.logger.info(f"User from database: {user}")
        if user and user.password == form.password.data:
            current_app.logger.info("Login successful!")
            login_user(user)
            return redirect(url_for('home.index'))
        else:
            flash('Invalid credentials')
    return render_template('login/login.html', form=form)


@login.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login.login_'))
