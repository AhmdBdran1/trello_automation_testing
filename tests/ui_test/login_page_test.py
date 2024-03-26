import unittest
from selenium import webdriver
from infra.browser_wrapper import BrowserWrapper
from logic.ui_logic.login_page import Login
from utility.teardown_utilis import check_the_result_of_test


class LoginPageTests(unittest.TestCase):

    def setUp(self):
        self.browser_wrapper = BrowserWrapper()

    def tearDown(self):
        print('done')

    def test_login(self, option=webdriver.ChromeOptions()):  # test the login proces
        driver = self.browser_wrapper.get_driver(option)
        login_page = Login(driver)
        self.assertTrue(login_page.login())


if __name__ == "__main__":
    unittest.main()
