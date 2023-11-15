from app.blueprints.home import home
from app.blueprints.posts import post


def init_app(app):
    app.register_blueprint(home)
    app.register_blueprint(post)