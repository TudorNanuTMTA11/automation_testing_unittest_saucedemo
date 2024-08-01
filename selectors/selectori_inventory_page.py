from selenium.webdriver.common.by import By
from unittest import TestCase
from selenium.webdriver.support.select import Select
from seleniumbase import Driver

class Test_Inventory(TestCase):
    PRODUCT_SORT_CONTAINER = (By.XPATH, '//*[@class= "product_sort_container"]')
    INVENTORY_ITEM_PRICE = (By.XPATH, '//*[@class = "inventory_item_price"]')
    ADD_TO_CART_BTN = (By.XPATH, '//button[contains(text(),"Add to cart")]')
    INVENTORY_ITEM_NAME = (By.XPATH, '//*[@class = "inventory_item_name"]')
    SHOPPING_CART_CONTAINER_SAUCE_LABS_BACKPACK = (By.XPATH, '//*[@class = "shopping_cart_container"]')
    SHOPPING_CART_LINK = (By.CLASS_NAME, 'shopping_cart_link')
    REMOVE_SAUCE_LABS_BACKPACK_BTN_INPUT = (By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button')
    SWAG_LABS_LOGO = (By.XPATH, '//*[@class = "app_logo"]')