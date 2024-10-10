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
    SHOPPING_CART_LINK = (By.CLASS_NAME, 'shopping_cart_link')
    REMOVE_SAUCE_LABS_BACKPACK_BTN_INPUT = (By.XPATH, '//button[@class="btn btn_secondary btn_small btn_inventory')
    SWAG_LABS_LOGO = (By.XPATH, '//*[@class = "app_logo"]')
    CHECKOUT_BTN = (By.ID, 'checkout')
    FIRST_NAME = (By.ID, 'first-name')
    LAST_NAME = (By.ID, 'last-name')
    POSTAL_CODE = (By.ID, 'postal-code')
    CONTINUE_BTN = (By.ID, 'continue')
    FINISH_BTN = (By.ID, 'finish')
    ORDER_COMPLETE_MESSAGE = (By.XPATH, '//div[@id="checkout_complete_container"]//h2')
    REMOVE_PRODUCT = (By.ID, 'remove-sauce-labs-backpack')
    ERROR_FIRST_NAME_MESSAGE = (By.XPATH, '//*[@class = "error-message-container error"]')
    ERROR_LAST_NAME_MESSAGE = (By.XPATH, '//*[@class="error-message-container error"]')
    ERROR_POSTAL_CODE_MESSAGE = (By.XPATH, '//*[@class="error-message-container error"]')
    CONTINUE_SHOPPING_BTN = (By.ID, 'continue-shopping')
    CANCEL_BTN = (By.ID, 'cancel')
    BACK_TO_PRODUCTS = (By.ID, 'back-to-products')


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

    def the_logo_is_displayed(self):
        try:
            logo = WebDriverWait(self.chrome, 10).until(EC.visibility_of_element_located(self.SWAG_LABS_LOGO))
            assert logo.is_displayed()
            logging.info('The logo is displayed')
        except Exception as l:
            logging.error(f"An error occurred while displaying the logo website : {str(l)}")

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

    def the_product_is_added_to_cart(self):
        try:
            added_to_cart = self.chrome.find_element(*self.SHOPPING_CART_LINK)
            added_to_cart.click()
            logging.info('The user is redirected to cart page')
        except Exception as t:
            logging.error(f'An error occurred while being redirected to the cart page : {str(t)}')

    def i_click_on_the_checkout_button(self):
        try:
            checkout_btn = self.chrome.find_element(*self.CHECKOUT_BTN)
            checkout_btn.click()
            logging.info('The user is redirecting to the details page')
        except Exception as e:
            logging.error(f'An error occurred while being redirected to the details page : {str(e)}')
    def the_first_name_is_inserted(self):
        try:
            first_name = self.chrome.find_element(*self.FIRST_NAME)
            first_name.send_keys()
            logging.info('The first name is inserted')
        except Exception as t:
            logging.error(f'An error occurred while inserting the first name : {str(t)}')

    def the_last_name_is_inserted(self):
        try:
            last_name = self.chrome.find_element(*self.LAST_NAME)
            last_name.send_keys()
            logging.info('The last name is inserted')
        except Exception as t:
            logging.error(f'An error occurred while inserting the last name : {str(t)}')

    def the_postal_code_is_inserted(self):
        try:
            postal_code = self.chrome.find_element(*self.POSTAL_CODE)
            postal_code.send_keys()
            logging.info('The postal code is inserted')
        except Exception as t:
            logging.error(f'An error occurred while inserting the postal code : {str(t)}')

    def i_click_on_the_continue_button(self):
        try:
            continue_btn = self.chrome.find_element(*self.CONTINUE_BTN)
            continue_btn.click()
            logging.info('The shopping procedure continues')
        except Exception as e:
            logging.error(f'An error occurred while clicking the continue button : {str(e)}')

    def i_click_on_the_finish_button(self):
        try:
            finish_btn = self.chrome.find_element(*self.FINISH_BTN)
            finish_btn.click()
            logging.info('The shopping procedure is finished')
        except Exception as e:
            logging.error(f'An error occurred while finishing the shopping procedure: {str(e)}')

    def the_message_order_complete_is_shown(self):
        try:
            order_complete = (WebDriverWait(self.chrome, 10).
                              until(EC.visibility_of_element_located(self.ORDER_COMPLETE_MESSAGE)))
            assert order_complete.is_displayed()
            logging.info('The order complete message is displayed')
        except Exception as l:
            logging.error(f"An error occurred while displaying the order complete message : {str(l)}")

    def i_click_on_the_back_to_products_button(self):
        try:
            back_to_products_btn = self.chrome.find_element(*self.BACK_TO_PRODUCTS)
            back_to_products_btn.click()
            logging.info('The user is redirected back to the main page')
        except Exception as e:
            logging.error(f'An error occurred while being redirected back to the main page: {str(e)}')

    def i_click_on_the_remove_product_button(self):
        try:
            remove_product_btn = self.chrome.find_element(*self.REMOVE_PRODUCT)
            remove_product_btn.click()
            logging.info('The product is removed')
        except Exception as e:
            logging.error(f'An error occurred while removing the product from cart: {str(e)}')

    def i_click_on_the_continue_shopping_button(self):
        try:
            continue_shopping_btn = self.chrome.find_element(*self.CONTINUE_SHOPPING_BTN)
            continue_shopping_btn.click()
            logging.info('The shopping procedure is continued')
        except Exception as e:
            logging.error(f'An error occurred while continuing the shopping procedure: {str(e)}')


    def i_click_on_the_cancel_button(self):
        try:
            cancel_btn = self.chrome.find_element(*self.CANCEL_BTN)
            cancel_btn.click()
            logging.info('Buying procedure is cancelled')
        except Exception as e:
            logging.error(f'An error occurred while cancelling the buying procedure {str(e)}')

    def the_message_error_first_name_is_required_is_shown(self):
        try:
            error_first_name = (WebDriverWait(self.chrome, 10).
                              until(EC.visibility_of_element_located(self.ERROR_FIRST_NAME_MESSAGE)))
            assert error_first_name.is_displayed()
            logging.info('The error message first name is required is displayed')
        except Exception as l:
            logging.error(f"An error occurred while displaying the error message first name is required : {str(l)}")

    def the_message_error_last_name_is_required_is_shown(self):
        try:
            error_last_name = (WebDriverWait(self.chrome, 10).
                              until(EC.visibility_of_element_located(self.ERROR_LAST_NAME_MESSAGE)))
            assert error_last_name.is_displayed()
            logging.info('The error message last name is required is displayed')
        except Exception as l:
            logging.error(f"An error occurred while displaying the error message last name is required : {str(l)}")

    def the_message_error_postal_code_is_required_is_shown(self):
        try:
            error_postal_code = (WebDriverWait(self.chrome, 10).
                              until(EC.visibility_of_element_located(self.ERROR_POSTAL_CODE_MESSAGE)))
            assert error_postal_code.is_displayed()
            logging.info('The error message postal code is required is displayed')
        except Exception as l:
            logging.error(f"An error occurred while displaying the error message postal code is required : {str(l)}")








