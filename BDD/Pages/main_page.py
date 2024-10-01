from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import logging

from browser import Browser

class Main_page(Browser):
    PRODUCT_SORT_CONTAINER = (By.XPATH, '//*[@class= "product_sort_container"]')
    INVENTORY_ITEM_PRICE = (By.XPATH, '//*[@class = "inventory_item_price"]')
    INVENTORY_ITEM_NAME = (By.XPATH, '//*[@class = "inventory_item_name"]')
    ADD_TO_CART_BTN = (By.XPATH, '//button[contains(text(),"Add to cart")]')
    REMOVE_SAUCE_LABS_BACKPACK_BTN_INPUT = (By.XPATH, '//button[@class="btn btn_secondary btn_small btn_inventory')
    SWAG_LABS_LOGO = (By.XPATH, '//*[@class = "app_logo"]')


def i_click_on_the_sort_button(self):
        try:
            sort_items = self.chrome.find_element(*self.PRODUCT_SORT_CONTAINER)
            sort_items.click()
            logging.info('The sorting options were successfully shown on the tab')
        except Exception as e:
            logging.error(f'An error occurred while showing the sort options : {str(e)}')

    def i_click_on_the_option_price_low_to_high(self):
        try:
            sort_items = self.chrome.find_element(*self.INVENTORY_ITEM_PRICE)
            sort_items.click()
            logging.info('The items were successfully sorted from low price to high price')
        except Exception as e:
            logging.error(f'An error occurred while sorting the items prices : {str(e)}')

    def prices_are_sorted_from_low_to_high(self):
        try:
            sort_items_1 = self.chrome.find_element(*self.PRODUCT_SORT_CONTAINER)
            assert not sort_items_1.is_displayed()
            logging.info('The prices are shown from low to high')
        except Exception as e:
            logging.error(f'An error occurred while showing the prices from low to high : {str(e)}')

    def i_click_on_the_option_price_high_to_low(self):
        try:
            sort_items = self.chrome.find_element(*self.INVENTORY_ITEM_PRICE)
            sort_items.click()
            logging.info('The items were successfully sorted from high price to low price')
        except Exception as e:
            logging.error(f'An error occurred while sorting the items prices : {str(e)}')

    def prices_are_sorted_from_high_to_low(self):
        try:
            sort_items_1 = self.chrome.find_element(*self.PRODUCT_SORT_CONTAINER)
            assert not sort_items_1.is_displayed()
            logging.info('The prices are shown from high to low')
        except Exception as e:
            logging.error(f'An error occurred while showing the prices from high to low : {str(e)}')

    def i_click_on_the_option_name_A_to_Z(self):
        try:
            sort_items = self.chrome.find_element(*self.INVENTORY_ITEM_NAME)
            sort_items.click()
            logging.info('The items were successfully sorted from A to Z')
        except Exception as e:
            logging.error(f'An error occurred while sorting the items names : {str(e)}')

    def items_are_sorted_from_A_to_Z(self):
        try:
            sort_items_1 = self.chrome.find_element(*self.PRODUCT_SORT_CONTAINER)
            assert not sort_items_1.is_displayed()
            logging.info('The names are shown from A to Z')
        except Exception as e:
            logging.error(f'An error occurred while showing the names from A to Z : {str(e)}')

    def i_click_on_the_option_name_Z_to_A(self):
        try:
            sort_items = self.chrome.find_element(*self.INVENTORY_ITEM_NAME)
            sort_items.click()
            logging.info('The items were successfully sorted from Z to A')
        except Exception as e:
            logging.error(f'An error occurred while sorting the items names : {str(e)}')

    def items_are_sorted_from_Z_to_A(self):
        try:
            sort_items_1 = self.chrome.find_element(*self.PRODUCT_SORT_CONTAINER)
            assert not sort_items_1.is_displayed()
            logging.info('The items are shown from Z to A')
        except Exception as e:
            logging.error(f'An error occurred while showing the names from Z to A : {str(e)}')


    def i_click_on_the_add_to_cart_button(self):
        try:
            add_to_cart = self.chrome.find_element(*self.ADD_TO_CART_BTN)
            add_to_cart.click()
            logging.info('The item was added to cart')
        except Exception as e:
            logging.error(f'An error occurred while adding the item to cart : {str(e)}')

    def i_click_on_the_remove_button(self):
        try:
            add_to_cart = self.chrome.find_element(*self.REMOVE_SAUCE_LABS_BACKPACK_BTN_INPUT)
            add_to_cart.click()
            logging.info('The item was removed from cart')
        except Exception as e:
            logging.error(f'An error occurred while removing the item from cart : {str(e)}')

    def the_product_is_removed_from_cart(self):
        try:
            sort_items_1 = self.chrome.find_element(*self.REMOVE_SAUCE_LABS_BACKPACK_BTN_INPUT)
            assert not sort_items_1.is_displayed()
            logging.info('The option is like before pushing the button')
        except Exception as e:
            logging.error(f'An error occurred while showing the change on the website : {str(e)}')

    def the_logo_is_displayed(self):
        try:
            logo = WebDriverWait(self.chrome, 10).until(EC.visibility_of_element_located(self.SW)



