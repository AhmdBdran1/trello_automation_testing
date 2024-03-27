import unittest
from selenium import webdriver
from infra.api_wrapper import APIWrapper
from infra.browser_wrapper import BrowserWrapper
from logic.api_logic.board_endpoints import BoardEndPoints
from logic.ui_logic.board_page import BoardPage
from logic.ui_logic.home_page import HomePage
from logic.ui_logic.login_page import Login
from utility.name_generator import generate_random_name
from utility.teardown_utilis import check_the_result_of_test


class BoardPageTests(unittest.TestCase):

    def setUp(self):
        self.browser_wrapper = BrowserWrapper()
        self.my_api = APIWrapper()
        self.board_endpoint = BoardEndPoints(self.my_api)
        board_name = generate_random_name()
        self.response = self.board_endpoint.create_new_board(board_name)
        response_data = self.response.json()
        self.board_id = response_data['id']

    def tearDown(self):
        check_the_result_of_test(self)  # if the test failed create jira bug
        self.board_endpoint.delete_a_board(self.board_id)

    def test_add_new_list(self, option=webdriver.ChromeOptions()):  # testing adding new list functionality
        driver = self.browser_wrapper.get_driver(option)
        login_page = Login(driver)
        login_page.login()
        home_page = HomePage(driver)
        home_page.click_on_board()
        board_page = BoardPage(driver)
        list_name = generate_random_name()
        boolean = board_page.add_another_list(list_name)
        driver.quit()
        self.assertTrue(boolean)

    def test_add_new_card(self, option=webdriver.ChromeOptions()):  # testing adding new card
        driver = self.browser_wrapper.get_driver(option)
        login_page = Login(driver)
        login_page.login()
        home_page = HomePage(driver)
        home_page.click_on_board()
        board_page = BoardPage(driver)
        card_name = generate_random_name()
        boolean = board_page.add_new_card(card_name)
        driver.quit()
        self.assertTrue(boolean)

    def test_all_tests(self):  # run all tests
        tests_list = [self.test_add_new_card, self.test_add_new_list]
        for test in tests_list:
            self.browser_wrapper.run_test(test)


if __name__ == "__main__":
    unittest.main()
