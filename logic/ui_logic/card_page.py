from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from infra.base_page import BasePage


class CardPage(BasePage):
    DESCRIPTION_BTN_XPATH = "//p[@dir='auto']"
    DESCRIPTION_FILED_XPATH = "//div[@id='ak-editor-textarea']"
    SAVE_DESCRIPTION_CHANGE_BTN_XPATH = "//button[normalize-space()='Save']"
    WRITE_COMMENT_BTN_XPATH = "//input[@placeholder='Write a comment…']"
    COMMENT_FILED_XPATH = "(//div[@id='ak-editor-textarea'])[2]"
    SAVE_COMMENT_BTN_XPATH = "//button[@class='bxgKMAm3lq5BpA SdamsUKjxSBwGb SEj5vUdI3VvxDc']"
    LABELS_BTN_XPATH = "//a[@title='Labels']"
    GREEN_LABEL_XPATH = "//span[@aria-label='Color: green, title: none']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_to_change_description(self):
        click_change_description_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.DESCRIPTION_BTN_XPATH)))
        click_change_description_btn.click()

    def insert_description_text(self, description):
        description_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.DESCRIPTION_FILED_XPATH)))
        description_field.clear()
        description_field.send_keys(description)

    def click_save_description(self):
        save_description_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SAVE_DESCRIPTION_CHANGE_BTN_XPATH)))
        save_description_btn.click()

    def click_to_write_new_comment(self):
        click_write_new_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.WRITE_COMMENT_BTN_XPATH)))
        click_write_new_btn.click()

    def insert_the_comment_text(self, comment_txt):
        comment_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.COMMENT_FILED_XPATH)))
        comment_field.send_keys(comment_txt)

    def click_save_comment(self):
        save_comment_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.SAVE_COMMENT_BTN_XPATH)))
        save_comment_btn.click()

    def click_on_labels(self):
        labels_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.LABELS_BTN_XPATH)))
        labels_btn.click()

    def click_add_green_label(self):
        green_label = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.GREEN_LABEL_XPATH)))
        green_label.click()

    def change_card_description(self, description):
        try:
            self.click_to_change_description()
            self.insert_description_text(description)
            self.click_save_description()
            return True
        except Exception as e:
            print(e)
            return False

    def write_new_comment(self, comment_txt):
        try:
            self.click_to_write_new_comment()
            self.insert_the_comment_text(comment_txt)
            self.click_save_comment()
            return True
        except Exception as e:
            print(e)
            return False

    def add_label(self):
        try:
            self.click_on_labels()
            #self.click_add_green_label()
            return True
        except Exception as e:
            print(e)
            return False
