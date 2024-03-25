import unittest
import HtmlTestRunner

from tests.ui_test.board_page_test import BoardPageTests
from tests.ui_test.card_page_test import CardPageTests
from tests.ui_test.home_page_test import HomePageTests
from tests.ui_test.login_page_test import LoginPageTests

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(BoardPageTests('test_all_tests'))
    suite.addTest(CardPageTests('test_all_tests'))
    runner = HtmlTestRunner.HTMLTestRunner(output='test-reports')
    runner.run(suite)
