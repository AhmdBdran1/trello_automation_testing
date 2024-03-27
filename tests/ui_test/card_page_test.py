import unittest
from time import sleep

from selenium import webdriver
from infra.api_wrapper import APIWrapper
from infra.browser_wrapper import BrowserWrapper
from logic.api_logic.board_endpoints import BoardEndPoints
from logic.api_logic.card_endpoints import CardEndPoints
from logic.api_logic.list_endpoints import ListEndPoints
from logic.ui_logic.board_page import BoardPage
from logic.ui_logic.card_page import CardPage
from logic.ui_logic.home_page import HomePage
from logic.ui_logic.login_page import Login
from utility.name_generator import generate_random_name
from utility.teardown_utilis import check_the_result_of_test


class CardPageTests(unittest.TestCase):

    def setUp(self):
        self.browser_wrapper = BrowserWrapper()
        self.my_api = APIWrapper()
        self.board_endpoint = BoardEndPoints(self.my_api)
        board_name = generate_random_name()  # generate random name for board
        self.response = self.board_endpoint.create_new_board(board_name)
        response_data = self.response.json()
        self.board_id = response_data['id']
        self.list_endpoints = ListEndPoints(self.my_api)
        list_name = generate_random_name()  # generate random name for list
        response = self.list_endpoints.create_new_list(self.board_id, list_name)
        response_data = response.json()
        list_id = response_data['id']
        self.card_endpoints = CardEndPoints(self.my_api)
        card_name = generate_random_name()  # generate random name for the card
        response = self.card_endpoints.create_new_card(list_id, card_name)
        response_data = response.json()
        self.card_id = response_data['id']

    def tearDown(self):
        check_the_result_of_test(self)
        self.board_endpoint.delete_a_board(self.board_id)

    def test_to_simulate_failure_situation(self, option=webdriver.ChromeOptions()):
        driver = self.browser_wrapper.get_driver(option)
        login_page = Login(driver)
        login_page.login()
        home_page = HomePage(driver)
        home_page.click_on_board()
        board_page = BoardPage(driver)
        board_page.click_on_the_card()
        self.assertTrue(False)

    def test_change_card_description(self, option=webdriver.ChromeOptions()):
        try:
            driver = self.browser_wrapper.get_driver(option)
            login_page = Login(driver)
            login_page.login()
            home_page = HomePage(driver)
            home_page.click_on_board()
            board_page = BoardPage(driver)
            board_page.click_on_the_card()
            card_page = CardPage(driver)
            card_page.change_card_description("new description")
            response = self.card_endpoints.get_a_card(self.card_id)
            response_data = response.json()
            description = response_data['desc']
            driver.quit()
            self.assertIn('new description', description)
        except Exception as e:
            self.fail("Test failed: {}".format(e))

    def test_add_comment_for_card(self, option=webdriver.ChromeOptions()):
        driver = self.browser_wrapper.get_driver(option)
        login_page = Login(driver)
        login_page.login()
        home_page = HomePage(driver)
        home_page.click_on_board()
        board_page = BoardPage(driver)
        board_page.click_on_the_card()
        card_page = CardPage(driver)
        boolean = card_page.write_new_comment("new comment")
        driver.quit()
        self.assertTrue(boolean)

    def test_add_label_for_card(self, option=webdriver.ChromeOptions()):
        driver = self.browser_wrapper.get_driver(option)
        login_page = Login(driver)
        login_page.login()
        home_page = HomePage(driver)
        home_page.click_on_board()
        board_page = BoardPage(driver)
        board_page.click_on_the_card()
        card_page = CardPage(driver)
        boolean = card_page.add_label()
        driver.quit()
        self.assertTrue(boolean)

    def test_all_tests(self):  # run all tests
        tests_list = [self.test_add_comment_for_card, self.test_add_label_for_card]
        for test in tests_list:
            self.browser_wrapper.run_test(test)


if __name__ == "__main__":
    unittest.main()
