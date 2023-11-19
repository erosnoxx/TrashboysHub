from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


db = SQLAlchemy()
lm = LoginManager()


def init_app(app):
    db.init_app(app)
    Migrate(app, db)
    lm.init_app(app)

    @app.shell_context_processor
    def load_context_processor():
        from app.models import Post
        return {
            'app': app,
            'db': db,
            'Post': Post
        }
