import json
import unittest

from infra.api_wrapper import APIWrapper
from logic.api_logic.board_endpoints import BoardEndPoints
from logic.api_logic.card_endpoints import CardEndPoints
from logic.api_logic.list_endpoints import ListEndPoints
from utility.teardown_utilis import check_the_result_of_test


class CardTest(unittest.TestCase):
    def setUp(self):
        self.my_api = APIWrapper()
        self.board_endpoint = BoardEndPoints(self.my_api)
        self.list_endpoints = ListEndPoints(self.my_api)
        self.card_endpoints = CardEndPoints(self.my_api)
        self.response = self.board_endpoint.create_new_board("new board")
        response_data = self.response.json()
        self.board_id = response_data['id']
        self.new_list_response = self.list_endpoints.create_new_list(self.board_id, "new list")
        new_list_response_data = self.new_list_response.json()
        self.list_id = new_list_response_data['id']
        self.new_card_response = self.card_endpoints.create_new_card(self.list_id, "new card")
        new_card_response_data = self.new_card_response.json()
        self.card_id = new_card_response_data['id']

    def tearDown(self):
        check_the_result_of_test(self)  # if the test failed create jira bug issue
        self.board_endpoint.delete_a_board(self.board_id)

    def test_create_new_card(self):
        self.assertTrue(self.new_card_response.status_code == 200)

    def test_get_a_card(self):
        response = self.card_endpoints.get_a_card(self.card_id)
        self.assertTrue(response.status_code == 200)
        response_data = response.json()
        self.assertEqual(response_data['name'], 'new card')

    def test_update_card_name(self):
        response = self.card_endpoints.update_card_name(self.card_id, "new name")
        self.assertTrue(response.status_code == 200)
        response_data = response.json()
        self.assertEqual(response_data['name'], 'new name')

    def test_update_card_description(self):
        response = self.card_endpoints.update_card_description(self.card_id, "it's a new description")
        self.assertTrue(response.status_code == 200)
        response_data = response.json()
        self.assertEqual(response_data['desc'], "it's a new description")

    def test_delete_card(self):
        response = self.card_endpoints.delete_card(self.card_id)
        self.assertTrue(response.status_code == 200)


if __name__ == "__main__":
    unittest.main()
