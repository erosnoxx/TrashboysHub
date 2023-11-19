from app.blueprints.home import home
from app.blueprints.posts import post
from app.blueprints.categories import category
from app.blueprints.media import media
from app.blueprints.login import login


def init_app(app):
    app.register_blueprint(home)
    app.register_blueprint(post)
    app.register_blueprint(category)
    app.register_blueprint(media)
    app.register_blueprint(login)
