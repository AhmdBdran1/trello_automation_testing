import json
from selenium import webdriver
import os
import concurrent.futures

from utility.json_files_reader import read_config


class BrowserWrapper:
    def __init__(self):
        self.driver = None

    def get_driver(self, option):  # create driver based on config content
        config = read_config()
        grid = config['grid']
        hub_url = config['hub_url']
        url = config['url']
        option.add_argument('--headless')  # This line makes Chrome run in headless mode
        option.add_argument('--no--sandbox')
        option.add_argument('--disable-dev-shm-usage')
        option.add_argument('--window-size=1920x1080')

        if grid:
            print(option.to_capabilities())
            driver = webdriver.Remote(command_executor=hub_url, options=option)
            driver.get(url)
            driver.maximize_window()
            return driver
        else:
            driver = webdriver.Chrome(option)
            driver.get(url)
            driver.maximize_window()
            return driver

    def test_run_grid_serial(self, test_execute):  # run the test with serial proces
        cap_list = self.get_capabilities_list()
        for caps in cap_list:
            test_execute(caps)

    def test_run_grid_parallel(self, test_execute):
        options_list = self.get_capabilities_list()
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(options_list)) as executor:
            list(executor.map(test_execute, options_list))

    def run_test(self, test_execute): # add commentt
        config = read_config()
        grid = config['grid']
        if grid:
            self.test_run_grid_parallel(test_execute)
        else:
            self.test_run_grid_serial(test_execute)

    def get_capabilities_list(self):  # initialize the capabilities we need to test on
        chrome_cap = webdriver.ChromeOptions()
        firefox_cap = webdriver.FirefoxOptions()
        cap_list = [firefox_cap, chrome_cap]
        return cap_list
