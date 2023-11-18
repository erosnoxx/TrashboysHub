from ward import test
from __tests__.fixtures import browser
from flask import url_for
from .factories.login_factory import LoginFactory
from .factories.permission_factory import PermissionFactory

@test('Current user logs into the site', tags=['login'])
def _(browser=browser):
    permissions = [PermissionFactory.create(level='admin'),
                   PermissionFactory.create(level='user')]
    login = LoginFactory.create(permissions=permissions)

    browser.visit(url_for('login.login_'))
    browser.fill('username', login.username)
    browser.fill('password', login.password)
    browser.find_by_value('Login').click()

    assert browser.url == url_for('home.index')
