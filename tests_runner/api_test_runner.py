import concurrent.futures
import unittest

from HtmlTestRunner import HTMLTestRunner

from infra.api_wrapper import APIWrapper
from tests.api_test.board_test import BoardTest
from tests.api_test.card_test import CardTest
from tests.api_test.list_in_board_test import ListInBoardTest
from tests.api_test.list_test import ListTest

if __name__ == "__main__":
    # Create a test suite containing all the test cases
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    # Add all your test classes to the suite
    suite.addTests(loader.loadTestsFromTestCase(ListTest))
    suite.addTests(loader.loadTestsFromTestCase(BoardTest))
    # Add other test classes similarly

    # Run the tests concurrently
    with concurrent.futures.ThreadPoolExecutor() as executor:
        test_results = list(executor.map(unittest.TextTestRunner().run, [suite]))


