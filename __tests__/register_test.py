from ward import test
from __tests__.fixtures import browser
from flask import url_for
from faker import Faker


@test('Current user registration', tags=['register'])
def _(browser=browser):
    
    browser.visit(url_for('login.login_'))
    browser.find_by_text('Sign up').click()
    browser.fill('fullname', Faker().name())
    browser.fill('username', Faker().user_name())
    browser.fill('email', Faker().email())
    browser.fill('password', Faker().password())
    browser.select('gender', 'Male')
    browser.fill('birth', Faker().date_of_birth(minimum_age=18, maximum_age=90))
    browser.find_by_value('submit').click()

    assert browser.url == url_for('login.login_')
