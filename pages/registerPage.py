from playwright.sync_api import expect, Page

class RegisterPage():
    def __init__(self, page: Page):
        self.page = page

        self.firstName = page.locator("#customer\\.firstName")
        self.lastName = page.locator("#customer\\.lastName")
        self.streetAddress = page.locator("#customer\\.address\\.street")
        self.city = page.locator("#customer\\.address\\.city")
        self.state = page.locator("#customer\\.address\\.state")
        self.zipcode = page.locator("#customer\\.address\\.zipCode")
        self.phoneNumber = page.locator("#customer\\.phoneNumber")
        self.SSN = page.locator("#customer\\.ssn")
        self.userName = page.locator("#customer\\.username")
        self.password = page.locator("#customer\\.password")
        self.repeatedPassword = page.locator("#repeatedPassword")
        self.registerBtn = page.locator("input[value='Register']")
        self.successfulRegistrationMsgLabel = page.get_by_text("Your account was created successfully. You are now logged in.")
        self.logOutBtn = page.locator("//li/a[contains(text(), 'Log Out')]")

    def enterFirstName(self, fnameValue):
        self.firstName.fill(fnameValue)
        print("fname is", fnameValue)

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

    def enterPhoneNumber(self, phoneNumberValue):
        self.phoneNumber.fill(phoneNumberValue)
        print("phoneNumberValue is", phoneNumberValue)

    def enterSSN(self, SSNValue):
        self.SSN.fill(SSNValue)
        print("SSNValue is", SSNValue)

    def enterUserName(self, userNameValue):
        self.userName.fill(userNameValue)
        print("userNameValue is", userNameValue)

    def enterPassword(self, passwordValue):
        self.password.fill(passwordValue)
        print("passwordValue is", passwordValue)
    
    def enterRepeatedPassword(self, repeatedPasswordValue):
        self.repeatedPassword.fill(repeatedPasswordValue)
        print("repeated password value is ", repeatedPasswordValue)

    def clickRegisterBtn(self):
        self.registerBtn.click()
        print("register Button Clicked")
        expect(self.successfulRegistrationMsgLabel).to_be_visible()
        expect(self.successfulRegistrationMsgLabel).to_have_text("Your account was created successfully. You are now logged in.")

    def clickLogOutBtn(self):
        self.logOutBtn.click()
        print("logout clicked")
