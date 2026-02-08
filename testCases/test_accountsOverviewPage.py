from playwright.sync_api import Page, expect
from pages.loginPage import *
from pages.registerPage import *
from pages.accountsOverviewPage import *
from conftest import *
from utils.readingJson import readJsonData

from openpyxl import load_workbook
from utils.handlingExcel import *

def test_accountsOverviewPageValues(page, accountsOverview_page, login_page):
    print(" inside test_accountsOverviewPageValues function ")

    #launch the browser
    login_page.launchTheParaBankBrowser()
    #login with valid creds
    credentials = "testData\\QA_Credentials.json"
    testData = readJsonData(credentials)
    login_page.clickOnLogInBtn(testData["username"], testData["password"])

    #click on account overview link in left menu
    accountsOverview_page.accountsOverviewDataCheck()

    #click on account number to get more details
    accountsOverview_page.clickAccountNumber()

    # use the data from excel to retrieve the month and type as requested by user
    filepath = "testData\\ParaBank_Test_details.xlsx"
    sheetname = "AccActivity"

    excelData = read_excel_by_rows(filepath, sheetname)

    for data in excelData:
        print("checking for month", data[0])
        print("checking for type", data[1])

        #select the month and type and click on go button
        accountsOverview_page.checkAccountActivity(data[0],data[1])
        print("done")
        accountsOverview_page.checkTransactionDetails()




# def test_multipleUserRegistrations_using_excelData(page, reg_Page, login_page):
#     filepath = "testData\\ParaBank_Test_details.xlsx"
#     sheetname = "Sheet1"

#     excelData = read_excel_by_rows(filepath, sheetname)

#     for data in excelData:
#         print("Registering user:", data[0])

#         login_page.launchTheParaBankBrowser()
#         login_page.clickOnRegisterLink()

#         reg_Page.enterFirstName(data[1])
#         reg_Page.enterLastName(data[2])
#         reg_Page.enterStreetAddress(data[3])
#         reg_Page.enterCity(data[4])
#         reg_Page.enterState(data[5])
#         reg_Page.enterZipcode(data[6])
#         reg_Page.enterPhoneNumber(data[7])
#         reg_Page.enterSSN(data[8])
#         reg_Page.enterUserName(data[9])
#         reg_Page.enterPassword(data[10])
#         reg_Page.enterRepeatedPassword(data[11])

#         reg_Page.clickRegisterBtn()
#         reg_Page.clickLogOutBtn()


