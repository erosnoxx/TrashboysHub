from flask import Flask
import app.routes as routes


def create_app():
    app = Flask(__name__)

    routes.init_app(app)
    
    return app