from app.blueprints.home import home
from app.blueprints.posts import post
from app.blueprints.categories import category


def init_app(app):
    app.register_blueprint(home)
    app.register_blueprint(post)
    app.register_blueprint(category)