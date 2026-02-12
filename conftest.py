import pytest
from playwright.sync_api import sync_playwright
from pages.registerPage import RegisterPage
from pages.loginPage import LoginPage
from pages.forgotLoginInfo import forgotLoginInfo
from pages.accountsOverviewPage import AccountsOverviewPage
import allure

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




@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Capture screenshots for setup, call, and teardown failures
    if report.failed:
        page = item.funcargs.get("page", None)
        if page:
            step = report.when  # setup / call / teardown
            screenshot = page.screenshot()
            allure.attach(
                screenshot,
                name=f"Failure Screenshot ({step})",
                attachment_type=allure.attachment_type.PNG
            )


# allure generate ./allure-results --clean -o ./allure-report

# we need to share the whole allire report folder with the team member and to view the result, use the next command
# allure open ./allure-report

# we can use this command to generate and open the allure report after test execution is completed
# allure open ./allure-report
