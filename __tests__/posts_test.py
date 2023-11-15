from ward import test
from __tests__.fixtures import browser
from __tests__.factories.category_factory import CategoryFactory
from flask import url_for
from app.models import Post, Category


@test('Current user registers a post', tags=['posts'])
def _(browser=browser):
    category = CategoryFactory.create()

    browser.visit(url_for('home.index'))
    browser.links.find_by_text('Register post').click()
    browser.fill('title', 'Só de boa')
    browser.fill('text', 'Na paz de Deus')
    browser.select('categories', str(category.id))
    browser.check('published')
    browser.find_by_value('Save').click()

    assert browser.url == url_for('home.index')
    assert browser.is_text_present('Published Successfully')
    assert Post.query.first().title == 'Só de boa'
    assert Post.query.count() == 1
    assert Category.query.first() == Post.query.first().category
