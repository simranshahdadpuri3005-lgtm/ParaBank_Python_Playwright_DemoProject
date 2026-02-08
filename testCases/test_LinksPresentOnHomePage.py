from playwright.sync_api import Page, expect
import pytest
from pages.loginPage import *
from pages.registerPage import *
from conftest import *

def test_LinksPresentOnHomePage(page, reg_Page,login_page):
    print("testing various links on Home page")
    login_page.launchTheParaBankBrowser()
    login_page.clickOnRegisterLink()
    login_page.forgotInfoLoginLink()
    login_page.aboutUsLink()
    login_page.servicesLink()
    login_page.adminPageLink()
    login_page.homePageIcon()
    login_page.demoWebsiteAboutIcon()
    login_page.customerCareIcon()
    login_page.paraBankLogo_HomePageLink()
    login_page.latestNewsSection_ReadMoreLink()
    login_page.productsLink()
    login_page.locationsLink()



