from playwright.sync_api import Page, expect
import pytest
from pages.loginPage import *
from pages.registerPage import *
from pages.loginPage import *
from pages.accountsOverviewPage import AccountsOverviewPage

from conftest import *
from utils.readingJson import readJsonData

def test_validLogin(page, reg_Page,login_page, accountsOverview_page):
    print("inside valid login function in test file")
    login_page.launchTheParaBankBrowser()
  
    credentials = "testData\\QA_Credentials.json"
    testData = readJsonData(credentials)
    print("username is", testData["username"])
    print("password is ", testData["password"])
    login_page.clickOnLogInBtn(testData["username"], testData["password"])
    
    page.screenshot(path="screenshots/account_details1.png", full_page=True)
    
    #accountsOverview_page.accountsOverviewDataCheck()


