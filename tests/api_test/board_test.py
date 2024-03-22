import unittest

from infra.api_wrapper import APIWrapper
from logic.api_logic.board_endpoints import BoardEndPoints
from utility.teardown_utilis import check_the_result_of_test


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.my_api = APIWrapper()
        self.board_endpoint = BoardEndPoints(self.my_api)

    def tearDown(self):
        check_the_result_of_test(self)  # Check if the test failed

    def test_add_new_board(self):
        response = self.board_endpoint.create_new_board()
        self.assertTrue(response.status_code == 200)


if __name__ == "__main__":
    unittest.main()
