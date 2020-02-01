"""
All the Login page related methods will be present in this class
"""
from pages import page_package
# import utilities.custom_logger as cl
# from pages.home.navigation_page import NavigationPage
# import logging
# from base.basepage import BasePage


class LoginPage(page_package.BasePage):

    log = page_package.cl.customLogger(page_package.logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = page_package.NavigationPage(driver)

    # Locators
    _login_link = "Login"
    _email_field = "//input[@name='email']"
    _password_field = "//input[@name='password']"
    _login_button = "//button[contains(text(),'LOGIN')]"
    _settings_icon = "//header[@class='topnavbar-wrapper']//a[@data-title='SETTINGS']"

    def clickLoginLink(self):
        """
        Click on the Login link
        """
        self.elementClick(self._login_link, locatorType="link")

    def clearFields(self):
        """
        Clear email and password fields
        """
        self.clearField(self._email_field, locatorType="xpath")
        self.clearField(self._password_field, locatorType="xpath")

    def enterEmail(self, email):
        """
        Enter email in the email field
        """
        self.sendKeys(email, self._email_field, locatorType="xpath")

    def enterPassword(self, password):
        """
        Enter password in the password field
        """
        self.sendKeys(password, self._password_field, locatorType="xpath")

    def clickLoginButton(self):
        """
        Click on the login(form) button
        """
        self.elementClick(self._login_button, locatorType="xpath")

    def login(self, email="", password=""):
        """
        Combines methods to execute login flow
        """
        self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        """
        Verify if the login was successful
        """
        self.waitForElement(self._settings_icon, locatorType="xpath")
        result = self.isElementPresent(self._settings_icon, locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        """
        Verify if the login failed
        """
        self.waitForElement("//p[contains(text(),'Invalid Username or Password')]", locatorType="xpath")
        result = self.isElementPresent("//p[contains(text(),'Invalid Username or Password')]", locatorType="xpath")
        self.elementClick(locator="//button[@class='confirm']", locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        """
        Verify Page title
        """
        return self.verifyPageTitle("Welcome to Teams Office")

    def logout(self):
        """
        Method to log out
        """
        self.nav.navigateToUserDropdown()
        logoutLinkElement = self.waitForElement(locator="//a[@title='Logout']",
                                                locatorType="xpath", pollFrequency=1)
        # self.elementClick(element=logoutLinkElement)
        self.elementClick(locator="//a[@title='Logout']",
                          locatorType="xpath")
