from ward import test
from __tests__.fixtures import browser
from flask import url_for
from app.models import Category


@test('Current user registers a category', tags=['categories'])
def _(browser=browser):

    browser.visit(url_for('home.index'))
    browser.links.find_by_text('Register category').click()
    browser.fill('name', 'Europe')
    browser.find_by_value('Save').click()

    assert browser.url == url_for('home.index')
    assert Category.query.count() == 1
    assert Category.query.first().name == 'Europe'
