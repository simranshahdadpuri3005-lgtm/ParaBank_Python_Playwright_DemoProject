from playwright.sync_api import Page, expect
import pytest
from pages.loginPage import *
from pages.registerPage import *
from conftest import *
from openpyxl import load_workbook
from utils.handlingExcel import *



# def test_newRegistration(page, reg_Page,login_page ):
#     print("new registration test case")
#     login_page.launchTheParaBankBrowser()
#     login_page.clickOnRegisterLink()

#     reg_Page.enterFirstName("first name")
#     reg_Page.enterLastName("last name")
#     reg_Page.enterStreetAddress("street")
#     reg_Page.enterCity("city")
#     reg_Page.enterState("state")
#     reg_Page.enterZipcode("l5m 6e6")
#     reg_Page.enterPhoneNumber("123456789")
#     reg_Page.enterSSN("765-987-876")
#     reg_Page.enterUserName("test_user3")
#     reg_Page.enterPassword("testpassword1")
#     reg_Page.enterRepeatedPassword("testpassword1")

#     reg_Page.clickRegisterBtn()

# def test_printExcelValues_ByRows():
#     print("inside test_printExcelValues_ByRows function in tst new registation file")
#     filepath ="testData\ParaBank_Test_details.xlsx"
#     sheetname ="Sheet1"
#     excelData = read_excel_by_rows(filepath, sheetname)
#     print("exceldata is ", excelData)

def test_multipleUserRegistrations_using_excelData(page, reg_Page, login_page):
    filepath = "testData\\ParaBank_Test_details.xlsx"
    sheetname = "Sheet1"

    excelData = read_excel_by_rows(filepath, sheetname)

    for data in excelData:
        print("Registering user:", data[0])

        login_page.launchTheParaBankBrowser()
        login_page.clickOnRegisterLink()

        reg_Page.enterFirstName(data[1])
        reg_Page.enterLastName(data[2])
        reg_Page.enterStreetAddress(data[3])
        reg_Page.enterCity(data[4])
        reg_Page.enterState(data[5])
        reg_Page.enterZipcode(data[6])
        reg_Page.enterPhoneNumber(data[7])
        reg_Page.enterSSN(data[8])
        reg_Page.enterUserName(data[9])
        reg_Page.enterPassword(data[10])
        reg_Page.enterRepeatedPassword(data[11])

        reg_Page.clickRegisterBtn()
        reg_Page.clickLogOutBtn()
