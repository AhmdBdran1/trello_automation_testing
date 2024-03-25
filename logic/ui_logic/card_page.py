from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage


class CardPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


