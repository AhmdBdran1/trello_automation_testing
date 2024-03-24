import unittest
from time import sleep

from selenium import webdriver
from infra.api_wrapper import APIWrapper
from infra.browser_wrapper import BrowserWrapper
from logic.api_logic.board_endpoints import BoardEndPoints
from logic.api_logic.card_endpoints import CardEndPoints
from logic.api_logic.list_endpoints import ListEndPoints
from logic.ui_logic.board_page import BoardPage
from logic.ui_logic.home_page import HomePage
from logic.ui_logic.login_page import Login
from utility.teardown_utilis import check_the_result_of_test


class CardPageTests(unittest.TestCase):

    def setUp(self):
        self.browser_wrapper = BrowserWrapper()
        self.my_api = APIWrapper()
        self.board_endpoint = BoardEndPoints(self.my_api)
        self.response = self.board_endpoint.create_new_board("new board")  # GENERATE BOARD NAMEe
        response_data = self.response.json()
        self.board_id = response_data['id']
        self.list_endpoints = ListEndPoints(self.my_api)
        response = self.list_endpoints.create_new_list(self.board_id, "new list")
        response_data = response.json()
        list_id = response_data['id']
        self.card_endpoints = CardEndPoints(self.my_api)
        self.card_endpoints.create_new_card(list_id, 'new card')

    def tearDown(self):
        check_the_result_of_test(self)  # if the test failed create jira bug
        self.board_endpoint.delete_a_board(self.board_id)

    def test_go_into_card(self, option=webdriver.ChromeOptions()):
        driver = self.browser_wrapper.get_driver(option)
        login_page = Login(driver)
        login_page.login()
        home_page = HomePage(driver)
        home_page.click_on_board()
        board_page = BoardPage(driver)
        board_page.click_on_the_card()
        driver.quit()

    def test_all_tests(self):  # run all tests
        tests_list = [self.test_go_into_card]
        for test in tests_list:
            self.browser_wrapper.run_test(test)


if __name__ == "__main__":
    unittest.main()
