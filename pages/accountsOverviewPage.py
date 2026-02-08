from playwright.sync_api import expect, Page

class AccountsOverviewPage():
    def __init__(self, page: Page):
        self.page = page
        #accounts overview section
        self.pageHeaderlabel = page.locator("//div[@id='showOverview']/h1[@class='title']")
        # self.accountNumberLinkInTable = page.locator("//a[contains(text(), '14121')]")
        # self.balanceValueInTable = page.locator("//a[contains(text(), '14121')]/parent::td/following-sibling::td[1]")
        # self.availableBalValueInTable = page.locator("//a[contains(text(), '14121')]/parent::td/following-sibling::td[2]")
        self.totalAmountLabel = page.locator("//table[@id='accountTable']/tbody/tr[2]/td[2]")
        self.accountNumberLinkInTable = page.locator("//a[matches(text(), '^[0-9]+$')]")    
        self.balanceValueInTable = page.locator("//a[matches(text(), '^[0-9]+$')]/parent::td/following-sibling::td[1]")
        self.availableBalValueInTable = page.locator("//a[matches(text(), '^[0-9]+$')]/parent::td/following-sibling::td[2]")

        # account details section
        self.accountDetailsHeaderLabel = page.locator("//h1[contains(text(),'Account Details')]")
        # account activity section
        self.activityPeriodMonth = page.locator("select#month")
        self.activityType = page.locator("select#transactionType")
        self.activityGoBtn = page.locator("input[type='submit'], button:has-text('GO')")

        # transaction details link
        self.transactionTypeInTableClick= page.locator("//a[contains(text(),'Funds ')]")

        # self.activityDateInTable =
        # self.activityTransactionInTable =
        # self.activityDebitInTable =
        # self.activityCreditInTable =

        # transaction details section
        self.transactionId = page.locator("//td[normalize-space()='Transaction ID:']/following-sibling::td")
        self.transactionDate = page.locator("//td[normalize-space()='Date:']/following-sibling::td")
        self.transactionDesc =page.locator("//td[normalize-space()='Description:']/following-sibling::td")
        self.transactionType = page.locator("//td[normalize-space()='Type:']/following-sibling::td")
        self.transactionAmt =page.locator("//td[normalize-space()='Amount:']/following-sibling::td")




    def accountsOverviewDataCheck(self):
        print("self.pageHeaderlabel", self.pageHeaderlabel.text_content())
        print("accountNumberLinkInTable",self.accountNumberLinkInTable.text_content())
        print("balanceValueInTable", self.balanceValueInTable.text_content())
        print("availableBalValueInTable", self.accountNumberLinkInTable.text_content())
        print("totalAmountLabel", self.totalAmountLabel.text_content())
    
    def clickAccountNumber(self):
        self.accountNumberLinkInTable.click()
       # print("clicked on account number", self.accountNumberLinkInTable.text_content())
        print("page header is now ",self.accountDetailsHeaderLabel.text_content() )
        #self.page.screenshot(path="screenshots/account_details.png", full_page=True)
           

    def checkAccountActivity(self, activityMonthValue, activityTypeValue ):
        self.activityPeriodMonth.select_option(label=activityMonthValue)
        self.activityType.select_option(label=activityTypeValue)
        
        print("checking account activity for month", activityMonthValue)
        print("type",activityTypeValue)

        self.activityGoBtn.click()


    def checkTransactionDetails(self):
        print("inside checkTransactionDetails")
        self.transactionTypeInTableClick.click()
        print("transaction id ", self.transactionId.text_content())
        print("transaction date ",self.transactionDate.text_content())
        print("transaction desc ",self.transactionDesc.text_content())
        print("transaction type ",self.transactionType.text_content())
        print("transaction amount ",self.transactionAmt.text_content())
        self.page.screenshot(path="screenshots/transaction_details.png", full_page=True)