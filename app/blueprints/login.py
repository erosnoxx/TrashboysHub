import secrets
from hashlib import sha256
from flask import Blueprint, render_template, redirect, url_for, session, current_app, flash
from flask_login import login_user, logout_user
from app.forms import LoginForm, UserForm, VerificationForm
from app.models import User, User_Permissions, Permissions
from app.extensions import lm, db
from datetime import datetime
from app.mail import send_email


def generate_otp():
    return secrets.randbelow(10**7 - 1) + 10**6


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

        session['new_user'] = {
            'fullname': form.fullname.data,
            'username': form.username.data,
            'email': form.email.data,
            'password': hashed_password,
            'salt': salt,
            'gender': form.gender.data,
            'birth': form.birth.data,
            'reg_date': datetime.now().date()
        }

        session['otp'] = generate_otp()
        otp = session.get('otp')
        user_email = session['new_user']['email']

        send_email(subject='Trashboys Hub | E-mail Verification',
                body=f'Your verification code is: {otp}. Please enter your verification code on the site.',
                to=user_email)

        return redirect(url_for('login.otp'))
    return render_template('register/register.html', form=form)


@login.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login.login_'))


@login.route('/register/verification', methods=['get', 'post'])
def otp():
    form = VerificationForm()
    otp = session.get('otp')
    
    if form.validate_on_submit():
        if form.otp.data == otp:
            birth_date_str = session['new_user']['birth']
            reg_date_str = session['new_user']['reg_date']
            birth_date = datetime.strptime(birth_date_str, '%a, %d %b %Y %H:%M:%S %Z').date()
            reg_date = datetime.strptime(reg_date_str, '%a, %d %b %Y %H:%M:%S %Z').date()
            session['new_user']['birth'] = birth_date
            session['new_user']['reg_date'] = reg_date

            existing_username = User.query.filter(User.username == session['new_user']['username']).first()
            existing_email = User.query.filter(User.email == session['new_user']['email']).first()


            if not existing_username and not existing_email:
                new_user = User(**session['new_user'])
                db.session.add(new_user)
                db.session.commit()

                default_permission = Permissions.query.filter_by(level='user').first()
                user_permission = User_Permissions(user_id=new_user.id,
                                                permission_id=default_permission.id)
                db.session.add(user_permission)
                db.session.commit()

                return redirect(url_for('login.login_'))
            else:
                flash('User already register')

    return render_template('register/otp.html', form=form)