from ward import fixture
from splinter import Browser
from app import create_app, db
from dotenv import load_dotenv

load_dotenv('.env.test')

@fixture
def browser():
    app = create_app()
    app.testing = True
    context = app.test_request_context()
    context.push()

    with app.test_client():
        db.create_all()

        yield Browser('flask', app=app)

        db.drop_all()
        db.session.remove()