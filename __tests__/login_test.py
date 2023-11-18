from ward import test
from __tests__.fixtures import browser
from flask import url_for
from __tests__.factories.login_factory import LoginFactory


@test('Current user logs into the site', tags=['login'])
def _(browser=browser):
    login = LoginFactory.create()

    browser.visit(url_for('login.login_'))
    browser.fill('username', login.username)
    browser.fill('password', login.password)
    browser.find_by_value('Login').click()

    assert browser.url == url_for('home.index')
