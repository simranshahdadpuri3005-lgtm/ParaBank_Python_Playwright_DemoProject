from playwright.sync_api import expect, Page

class forgotLoginInfo():

    def __init__(self, page: Page):
        self.page = page

        self.firstName = page.locator("#firstName")
        self.lastName = page.locator("#lastName")
        self.streetAddress = page.locator("#address\\.street")
        self.city = page.locator("#address\\.city")
        self.state = page.locator("#address\\.state")
        self.zipcode = page.locator("#address\\.zipCode")
        self.SSN = page.locator("#ssn")
        self.findMyLoginInfoBtn = page.locator("input[value='Find My Login Info']")
        self.success_info_message = page.locator("//p[contains(text(), 'You are now logged in')]")


    def enterFirstName(self, fnameValue):
        self.firstName.fill(fnameValue)
        print("forgotInfoLoginLink fname is", fnameValue)

    def enterLastName(self, lnameValue):
        self.lastName.fill(lnameValue)
        print("lname is", lnameValue)

    def enterStreetAddress(self, streetAddressValue):
        self.streetAddress.fill(streetAddressValue)
        print("streetAddressValue is", streetAddressValue)

    def enterCity(self, cityValue):
        self.city.fill(cityValue)
        print("cityValue is", cityValue)

    def enterState(self, stateValue):
        self.state.fill(stateValue)
        print("state is", stateValue)

    def enterZipcode(self, zipcodeValue):
        self.zipcode.fill(zipcodeValue)
        print("zipcodeValue is", zipcodeValue)

    def enterSSN(self, SSNValue):
        self.SSN.fill(SSNValue)
        print("SSNValue is", SSNValue)

    def findMyLoginInfoFunction(self):
        self.findMyLoginInfoBtn.click()
        print("findMyLoginInfo Button Clicked")
        #expect(self.success_info_message).to_have_text("Your login information was located successfully. You are now logged in.")

        
        