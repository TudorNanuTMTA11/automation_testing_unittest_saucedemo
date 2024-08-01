from selenium.webdriver.common.by import By
from unittest import TestCase
from selenium.webdriver.support.select import Select
from seleniumbase import Driver


class Test_Checkout(TestCase):
    FIRST_NAME = (By.ID, 'first-name')
    LAST_NAME = (By.ID, 'last-name')
    POSTAL_CODE = (By.ID, 'postal-code')
    CONTINUE_BTN = (By.ID, 'continue')
    ERROR_FIRST_NAME_MESSAGE = (By.XPATH, '//*[@class = "error-message-container error"]')
    ERROR_LAST_NAME_MESSAGE = (By.XPATH, '//*[@class="error-message-container error"]')
    ERROR_POSTAL_CODE_MESSAGE = (By.XPATH, '//*[@class="error-message-container error"]')
    CANCEL_BTN = (By.ID, 'cancel')
    FINISH_BTN = (By.ID, 'finish')
    BACK_TO_PRODUCTS = (By.ID, 'back-to-products')
