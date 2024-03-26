from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage


class BoardPage(BasePage):

    ADD_ANOTHER_LIST_XPATH = "//button[normalize-space()='Add another list']"
    ENTER_LIST_TITLE_XPATH = "//textarea[@placeholder='Enter list title…']"
    ADD_LIST_BTN_XPATH = "//button[normalize-space()='Add list']"
    ADD_A_CARD_XPATH = "(//button[@type='button'][normalize-space()='Add a card'])[1]"
    ENTER_CARD_TITLE_XPATH = "//textarea[@placeholder='Enter a title for this card…']"
    ADD_CARD_XPATH = "//button[normalize-space()='Add card']"
    OPEN_THE_CARD_XPATH = "//li[@class='T9JQSaXUsHTEzk']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_on_add_another_list(self):
        add_another_list_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.ADD_ANOTHER_LIST_XPATH)))
        add_another_list_btn.click()

    def insert_list_title(self, list_title):
        title_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.ENTER_LIST_TITLE_XPATH)))
        title_field.send_keys(list_title)

    def click_add_list(self):
        add_list_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ADD_LIST_BTN_XPATH)))
        add_list_btn.click()

    def click_on_add_new_card(self):
        add_new_card_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ADD_A_CARD_XPATH)))
        add_new_card_btn.click()

    def insert_card_title(self, list_title):
        title_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.ENTER_CARD_TITLE_XPATH)))
        title_field.send_keys(list_title)

    def click_add_card(self):
        add_card_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.ADD_CARD_XPATH)))
        add_card_btn.click()

    def click_on_the_card(self):
        click_on_go_into_the_card = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.OPEN_THE_CARD_XPATH)))
        click_on_go_into_the_card.click()

    def add_another_list(self, list_title):
        try:
            self.click_on_add_another_list()
            self.insert_list_title(list_title)
            self.click_add_list()
            return True
        except Exception as e:
            print(e)
            return False

    def add_new_card(self, card_title):
        try:
            self.click_on_add_new_card()
            self.insert_card_title(card_title)
            self.click_add_card()
            return True
        except Exception as e:
            print(e)
            return False



