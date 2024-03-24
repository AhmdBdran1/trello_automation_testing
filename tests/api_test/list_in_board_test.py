import unittest

from infra.api_wrapper import APIWrapper
from logic.api_logic.board_endpoints import BoardEndPoints
from logic.api_logic.list_in_board_endpoints import ListInBoardEndPoints
from utility.teardown_utilis import check_the_result_of_test


class ListTest(unittest.TestCase):
    def setUp(self):
        self.my_api = APIWrapper()
        self.board_endpoint = BoardEndPoints(self.my_api)
        self.response = self.board_endpoint.create_new_board("new board")
        response_data = self.response.json()
        self.board_id = response_data['id']
        self.list_endpoints = ListInBoardEndPoints(self.my_api, self.board_id)
        self.response = self.list_endpoints.create_list_on_a_board("create api tests")

    def tearDown(self):
        check_the_result_of_test(self)  # if the test failed create jira bug issuee
        self.board_endpoint.delete_a_board(self.board_id)

    def test_create_list_on_a_board(self):
        self.assertTrue(self.response.status_code == 200)

    def test_get_lists_on_a_board(self):
        response = self.list_endpoints.get_lists_on_a_board()
        self.assertTrue(response.status_code == 200)


if __name__ == "__main__":
    unittest.main()
