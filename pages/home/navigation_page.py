"""
Class containing basic navigation methods in the home page
"""

import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _switch_user_icon = "//a[@data-title='SWITCH_USER']"
    _sync_icon = "//a[@data-title='SYNC']"
    _user_settings_icon = "//a[@data-title='SETTINGS']"
    _more_icon = "//a[@data-original-title='More']"
    _admin = "//span[@data-id='ADMIN']"
    _prime = "//span[@data-id='PRIME']"
    _doc = "//span[@data-id='DOCUMENT']"
    _action = "//span[@data-id='ACTION']"
    _accounting = "//span[@data-id='ACCOUNTING']"
    _timecosting = "//span[@data-id='TIME_COSTING']"
    _cosec = "//span[@data-id='COSEC']"
    _membership = "//span[@data-id='MEMBERSHIP']"
    _prime_person = "//span[@data-id='PERSON']"


    def navigateToSwitchUser(self):
        """
        Navigate/Click on All courses link/page
        """
        self.elementClick(locator=self._switch_user_icon, locatorType="link")

    def navigateToSync(self):
        """
        Navigate/Click on My Courses link/page
        """
        self.elementClick(locator=self._sync_icon, locatorType="link")

    def navigateToUserSettings(self):
        """
        Navigate/click to User settings section
        """
        userSettingsElement = self.waitForElement(locator=self._user_settings_icon, locatorType="xpath", pollFrequency=1)
        # self.elementClick(element=userSettingsElement)
        self.elementClick(locator=self._user_settings_icon, locatorType="xpath")

    def navigateToUserDropdown(self):
        """
        Navigate to User dropdown option
        """
        userDropdown = self.waitForElement(locator=self._more_icon, locatorType="xpath", pollFrequency=1)
        # self.elementClick(element=userDropdown)
        self.elementClick(locator=self._more_icon, locatorType="xpath")

    def naviateToAdmin(self):
        """
        Navigate to Admin dropdown
        """
        self.elementClick(locator=self._admin, locatorType="xpath")

    def navigateToPrime(self):
        """
        Navigate to Prime dropdown
        """
        element = self.waitForElement(locator=self._prime, locatorType="xpath", timeout=10, pollFrequency=1)
        self.elementClick(element=element)

    def navigateToDoc(self):
        """
        Navigate to Doc dropdown
        """
        self.elementClick(locator=self._doc, locatorType="xpath")

    def navigateToAction(self):
        """
        Navigate to Action dropdown
        """
        self.elementClick(locator=self._action, locatorType="xpath")

    def navigateToAccounting(self):
        """
        Navigate to Accounting dropdown
        """
        self.elementClick(locator=self._accounting, locatorType="xpath")

    def navigateToTimecosting(self):
        """
        Navigate to Time costing dropdown
        """
        self.elementClick(locator=self._timecosting, locatorType="xpath")

    def navigateToCosec(self):
        """
        Navigate to Cosec dropdown
        """
        self.elementClick(locator=self._cosec, locatorType="xpath")

    def navigateToMembership(self):
        """
        Navigate to Membership dropdown
        """
        self.elementClick(locator=self._membership, locatorType="xpath")

    def navigateToPerson(self):
        """
        Navigate to Person page
        """
        element = self.waitForElement(locator=self._prime_person, locatorType="xpath", timeout=10, pollFrequency=1)
        self.elementClick(element=element)
