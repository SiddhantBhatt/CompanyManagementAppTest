"""
Tests for Prime->Person Page
"""

from pages.prime.person_page import PersonPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class PersonTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        """
        Class object(s) setup
        """
        self.pp = PersonPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_addInvalidPerson(self):
        """
        Tests for verifying error in add person form
        Uses TestStatus class to mark/assert test case results
        """
        self.log.info("*#" * 20)
        self.log.info("test_addInvalidPerson started")
        self.log.info("*#" * 20)
        result = self.pp.invalidAddPerson()
        self.ts.markFinal(testName="test_addInvalidPerson", result=result, resultMessage="Verify Invalid Add Person")

    @pytest.mark.run(order=2)
    def test_addPerson(self):
        """
        Tests for adding a person record and verifies its presence in the person list
        Uses TestStatus class to mark/assert test case results
        """
        self.log.info("*#" * 20)
        self.log.info("test_addPerson started")
        self.log.info("*#" * 20)
        self.pp.addPerson(firstName="Test", lastName="Test", postalName="Test", nickname="Test",
                          nationality="Indian", qualification="Test", honours="Test", notes="Test")
        result = self.pp.verifyPersonRecord(firstName="Test", lastName="Test")
        self.ts.markFinal(testName="test_addPerson", result=result, resultMessage="Verify Add Person")

    @pytest.mark.run(order=3)
    def test_listButton(self):
        """
        Test for List Button working
        Person "Test, Test" should exist
        """
        self.log.info("*#" * 20)
        self.log.info("test_listButton started")
        self.log.info("*#" * 20)
        # self.driver.get("https://logisticsmarts.net/")
        # self.pp.selectCompany("Windows")
        self.pp.openPersonRecord(lastName="Test", firstName="Test")
        self.pp.clickOnList()
        result = self.pp.verifyPersonList()
        self.ts.markFinal(testName="test_listButton", result=result, resultMessage="Verify List Button")

    @pytest.mark.run(order=4)
    def test_auditButton(self):
        """
        Test for Audit Button working
        Person "Test, Test" should exist
        """
        self.log.info("*#" * 20)
        self.log.info("test_auditButton started")
        self.log.info("*#" * 20)
        # self.driver.get("https://logisticsmarts.net/")
        # self.pp.selectCompany(company="Windows")
        self.pp.openPersonRecord(lastName="Test", firstName="Test")
        self.pp.clickOnAudit()
        result = self.pp.verifyAuditTable()
        self.ts.markFinal(testName="test_auditButton", result=result, resultMessage="Verify Audit Button")

    @pytest.mark.run(order=5)
    def test_editPerson(self):
        """
        Test for edit person working
        Person "New, New" should exist
        """
        self.log.info("*#" * 20)
        self.log.info("test_editPerson started")
        self.log.info("*#" * 20)
        # self.driver.get("https://logisticsmarts.net/")
        # self.pp.selectCompany(company="Windows")
        # self.pp.openPersonRecord(lastName="New", firstName="New")
        self.pp.clickOnEdit()
        self.pp.enterSavePersonDetails(firstName="Test1", lastName="Test1", postalName="Test1", nickname="Test1",
                                       nationality="Indian", qualification="Test1", honours="Test1", notes="Test1")
        result = self.pp.verifyPersonRecord(firstName="Test1", lastName="Test1")
        self.ts.markFinal(testName="test_editPerson", result=result, resultMessage="Verify Edit Person")

    @pytest.mark.run(order=6)
    def test_editProfile(self):
        """
        Test for edit profile working
        Person "New, New" should exist
        """
        self.log.info("*#" * 20)
        self.log.info("test_editProfile started")
        self.log.info("*#" * 20)
        # self.driver.get("https://logisticsmarts.net/")
        # self.pp.selectCompany(company="Windows")
        self.pp.openPersonRecord(lastName="Test1", firstName="Test1")
        self.pp.editProfile(idcard="Test", passport="Test", dob="20190707", anniversary="20190707")
        result = self.pp.verifyEditProfile(idcard="Test", passport="Test")
        self.ts.markFinal(testName="test_editProfile", result=result, resultMessage="Verify Edit Profile")

    @pytest.mark.run(order=7)
    def test_addInvalidPersonalComms(self):
        """
        Tests for verifying error in add personal comms form
        Uses TestStatus class to mark/assert test case results
        """
        self.log.info("*#" * 20)
        self.log.info("test_addInvalidPersonalComms started")
        self.log.info("*#" * 20)
        result = self.pp.invalidAddPersonalComms()
        self.ts.markFinal(testName="test_addInvalidPersonalComms", result=result, resultMessage="Verify Invalid Add Personal Comms")

    @pytest.mark.run(order=8)
    def test_addPersonalComms(self):
        """
        Test for Add Personal Comms working
        Person "Test, Test" should exist
        """
        self.log.info("*#" * 20)
        self.log.info("test_addPersonalComms started")
        self.log.info("*#" * 20)
        # self.driver.get("https://logisticsmarts.net/")
        # self.pp.selectCompany(company="Windows")
        # self.pp.openPersonRecord(lastName="Test", firstName="Test")
        self.pp.addPersonalComms(commsType="Direct", commsData="Test", countryCode="00", areaCode="00", notes="Test")
        self.pp.openPersonRecord(lastName="Test1", firstName="Test1")
        result = self.pp.verifyAddPersonalComms(commsType="Direct", commsData="Test")
        self.ts.markFinal(testName="test_addPersonalComms", result=result, resultMessage="Verify Add Personal Comms")

    @pytest.mark.run(order=9)
    def test_deletePersonalComms(self):
        """
        Test for Delete Personal Comms working
        Person "Test, Test" should exist
        """
        self.log.info("*#" * 20)
        self.log.info("test_deletePersonalComms started")
        self.log.info("*#" * 20)
        # self.driver.get("https://logisticsmarts.net/")
        # self.pp.selectCompany(company="Windows")
        # self.pp.openPersonRecord(lastName="Test", firstName="Test")
        self.pp.deletePersonalComms(commsData="Test")
        result = self.pp.verifyDeletePersonalComms(commsData="Test")
        self.ts.markFinal(testName="test_deletePersonalComms", result=result,
                          resultMessage="Verify Delete Personal Comms")

    @pytest.mark.run(order=10)
    def test_deletePerson(self):
        """
        Test for Delete Person working
        Person "Test, Test" should exist
        """
        self.log.info("*#" * 20)
        self.log.info("test_deletePerson started")
        self.log.info("*#" * 20)
        # self.driver.get("https://logisticsmarts.net/")
        # self.pp.selectCompany(company="Windows")
        self.pp.deletePerson(lastName="Test1", firstName="Test1")
        result = not(self.pp.verifyPersonRecord(firstName="Test1", lastName="Test1"))
        self.ts.markFinal(testName="test_deletePerson", result=result,
                          resultMessage="Verify Delete Person")

