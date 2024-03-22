import unittest
from logic.api_logic.board_endpoints import BoardEndPoints
from utility.jira_operations import create_jira_issue


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.board_endpoint = BoardEndPoints()

    def tearDown(self):
        # Check if the test failed
        if hasattr(self, '_outcome') and self._outcome.result:
            result = self._outcome.result
            if result.errors or result.failures:
                # If test fails, create a JIRA issue
                test_method_name = self._testMethodName
                error_message = ""
                for test, traceback_text in result.errors + result.failures:
                    error_message += f"Test: {test}\n"
                    error_message += f"Error: {traceback_text}\n"
                create_jira_issue(f"{test_method_name} Test Failed", error_message)

    def test_add_new_board(self):
        response = self.board_endpoint.create_new_board()
        data = response.json()
        self.assertTrue(response.status_code == 200)


if __name__ == "__main__":
    unittest.main()
