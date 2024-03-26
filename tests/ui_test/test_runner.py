import concurrent.futures
from selenium import webdriver

from tests.ui_test.card_page_test import CardPageTests
from utility.jira_operations import create_jira_issue


class TestRunner:
    def __init__(self, test_class, browser_options_list):
        self.test_class = test_class
        self.browser_options_list = browser_options_list

    def run_tests(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for option in self.browser_options_list:
                futures.append(executor.submit(self._run_tests_with_browser, option))

            # Wait for all futures to complete
            for future in concurrent.futures.as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    print(f"An error occurred: {e}")

    def _run_tests_with_browser(self, option):
        print(f"Running tests with browser option: {option}")
        tests = [
            getattr(self.test_class, method_name)
            for method_name in dir(self.test_class)
            if method_name.startswith("test_") and callable(getattr(self.test_class, method_name))
        ]
        for test_method in tests:
            test_instance = self.test_class()
            test_instance.setUp()
            try:
                test_method(test_instance, option=option)
            except AssertionError as e:
                print(f"Test failed: {e}")
                # Create Jira issue for failed test
                issue_summary = f"Failed test: {test_method.__name__}"
                issue_description = f"Test failed with message: {e}"
                create_jira_issue(issue_summary, issue_description)
            finally:
                test_instance.tearDown()


if __name__ == "__main__":
    browser_options = [webdriver.ChromeOptions(), webdriver.FirefoxOptions()]  # Add more options as needed
    test_runner = TestRunner(CardPageTests, browser_options)
    test_runner.run_tests()
