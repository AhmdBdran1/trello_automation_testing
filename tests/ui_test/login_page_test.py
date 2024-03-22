import unittest
from selenium import webdriver
from infra.browser_wrapper import BrowserWrapper
from logic.ui_logic.login_page import Login
from utility.jira_operations import create_jira_issue


class LoginPageTests(unittest.TestCase):

    def setUp(self):
        self.browser_wrapper = BrowserWrapper()

    def tearDown(self):
        # Check if the test failed
        if hasattr(self, '_outcome') and self._outcome.result:
            result = self._outcome.result
            if result.errors or result.failures:
                # If test fails, create a JIRA issue
                test_method_name = self._testMethodName
                error_message = ""
                for test, traceback_text in result.errors + result.failures:
                    error_message += f"Test: {test}\n"
                    error_message += f"Error: {traceback_text}\n"
                create_jira_issue(f"{test_method_name} Test Failed", error_message)

    def test_login(self, option=webdriver.ChromeOptions()):  # test the login processs
        driver = self.browser_wrapper.get_driver(option)
        login_page = Login(driver)
        self.assertTrue(login_page.login())


if __name__ == "__main__":
    unittest.main()
