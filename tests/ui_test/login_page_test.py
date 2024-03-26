import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from infra.browser_wrapper import BrowserWrapper
from logic.ui_logic.login_page import Login
from utility.teardown_utilis import check_the_result_of_test


class LoginPageTests(unittest.TestCase):

    def setUp(self):
        self.browser_wrapper = BrowserWrapper()

    def tearDown(self):
        check_the_result_of_test(self)

    def test_login(self, option=webdriver.ChromeOptions()):  # test the login proces
        driver = self.browser_wrapper.get_driver(option)
        login_page = Login(driver)
        self.assertTrue(login_page.login())

    def test_login_page_load_time(self, option=webdriver.ChromeOptions()):
        start_time = time.time()
        driver = self.browser_wrapper.get_driver(option)
        # Wait until document.readyState is complete
        WebDriverWait(driver, 10).until(
            lambda drive: driver.execute_script("return document.readyState") == "complete")
        end_time = time.time()
        load_time = end_time - start_time
        print("Page load time:", load_time, "seconds")
        driver.quit()
        self.assertLessEqual(load_time, 20, "Page load time exceeds 10 seconds")


if __name__ == "__main__":
    unittest.main()
