from flask import Blueprint, render_template
from flask_login import login_required
from app.extensions import lm
from app.models import Post

home = Blueprint('home', __name__)
lm.login_view = 'login.login_'


@home.route('/')
@login_required
def index():
    posts = Post.query.filter_by(published=True).all()

    return render_template('home/index.html', posts=posts)