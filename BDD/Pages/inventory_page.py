from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By

import logging

from browser import Browser


class Inventory_page(Browser):
    LOGIN_BUTTON = (By.ID, "login-button")
    USER_NAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")

    def open_inventory_page(self):
        self.chrome.get("https://www.saucedemo.com/")

    def insert_username(self, username):
        try:
            user_name = self.chrome.find_element(*self.USER_NAME).send_keys(username)
        except Exception as i:
            logging.error(f"An error occurred while using the username : {str(i)}")

    def click_login_button(self):
        try:
            login_button = self.chrome.find_element(*self.LOGIN_BUTTON)
            if login_button:
                login_button.click()
            else:
                raise AssertionError('Login button element was not found')
        except Exception as i:
            logging.error(f"An error occurred while clicking the login button : {str(i)}")

    def login_failed(self, error_message):
        try:
            alerta = self.chrome.switch_to.alert
            alerta_text = alerta.text
            assert error_message in alerta_text
            logging.info("Login failed.format(error_message")
        except NoAlertPresentException:
            assert False, "Expected alert not found"

    def insert_password(self, user_password):
        try:
            userpassword = self.chrome.find_element(*self.PASSWORD).send_keys(user_password)
        except Exception as i:
            logging.error(f"An error occurred while using the password: {str(i)}")


    def main_page(self):
        page_url = "https://www.saucedemo.com/inventory.html"
        assert self.chrome.current_url == page_url, (f"An error occurred. Expected page_url {self.chrome.current_url}",
                                                             f"Actual current_url {page_url}")
