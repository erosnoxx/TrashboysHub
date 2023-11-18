import secrets
from hashlib import sha256
from flask import Blueprint, render_template, redirect, url_for
from flask import current_app
from flask_login import login_user, logout_user
from app.forms import LoginForm, UserForm
from app.models import User, User_Permissions, Permissions
from app.extensions import lm, db
from datetime import datetime


def generate_salt():
    return secrets.token_hex(16)


def hash_password(password, salt):
    hashed_password = sha256((password + salt).encode('utf-8')).hexdigest()
    return hashed_password

@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


login = Blueprint('login', __name__)


@login.route('/login', methods=['get', 'post'])
def login_():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user and hash_password(form.password.data, user.salt) == user.password:
            login_user(user)
            return redirect(url_for('home.index'))
    return render_template('login/login.html', form=form)


@login.route('/register', methods=['get', 'post'])
def register():
    form = UserForm()
    if form.validate_on_submit():
        salt = generate_salt()
        hashed_password = hash_password(form.password.data, salt)

        new_user = User(
            fullname=form.fullname.data,
            username=form.username.data,
            email=form.email.data,
            password=hashed_password,
            salt=salt,
            gender=form.gender.data,
            birth=form.birth.data,
            reg_date=datetime.now().date()
        )

        db.session.add(new_user)
        db.session.commit()

        default_permission = Permissions.query.filter_by(level='user').first()
        user_permission = User_Permissions(user_id=new_user.id,
                                           permission_id=default_permission.id)
        db.session.add(user_permission)
        db.session.commit()

        return redirect(url_for('login.login_'))
    return render_template('login/register.html', form=form)


@login.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login.login_'))
