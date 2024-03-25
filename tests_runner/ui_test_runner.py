import unittest
import HtmlTestRunner

from tests.ui_test.board_page_test import BoardPageTests
from tests.ui_test.card_page_test import CardPageTests

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(BoardPageTests('run_all_tests'))
    suite.addTest(CardPageTests('run_all_tests'))

    runner = HtmlTestRunner.HTMLTestRunner(output='test-reports')
    runner.run(suite)
