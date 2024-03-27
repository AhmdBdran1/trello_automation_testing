import unittest
from infra.api_wrapper import APIWrapper
from logic.api_logic.board_endpoints import BoardEndPoints
from utility.teardown_utilis import check_the_result_of_test


class BoardTest(unittest.TestCase):

    def setUp(self):
        self.my_api = APIWrapper()
        self.board_endpoint = BoardEndPoints(self.my_api)
        self.response = self.board_endpoint.create_new_board("new board")
        response_data = self.response.json()
        self.board_id = response_data['id']

    def tearDown(self):
        check_the_result_of_test(self)  # if the test failed create jira bug issue
        self.board_endpoint.delete_a_board(self.board_id)

    def test_add_new_board(self):
        self.assertTrue(self.response.status_code == 200)

    def test_update_board_name(self):
        response = self.board_endpoint.update_board_name(self.board_id, "updated")
        self.assertTrue(response.status_code == 200)

    def test_invite_someone_to_board_via_email(self):
        response = self.board_endpoint.invite_person_to_board_via_email(self.board_id, "ahmd1997bdran@gmail.com")
        self.assertTrue(response.status_code == 200)


if __name__ == "__main__":
    unittest.main()
