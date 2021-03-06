"""
Tests using ddt module for multiple data sets
"""

from pages.prime.person_page import PersonPage
from utilities.teststatus import TestStatus
import unittest, pytest
from ddt import ddt, data, unpack
import utilities.custom_logger as cl
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class AddMultiplePersonTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        """
        Class object(s) setup
        """
        self.pp = PersonPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(("First1", "Last1"), ("First2", "Last2"))
    @unpack
    def test_addPerson(self, firstName, lastName):
        """
        Tests for adding multiple person record and verifies its presence in the person list
        Uses TestStatus class to mark/assert test case results
        """
        self.log.info("*#" * 20)
        self.log.info("test_addPerson started")
        self.log.info("*#" * 20)
        self.pp.addPerson(firstName=firstName, lastName=lastName)
        result = self.pp.verifyPersonRecord(firstName=firstName, lastName=lastName)
        self.ts.markFinal(testName="test_addPerson", result=result, resultMessage="Verify Add Person")
        self.driver.get("https://logisticsmarts.net/")

