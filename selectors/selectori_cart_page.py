from selenium.webdriver.common.by import By
from unittest import TestCase
from selenium.webdriver.support.select import Select
from seleniumbase import Driver

CHECKOUT_BTN = (By.ID,'checkout')
REMOVE_PRODUCT = (By.ID, 'remove-sauce-labs-backpack')
CONTINUE_SHOPPING_BTN = (By.ID, 'continue-shopping')