from utility.jira_operations import create_jira_issue


def check_the_result_of_test(self):
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
