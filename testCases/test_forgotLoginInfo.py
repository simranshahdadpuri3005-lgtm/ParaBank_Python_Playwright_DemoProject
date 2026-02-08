from playwright.sync_api import Page, expect
import pytest
from pages.loginPage import *
from pages.registerPage import *
from pages.forgotLoginInfo import *
from conftest import *

# def test_newRegistration(page, reg_Page,login_page ):
#     print("new registration test case")
#     login_page.launchTheParaBankBrowser()
#     login_page.clickOnRegisterLink()

#     reg_Page.enterFirstName("first name")
#     reg_Page.enterLastName("last name")
#     reg_Page.enterStreetAddress("street")
#     reg_Page.enterCity("city")
#     reg_Page.enterState("state")
#     reg_Page.enterZipcode("zipcode")
#     reg_Page.enterPhoneNumber("123456789")
#     reg_Page.enterSSN("765-987-876")
#     reg_Page.enterUserName("test_user2")
#     reg_Page.enterPassword("testpassword1")
#     reg_Page.enterRepeatedPassword("testpassword1")

#     reg_Page.clickRegisterBtn()

#     login_page.paraBankLogo_HomePageLink()

def test_forgotLoginInfo(page, login_page, reg_Page, forgetInfo_page):
    print("new registration test case")
    login_page.launchTheParaBankBrowser()
    login_page.clickOnRegisterLink()

    reg_Page.enterFirstName("first")
    reg_Page.enterLastName("last")
    reg_Page.enterStreetAddress("street")
    reg_Page.enterCity("city")
    reg_Page.enterState("state")
    reg_Page.enterZipcode("zipcode")
    reg_Page.enterPhoneNumber("123456789")
    reg_Page.enterSSN("765-987-876")
    reg_Page.enterUserName("test_user9")
    reg_Page.enterPassword("testpassword1")
    reg_Page.enterRepeatedPassword("testpassword1")

    reg_Page.clickRegisterBtn()

    reg_Page.clickLogOutBtn()

    print("forgotLoginInfo test case")
   # login_page.launchTheParaBankBrowser()
    login_page.forgotInfoLoginLink()
    print("1")
    forgetInfo_page.enterFirstName("first")
    forgetInfo_page.enterLastName("last")
    forgetInfo_page.enterStreetAddress("street")
    forgetInfo_page.enterCity("city")
    forgetInfo_page.enterState("state")
    forgetInfo_page.enterZipcode("zipcode")
    forgetInfo_page.enterSSN("765-987-876")
    forgetInfo_page.findMyLoginInfoFunction()





