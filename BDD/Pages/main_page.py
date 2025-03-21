

import logging

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base_page import Base_page


class Main_page(Base_page):

    def error_message_first_name_is_displayed(self, expected_error_message):
        self.check_error_message(*self.ERROR_MESSAGE, expected_error_message)

    def error_message_last_name_is_displayed(self, expected_error_message):
        self.check_error_message(*self.ERROR_MESSAGE, expected_error_message)

    def error_message_postal_code_is_displayed(self, expected_error_message):
        self.check_error_message(*self.ERROR_MESSAGE, expected_error_message)

    def i_click_on_the_sort_button(self):
        try:
            self.chrome.find_element(*self.PRODUCT_SORT_CONTAINER).click()
            logging.info('The sorting options were successfully shown on the tab')
        except Exception as e:
            logging.error(f'An error occurred while showing the sort options : {str(e)}')

    def i_click_on_the_option_price_low_to_high(self):
        try:
            self.chrome.find_element(*self.INVENTORY_ITEM_PRICE).click()
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
            self.chrome.find_element(*self.INVENTORY_ITEM_PRICE).click()
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
            self.chrome.find_element(*self.INVENTORY_ITEM_NAME).click()
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
            self.chrome.find_element(*self.INVENTORY_ITEM_NAME).click()
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
            self.chrome.find_element(*self.ADD_TO_CART_BTN).click()
            logging.info('The item was added to cart')
        except Exception as e:
            logging.error(f'An error occurred while adding the item to cart : {str(e)}')

    def i_click_on_the_remove_button(self):
        try:
            self.chrome.find_element(*self.REMOVE_SAUCE_LABS_BACKPACK_BTN_INPUT).click()
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
            self.chrome.find_element(*self.SHOPPING_CART_CONTAINER).click()
            logging.info('The user is redirected to cart page')
        except Exception as t:
            logging.error(f'An error occurred while being redirected to the cart page : {str(t)}')

    def i_click_on_the_checkout_button(self):
        try:
            self.chrome.find_element(*self.CHECKOUT_BTN).click()
            logging.info('The user is redirecting to the details page')
        except Exception as e:
            logging.error(f'An error occurred while being redirected to the details page : {str(e)}')

    def i_click_on_the_continue_button(self):
        try:
            self.chrome.find_element(*self.CONTINUE_BTN).click()
            logging.info('The shopping procedure continues')
        except Exception as e:
            logging.error(f'An error occurred while clicking the continue button : {str(e)}')

    def i_click_on_the_finish_button(self):
        try:
            self.chrome.find_element(*self.FINISH_BTN).click()
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
            self.chrome.find_element(*self.BACK_TO_PRODUCTS).click()
            logging.info('The user is redirected back to the main page')
        except Exception as e:
            logging.error(f'An error occurred while being redirected back to the main page: {str(e)}')

    def i_click_on_the_remove_product_button(self):
        try:
            self.chrome.find_element(*self.REMOVE_PRODUCT).click()
            logging.info('The product is removed')
        except Exception as e:
            logging.error(f'An error occurred while removing the product from cart: {str(e)}')

    def i_click_on_the_continue_shopping_button(self):
        try:
            self.chrome.find_element(*self.CONTINUE_SHOPPING_BTN).click()
            logging.info('The shopping procedure is continued')
        except Exception as e:
            logging.error(f'An error occurred while continuing the shopping procedure: {str(e)}')

    def i_click_on_the_cancel_button(self):
        try:
            self.chrome.find_element(*self.CANCEL_BTN).click()
            logging.info('Buying procedure is cancelled')
        except Exception as e:
            logging.error(f'An error occurred while cancelling the buying procedure {str(e)}')

