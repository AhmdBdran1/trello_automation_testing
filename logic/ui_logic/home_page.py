from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage


class HomePage(BasePage):
    BOARD_ITEM_XPATH = "//div[@class='all-boards']//li[1]"
    CREATE_NEW_BOARD_XPATH = "//li[@data-testid='create-board-tile']"
    BOARD_TITLE_XPATH = "//input[@type='text']"
    CLICK_TO_CREATE_XPATH = "//button[contains(text(),'Create')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_on_board(self):
        try:
            board_btn = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, self.BOARD_ITEM_XPATH)))
            board_btn.click()
            return True

        except Exception as e:
            print(e)
            return False

    def click_to_create_new_board(self):
        create_new_board_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.CREATE_NEW_BOARD_XPATH)))
        create_new_board_btn.click()

    def insert_board_title(self, title):
        title_field = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.BOARD_TITLE_XPATH)))
        title_field.send_keys(title)

    def click_on_create(self):
        click_on_create_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.CLICK_TO_CREATE_XPATH)))
        click_on_create_btn.click()

    def create_new_board(self, title):
        try:
            self.click_to_create_new_board()
            self.insert_board_title(title)
            self.click_on_create()
            return True
        except Exception as e:
            print(e)
            return False
