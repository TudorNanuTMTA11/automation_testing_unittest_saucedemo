from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By


import logging

from base_page import Base_page




class Login_page(Base_page):

    def open_login_page(self):
        self.chrome.get("https://www.saucedemo.com/")

    def login_failed(self, error_message):
        try:
            alerta = self.chrome.switch_to.alert
            alerta_text = alerta.text
            assert error_message in alerta_text
            logging.info("Login failed.format{error_message}")
        except NoAlertPresentException:
            assert False, "Expected alert not found"

    def main_page(self):
        page_url = "https://www.saucedemo.com/inventory.html"
        assert self.chrome.current_url == page_url, (f"An error occurred. Expected page_url {page_url}",
                                                             f"Actual current_url {self.chrome.current_url}")
