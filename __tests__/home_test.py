from ward import test
from splinter import Browser
from app import create_app, db
from app.models import Post
from __tests__.fixtures import browser

@test('Main page must be online')
def _(browser=browser):

    browser.visit('/')

    assert browser.is_text_present('Hello')


@test('Current user acess the main page and sees a post')
def _(browser=browser):

    post = Post(title='Vacations!', published=True, 
        text='Somebody once told me the world is gonna roll me')
    db.session.add(post)
    db.session.commit()

    browser.visit('/')

    assert browser.is_text_present('Vacations!')