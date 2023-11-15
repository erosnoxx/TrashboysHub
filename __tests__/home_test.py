from ward import test
from __tests__.fixtures import browser
from faker import Faker
from flask import url_for
from __tests__.factories.post_factory import PostFactory


@test('Main page must be online')
def _(browser=browser):

    browser.visit(url_for('home.index'))

    assert browser.is_text_present('Posts')


@test('Current user access main page and sees a post')
def _(browser=browser):
    post = PostFactory.create()

    browser.visit(url_for('home.index'))

    assert browser.is_text_present(post.title)


@test('Current user accesses main page and doesnt see a post')
def _(browser=browser):

    browser.visit(url_for('home.index'))

    assert browser.is_text_present('Nothing to do here')


@test('Current user accesses main page and doesnt see unpublished posts')
def _(browser=browser):
    post = PostFactory.create(title='Vacations!')
    drafts = PostFactory.create_batch(2, published=False)

    browser.visit(url_for('home.index'))

    assert browser.is_text_present(post.title)
    assert browser.is_text_not_present(drafts[0].title)
    assert browser.is_text_not_present(drafts[1].title)


@test('Current user sees a unitary post')
def _(browser=browser):
    post = PostFactory.create()

    browser.visit(url_for('home.index'))
    browser.links.find_by_text(post.title).click()

    assert browser.is_text_present(post.title)
    assert browser.is_text_present(post.text)