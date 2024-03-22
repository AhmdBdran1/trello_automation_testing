import concurrent.futures
import unittest
import requests
from utility.json_files_reader import read_config


class APIWrapper:

    def __init__(self):
        self.response = None
        self.my_request = requests
        config = read_config()
        self.grid = config['grid']
        self.url = config['api_url']

    def api_get_request(self, endpoints, headers):
        self.response = self.my_request.get(self.url + endpoints, headers=headers)
        print(self.response)
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code

    def api_post_request(self, endpoints, params):
        self.response = self.my_request.post(endpoints, params=params)
        print(self.response)
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code

    def api_put_request(self, endpoints, data, headers):
        self.response = self.my_request.put(self.url + endpoints, json=data, headers=headers)
        print(self.response)
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code

    def api_delete_request(self, endpoints, headers):
        self.response = self.my_request.delete(self.url + endpoints, headers=headers)
        print(self.response)
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code

    # Define a function to run each test case
    def run_test_case(self, test_case):
        suite = unittest.TestLoader().loadTestsFromTestCase(test_case)
        unittest.TextTestRunner().run(suite)

    # Define the main function to run all test cases
    def run_tests(self, test_cases):
        if self.grid:
            self.run_tests_in_parallel(test_cases)
        else:
            self.run_test_in_serial(test_cases)

    # Define the main function to run all test cases concurrently
    def run_tests_in_parallel(self, test_cases):
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(test_cases)) as executor:
            executor.map(self.run_test_case, test_cases)

    # Define the main function to run all test cases in serial
    def run_test_in_serial(self, test_cases):
        for test_case in test_cases:
            self.run_test_case(test_case)
