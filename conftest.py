import pytest
from playwright.sync_api import sync_playwright
from pages.registerPage import RegisterPage
from pages.loginPage import LoginPage
from pages.forgotLoginInfo import forgotLoginInfo
from pages.accountsOverviewPage import AccountsOverviewPage

@pytest.fixture()
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=5000)
        page = browser.new_page()
        yield page
        browser.close()

@pytest.fixture()
def reg_Page(page):
    reg_Page = RegisterPage(page)
    return reg_Page

@pytest.fixture()
def login_page(page):
    login_page = LoginPage(page)
    return login_page

@pytest.fixture()
def forgetInfo_page(page):
    forgetInfo_page = forgotLoginInfo(page)
    return forgetInfo_page

@pytest.fixture()
def accountsOverview_page(page):
    accountsOverview_page = AccountsOverviewPage(page)
    return accountsOverview_page