
import unittest

from infra.api_wrapper import APIWrapper
from logic.api_logic.board_endpoints import BoardEndPoints
from logic.api_logic.card_endpoints import CardEndPoints
from logic.api_logic.list_endpoints import ListEndPoints
from utility.name_generator import generate_random_name
from utility.teardown_utilis import check_the_result_of_test


class NegativeTest(unittest.TestCase):
    def setUp(self):
        self.my_api = APIWrapper()
        self.board_endpoint = BoardEndPoints(self.my_api)
        self.list_endpoints = ListEndPoints(self.my_api)
        self.card_endpoints = CardEndPoints(self.my_api)
        self.board_name = generate_random_name()
        self.response = self.board_endpoint.create_new_board(self.board_name)
        response_data = self.response.json()
        self.board_id = response_data['id']
        self.list_name = generate_random_name()
        self.new_list_response = self.list_endpoints.create_new_list(self.board_id, self.list_name)
        new_list_response_data = self.new_list_response.json()
        self.list_id = new_list_response_data['id']
        self.card_name = generate_random_name()
        self.new_card_response = self.card_endpoints.create_new_card(self.list_id, self.card_name)
        new_card_response_data = self.new_card_response.json()
        self.card_id = new_card_response_data['id']

    def tearDown(self):
        check_the_result_of_test(self)  # if the test failed create jira bug issue
        self.board_endpoint.delete_a_board(self.board_id)

    def test_get_card_with_wrong_api_token(self):  # security testing
        response = self.card_endpoints.get_card_with_wrong_api_token(self.card_id)
        self.assertEqual(response, 200)


if __name__ == "__main__":
    unittest.main()
