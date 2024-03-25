import unittest
import HtmlTestRunner

from tests.ui_test.board_page_test import BoardPageTests
from tests.ui_test.card_page_test import CardPageTests


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(BoardPageTests('test_all_tests'))
    suite.addTest(CardPageTests('test_all_tests'))
    suite.addTest(CardPageTests('test_to_simulate_failure_situation'))
    runner = HtmlTestRunner.HTMLTestRunner(output='test-reports')
    runner.run(suite)
