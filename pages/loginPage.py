#import pytest
from playwright.sync_api import expect, Page
import allure
from allureWraper import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        self.page = page
        self.registerLink_on_LoginPage = page.locator("//a[contains(text(), 'Register')]")
        self.forgotInfoLink_on_LoginPage = page.locator("//a[contains(text(), 'Forgot login info?')]")
        self.aboutUsLink_on_LoginPage = page.locator("//ul[@class='leftmenu']/li/a[contains(text(), 'About Us')]")
        self.servicesLink_on_LoginPage = page.locator("//ul[@class='leftmenu']/li/a[contains(text(), 'Services')]")
        self.productsLink_on_LoginPage = page.locator("//ul[@class='leftmenu']/li/a[contains(text(), 'Products')]")
        self.locationsLink_on_LoginPage = page.locator("//ul[@class='leftmenu']/li/a[contains(text(), 'Locations')]")
        self.adminPageLink_on_LoginPage = page.locator("//ul[@class='leftmenu']/li/a[contains(text(), 'Admin Page')]")
        self.latestNewsSection_ReadMoreLink_on_LoginPage = page.locator("//ul[@class='events']/following-sibling::p/a[contains(text(), 'Read More')]")
        self.paraBankLogo_HomePageLink_on_LoginPage = page.locator("//a[@href='index.htm']/img[@title= 'ParaBank']")
        self.homePageIcon_on_LoginPage = page.locator("//a[contains(text(), 'home')]")
        self.demoWebsiteAboutIcon_on_LoginPage = page.locator("//a[contains(text(), 'about')]")
        self.customerCareIcon_on_LoginPage = page.locator("//a[contains(text(), 'contact')]")
        self.usernameValue = page.locator("input[name='username']")
        self.passwordValue = page.locator("input[name='password']")
        self.logInBtn = page.locator("input[value='Log In']")


    #@allure.step("website launch step")
    def launchTheParaBankBrowser(self):
        print("inside launchTheParaBankBrowser fucntion on loginPage")
        self.page.goto("https://parabank.parasoft.com/parabank/index.htm")
        self.page.wait_for_timeout(1000)
        print("browser launched")

   # @allure.step("register link in login section step")
    def clickOnRegisterLink(self):
       # print("inside clickOnRegisterLink function on loginPage ")
        self.registerLink_on_LoginPage.click()
        print("register link in login section clicked")
        

    def forgotInfoLoginLink(self):
      #  print("inside forgotInfoLoginLink function on loginPage ")
        self.forgotInfoLink_on_LoginPage.click()
        print("forgotInfoLoginLink on login section clicked")
        

    def aboutUsLink(self):
       # print("inside aboutUsLink function on loginPage ")
        self.aboutUsLink_on_LoginPage.click()
        print("aboutUsLink in login section clicked")
                
    def servicesLink(self):
       # print("inside servicesLink function on loginPage ")
        self.servicesLink_on_LoginPage.click()
        print("servicesLink  in login section clicked")

        
    def productsLink(self):
       # print("inside productsLink function on loginPage ")
        self.productsLink_on_LoginPage.click()
        print("productsLink in login section clicked")
        self.goBackBtn_OnBrowser()

        
    def locationsLink(self):
      #  print("inside locationsLink function on loginPage ")
        self.locationsLink_on_LoginPage.click()
        print("locationsLink  in login section clicked")
        self.goBackBtn_OnBrowser()

        
    def adminPageLink(self):
      #  print("inside adminPageLink function on loginPage ")
        self.adminPageLink_on_LoginPage.click()
        print("register link in login section clicked")

        
    def latestNewsSection_ReadMoreLink(self):
      #  print("inside latestNewsSectionReadMoreLink function on loginPage ")
        self.latestNewsSection_ReadMoreLink_on_LoginPage.click()
        print("latestNewsSectionReadMoreLink in login section clicked")

        
    def paraBankLogo_HomePageLink(self):
      #  print("inside paraBankLogoHomePageLink function on loginPage ")
        self.paraBankLogo_HomePageLink_on_LoginPage.click()
        print("paraBankLogoHomePageLink in login section clicked")
        self.page.screenshot(path="screenshots/page_launched.png", full_page=True)

         
    def homePageIcon(self):
      #  print("inside homePageIcon function on loginPage ")
        self.homePageIcon_on_LoginPage.click()
        print("homePageIcon in login section clicked")

    
        
    def demoWebsiteAboutIcon(self):
      #  print("inside demoWebsiteAboutIcon function on loginPage ")
        self.demoWebsiteAboutIcon_on_LoginPage.click()
        print("demoWebsiteAboutIcon in login section clicked")

            
    def customerCareIcon(self):
      #  print("inside customerCareIcon function on loginPage ")
        self.customerCareIcon_on_LoginPage.click()
        print("customerCareIcon in login section clicked")

    
    def goBackBtn_OnBrowser(self):
        print("navigating back using browser back button")
        self.page.go_back()

    def clickOnLogInBtn(self, usernameVarValue, passwordVarValue):
        print("inside loginin function")
        self.usernameValue.fill(usernameVarValue)
        self.passwordValue.fill(passwordVarValue)
        print("username is", usernameVarValue)
        print("password is ", passwordVarValue)
        self.logInBtn.click()
        print("login clicked")
        

