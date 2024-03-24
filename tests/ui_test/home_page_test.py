import unittest
from selenium import webdriver
from infra.api_wrapper import APIWrapper
from infra.browser_wrapper import BrowserWrapper
from logic.api_logic.board_endpoints import BoardEndPoints
from logic.ui_logic.home_page import HomePage
from logic.ui_logic.login_page import Login
from utility.teardown_utilis import check_the_result_of_test


class HomePageTests(unittest.TestCase):

    def setUp(self):
        self.browser_wrapper = BrowserWrapper()
        self.my_api = APIWrapper()
        self.board_endpoint = BoardEndPoints(self.my_api)
        self.response = self.board_endpoint.create_new_board("new board")
        response_data = self.response.json()
        self.board_id = response_data['id']

    def tearDown(self):
        check_the_result_of_test(self)  # if the test failed create jira bug
        self.board_endpoint.delete_a_board(self.board_id)

    def test_get_into_the_board(self, option=webdriver.ChromeOptions()):
        driver = self.browser_wrapper.get_driver(option)
        login_page = Login(driver)
        login_page.login()
        home_page = HomePage(driver)
        boolean = home_page.click_on_board()
        self.assertTrue(boolean)

    def test_create_new_board(self, option=webdriver.ChromeOptions()):
        driver = self.browser_wrapper.get_driver(option)
        login_page = Login(driver)
        login_page.login()
        home_page = HomePage(driver)
        boolean = home_page.create_new_board("test board")
        self.assertTrue(boolean)


if __name__ == "__main__":
    unittest.main()
