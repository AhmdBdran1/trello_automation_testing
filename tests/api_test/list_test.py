import json
import unittest

from infra.api_wrapper import APIWrapper
from logic.api_logic.board_endpoints import BoardEndPoints
from logic.api_logic.list_endpoints import ListEndPoints
from utility.teardown_utilis import check_the_result_of_test


class ListTest(unittest.TestCase):
    def setUp(self):
        self.my_api = APIWrapper()
        self.board_endpoint = BoardEndPoints(self.my_api)
        self.list_endpoints = ListEndPoints(self.my_api)
        self.response = self.board_endpoint.create_new_board("new board created")
        response_data = self.response.json()
        self.board_id = response_data['id']
        self.new_list_response = self.list_endpoints.create_new_list(self.board_id, "new list")
        new_list_response_data = self.new_list_response.json()
        self.list_id = new_list_response_data['id']

    def tearDown(self):
        check_the_result_of_test(self)  # if the test failed create jira bug issue
        self.board_endpoint.delete_a_board(self.board_id)

    def test_create_new_list(self):
        self.assertTrue(self.new_list_response.status_code == 200)

    def test_get_a_list(self):
        response = self.list_endpoints.get_a_list(self.list_id)
        self.assertTrue(response.status_code == 200)
        response_data = response.json()
        self.assertEqual(response_data['name'], 'new list')

    def test_update_list_name(self):
        response = self.list_endpoints.update_list_name(self.list_id, "new name")
        self.assertTrue(response.status_code == 200)
        response_data = response.json()
        self.assertEqual(response_data['name'], 'new name')

    def test_get_list_cards(self):
        response = self.list_endpoints.get_list_cards(self.list_id)
        self.assertTrue(response.status_code == 200)
        response_data = response.json()
        print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))


if __name__ == "__main__":
    unittest.main()
