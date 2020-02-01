"""
Demo test suite file
"""

import unittest
from tests.home.login_tests import LoginTests
from tests.prime.person_test_csv_data import AddMultiplePersonCSVDataTests


# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(AddMultiplePersonCSVDataTests)

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)
