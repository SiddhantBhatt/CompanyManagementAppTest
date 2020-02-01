"""
All the Person page related methods will be present in this class
"""

import utilities.custom_logger as cl
from pages.home.navigation_page import NavigationPage
import logging
from base.basepage import BasePage
import time


class PersonPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _company_dropdown = "company"
    _search_company_field = "//input[@placeholder='Search Company..']"
    _company_name = "//li[contains(text(),'{0}')]"
    _addButton = "add"
    _addPerson_title = "//select[@name='title']"
    _addPerson_surname_field = "//input[@name='surname']"
    _addPerson_firstname_field = "//input[@name='givenName']"
    _addPerson_postalName = "//input[@name='postalName']"
    _addPerson_nickname = "//input[@name='nickname']"
    _addPerson_nationality = "nationality"
    _addPerson_nationality_select = "//div[text()='Indian']"
    _addPerson_qualification = "//input[@name='qualification']"
    _addPerson_honours = "//input[@name='honours']"
    _addPerson_mainWorkplace_dropdown = "//span[contains(text(),'Choose Main Workplace')]"
    _addPerson_mainWorkplace_searchField = "//input[@placeholder='Search..']"
    _addPerson_mainWorkplace_data = "//li[contains(text(),'{}')]"
    _notes_textbox = "//textarea[@name='notes']"
    _save_button = "//button[contains(text(),'Save')]"
    _person_name_in_list = "//a[contains(text(),'{0}, {1}')]"
    _listButton = "list"
    _personList = "table"
    _auditButton = "audit"
    _auditTable = "auditTable"
    _closeModal = "//div[@class='modal-dialog modal-lg']//button[contains(text(),'×')]"
    _editButton = "edit"
    _profileButton = "//a[@data-id='PROFILE']"
    _profile_editBtn = "edit-tab"
    _profile_idcard = "//input[@name='idCard']"
    _profile_passport = "//input[@name='passport']"
    _profile_dob = "dob"
    _profile_anniversary = "//input[@name='anniversary']"
    _profile_details_idcard = "idCard"
    _profile_details_passport = "passport"
    _profile_syncButton = "refresh-tab"
    _personalCommsButton = "//a[@data-id='PERSONAL_COMMS']"
    _addTabButton = "add-tab"
    _personalComms_commsType_dropdown = "//span[contains(text(),'Choose Comms Type')]"
    _personalComms_commsType_searchField = "//input[@placeholder='Search..']"
    _personalComms_commsType_data = "//li[contains(text(),'{}')]"
    _personalComms_numEmailUrlField = "//input[@title='Number/Email/URL']"
    _personalComms_countryCode = "//input[@name='countryCode']"
    _personalComms_areaCode = "//input[@name='areaCode']"
    _personalComms_mainToggle = "//label[@class='switch']//span"
    _personalComms_details_commsType = "//table[@id='tab-table']//td[contains(text(),'{}')]"
    _personalComms_details_commsData = "//table[@id='tab-table']//td[contains(text(),'{}')]"
    _personalComms_deleteButton = "//td[contains(text(),'{}')]/following-sibling::td[4]/a"
    _confirmDeleteButton = "//div[@id='deleteModal']//button[contains(text(),'Delete')]"
    _deleteButton = "delete"
    _invalidMessage = "//li[contains(text(),'invalid')]"



    def selectCompany(self, company):
        self.nav.navigateToPrime()
        self.nav.navigateToPerson()
        element = self.waitForElement(locator=self._company_dropdown, timeout=5, pollFrequency=0.5)
        self.elementClick(element=element)
        self.sendKeys(data=company, locator=self._search_company_field, locatorType="xpath")
        self.elementClick(locator=self._company_name.format(company), locatorType="xpath")

    def enterSavePersonDetails(self, firstName, lastName, postalName, nickname, nationality, qualification,
                               honours, notes):
        time.sleep(2)
        # self.selectByValue(item=title, locator=self._addPerson_title, locatorType="xpath")
        self.clearField(locator=self._addPerson_surname_field, locatorType="xpath")
        self.sendKeys(lastName, locator=self._addPerson_surname_field, locatorType="xpath")
        self.clearField(locator=self._addPerson_firstname_field, locatorType="xpath")
        self.sendKeys(firstName, locator=self._addPerson_firstname_field, locatorType="xpath")
        self.clearField(locator=self._addPerson_postalName, locatorType="xpath")
        self.sendKeys(postalName, locator=self._addPerson_postalName, locatorType="xpath")
        self.clearField(locator=self._addPerson_nickname, locatorType="xpath")
        self.sendKeys(nickname, locator=self._addPerson_nickname, locatorType="xpath")
        self.clearField(locator=self._addPerson_nationality)
        self.sendKeys(nationality, locator=self._addPerson_nationality)
        self.waitForElement(locator=self._addPerson_nationality_select, locatorType="xpath")
        self.elementClick(locator=self._addPerson_nationality_select, locatorType="xpath")
        self.clearField(locator=self._addPerson_qualification, locatorType="xpath")
        self.sendKeys(qualification, locator=self._addPerson_qualification, locatorType="xpath")
        self.clearField(locator=self._addPerson_honours, locatorType="xpath")
        self.sendKeys(honours, locator=self._addPerson_honours, locatorType="xpath")
        # self.elementClick(locator=self._addPerson_mainWorkplace_dropdown, locatorType="xpath")
        # self.sendKeys(data=workplace, locator=self._addPerson_mainWorkplace_searchField, locatorType="xpath")
        # time.sleep(2)
        # self.elementClick(locator=self._addPerson_mainWorkplace_data.format(workplace), locatorType="xpath")
        self.clearField(locator=self._notes_textbox, locatorType="xpath")
        self.sendKeys(notes, locator=self._notes_textbox, locatorType="xpath")
        time.sleep(2)
        self.elementClick(locator=self._save_button, locatorType="xpath")
        time.sleep(2)
        self.driver.get("https://logisticsmarts.net/app/person")

    def invalidAddPerson(self):
        self.selectCompany(company="Windows")
        addbtn = self.waitForElement(locator=self._addButton)
        self.elementClick(element=addbtn)
        time.sleep(2)
        self.elementClick(locator=self._save_button, locatorType="xpath")
        result = self.isElementPresent(locator=self._invalidMessage, locatorType="xpath")
        self.elementClick(locator=self._closeModal, locatorType="xpath")
        time.sleep(2)
        return result

    def addPerson(self, firstName, lastName, postalName, nickname, nationality, qualification,
                  honours, notes):
        # self.selectCompany(company="Windows")
        addbtn = self.waitForElement(locator=self._addButton)
        self.elementClick(element=addbtn)
        self.enterSavePersonDetails(firstName, lastName, postalName, nickname, nationality, qualification,
                                    honours, notes)
        time.sleep(2)

    def verifyPersonRecord(self, firstName, lastName):
        self.nav.navigateToPerson()
        result = self.isElementPresent(locator=self._person_name_in_list.format(lastName, firstName), locatorType="xpath")
        return result

    def openPersonRecord(self, lastName, firstName):
        self.waitForElement(locator=self._person_name_in_list.format(lastName, firstName), locatorType="xpath")
        self.elementClick(locator=self._person_name_in_list.format(lastName, firstName), locatorType="xpath")
        time.sleep(4)

    def clickOnList(self):
        self.elementClick(locator=self._listButton)

    def verifyPersonList(self):
        result = self.isElementPresent(locator=self._personList)
        time.sleep(2)
        return result

    def clickOnAudit(self):
        self.elementClick(locator=self._auditButton)
        time.sleep(2)

    def verifyAuditTable(self):
        self.waitForElement(locator=self._auditTable)
        result = self.isElementPresent(locator=self._auditTable)
        self.elementClick(locator=self._closeModal, locatorType="xpath")
        return result

    def clickOnEdit(self):
        self.elementClick(locator=self._editButton)

    def editProfile(self, idcard, passport, dob, anniversary):
        self.elementClick(locator=self._profileButton, locatorType="xpath")
        self.waitForElement(locator=self._profile_editBtn)
        self.elementClick(locator=self._profile_editBtn)
        self.waitForElement(locator=self._profile_idcard, locatorType="xpath")
        self.clearField(locator=self._profile_idcard, locatorType="xpath")
        self.sendKeys(idcard, locator=self._profile_idcard, locatorType="xpath")
        self.clearField(locator=self._profile_passport, locatorType="xpath")
        self.sendKeys(passport, locator=self._profile_passport, locatorType="xpath")
        time.sleep(2)
        self.clearField(locator=self._profile_dob)
        self.sendKeys(dob, locator=self._profile_dob)
        time.sleep(2)
        self.clearField(locator=self._profile_anniversary, locatorType="xpath")
        self.sendKeys(anniversary, locator=self._profile_anniversary, locatorType="xpath")
        time.sleep(2)
        self.elementClick(locator=self._save_button, locatorType="xpath")

    def verifyEditProfile(self, idcard, passport):
        time.sleep(2)
        self.waitForElement(locator=self._profile_syncButton)
        self.elementClick(locator=self._profile_syncButton)
        time.sleep(2)
        idcardText = self.getText(locator=self._profile_details_idcard)
        passportText = self.getText(locator=self._profile_details_passport)
        if idcardText == idcard and passportText == passport:
            result = True
        else:
            result = False
        return result

    def invalidAddPersonalComms(self):
        self.waitForElement(locator=self._personalCommsButton, locatorType="xpath")
        self.elementClick(locator=self._personalCommsButton, locatorType="xpath")
        self.waitForElement(locator=self._addTabButton)
        self.elementClick(locator=self._addTabButton)
        time.sleep(2)
        self.elementClick(locator=self._save_button, locatorType="xpath")
        result = self.isElementPresent(locator=self._invalidMessage, locatorType="xpath")
        self.elementClick(locator=self._closeModal, locatorType="xpath")
        return result

    def addPersonalComms(self, commsType, commsData, countryCode, areaCode, notes):
        self.waitForElement(locator=self._personalCommsButton, locatorType="xpath")
        self.elementClick(locator=self._personalCommsButton, locatorType="xpath")
        self.waitForElement(locator=self._addTabButton)
        self.elementClick(locator=self._addTabButton)
        time.sleep(2)
        self.waitForElement(locator=self._personalComms_commsType_dropdown, locatorType="xpath")
        self.elementClick(locator=self._personalComms_commsType_dropdown, locatorType="xpath")
        self.sendKeys(data=commsType, locator=self._personalComms_commsType_searchField, locatorType="xpath")
        self.elementClick(locator=self._personalComms_commsType_data.format(commsType), locatorType="xpath")
        self.sendKeys(data=countryCode, locator=self._personalComms_countryCode, locatorType="xpath")
        self.sendKeys(data=areaCode, locator=self._personalComms_areaCode, locatorType="xpath")
        self.sendKeys(data=commsData, locator=self._personalComms_numEmailUrlField, locatorType="xpath")
        self.elementClick(locator=self._personalComms_mainToggle, locatorType="xpath")
        self.sendKeys(notes, locator=self._notes_textbox, locatorType="xpath")
        time.sleep(2)
        self.elementClick(locator=self._save_button, locatorType="xpath")

    def verifyAddPersonalComms(self, commsType, commsData):
        self.waitForElement(locator=self._personalCommsButton, locatorType="xpath")
        self.elementClick(locator=self._personalCommsButton, locatorType="xpath")
        time.sleep(2)
        commsTypeText = self.getText(locator=self._personalComms_details_commsType.format(commsType), locatorType="xpath")
        commsDataText = self.getText(locator=self._personalComms_details_commsData.format(commsData), locatorType="xpath")
        if commsTypeText == commsType and commsDataText == commsData:
            result = True
        else:
            result = False
        return result

    def deletePersonalComms(self, commsData):
        self.waitForElement(locator=self._personalComms_deleteButton.format(commsData), locatorType="xpath")
        self.elementClick(locator=self._personalComms_deleteButton.format(commsData), locatorType="xpath")
        self.waitForElement(locator=self._confirmDeleteButton, locatorType="xpath")
        self.elementClick(locator=self._confirmDeleteButton, locatorType="xpath")
        time.sleep(2)

    def verifyDeletePersonalComms(self, commsData):
        result = self.isElementPresent(locator=self._personalComms_details_commsData.format(commsData), locatorType="xpath")
        if not result:
            return True
        else:
            return False

    def deletePerson(self, lastName, firstName):
        self.nav.navigateToPerson()
        self.openPersonRecord(lastName, firstName)
        self.waitForElement(locator=self._deleteButton)
        self.elementClick(locator=self._deleteButton)
        self.waitForElement(locator=self._confirmDeleteButton, locatorType="xpath")
        self.elementClick(locator=self._confirmDeleteButton, locatorType="xpath")
        self.nav.navigateToPerson()
        time.sleep(2)




















