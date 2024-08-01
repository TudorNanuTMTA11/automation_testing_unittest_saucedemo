from selenium.webdriver.common.by import By
from unittest import TestCase

from seleniumbase import Driver

class Test_Login(TestCase):
    LOGIN_USER_INPUT = (By.ID, 'user-name')
    LOGIN_PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BTN_INPUT = (By.ID, 'login-button')
    LOGIN_ERROR_MESSAGE = (By.XPATH, '//*[@class = "error-message-container error"]')