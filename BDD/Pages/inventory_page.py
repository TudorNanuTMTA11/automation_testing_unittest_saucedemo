from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By
from browser import Browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import logging


class Browser:
    s = Service(ChromeDriverManager().install())
    chrome = webdriver.Chrome(service=s)
    logging.basicConfig(level=logging.INFO)


class Inventory_page(browser):
    LOGIN_BUTTON = (By.ID, "login-button")
    USER_NAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    def open_inventory_page(self):
        self.chrome.get("https://www.saucedemo.com/")



    def insert_username(self):
        try:
            user_name= self.chrome.find_element(*self.USER_NAME)
            user_name.send_keys("standard_user")
        except Exception as i:
            logging.error(f"An error occurred while inserting the username : {str(i)}")

    def insert_invalid_password(self, password):
        try:
            user_password = self.chrome.find_element(self.PASSWORD)
            user_password.send_keys(password)
        except Exception as i:
            logging.error(f"An error occurred while inserting the password : {str(i)}")

    def click_login_button(self):
        max_try = 3
        attempts = 0
        while attempts < max_try:
            try:
                login_button = self.chrome.find_element(*self.LOGIN_BUTTON)
                if login_button:
                    login_button.click()
                    break
                else:
                    raise AssertionError('Login button element was not found')
            except Exception as i:
                logging.error(f"An error occurred while clicking the login button : {str(i)}")
                attempts += 1

    def login_failed(self, error_message):
        try:
            alerta = self.chrome.switch_to.alert
            alerta_text = alerta.text
            assert error_message in alerta_text
            logging.info("Login failed.format(error_message")
        except NoAlertPresentException
            assert False, "Expected alert not found"
