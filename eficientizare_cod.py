import unittest

from selenium.webdriver.common.by import By
from unittest import TestCase
from selenium.webdriver.support.select import Select
from seleniumbase import Driver


class Test_SauceDemo(TestCase):
    LOGIN_USER_INPUT = (By.ID, 'user-name')
    LOGIN_PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BTN_INPUT = (By.ID, 'login-button')
    LOGIN_ERROR_MESSAGE = (By.XPATH, '//*[@class = "error-message-container error"]')
    PRODUCT_SORT_CONTAINER = (By.XPATH, '//*[@class= "product_sort_container"]')
    INVENTORY_ITEM_PRICE = (By.XPATH, '//*[@class = "inventory_item_price"]')
    LOGIN_USER_INPUT = (By.ID, 'user-name')
    LOGIN_PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BTN_INPUT = (By.ID, 'login-button')
    ADD_TO_CART_BTN = (By.XPATH, '//button[contains(text(),"Add to cart")]')
    INVENTORY_ITEM_NAME = (By.XPATH, '//*[@class = "inventory_item_name"]')
    SHOPPING_CART_CONTAINER_SAUCE_LABS_BACKPACK = (By.XPATH, '//*[@class = "shopping_cart_container"]')
    SHOPPING_CART_LINK = (By.CLASS_NAME, 'shopping_cart_link')
    REMOVE_SAUCE_LABS_BACKPACK_BTN_INPUT = (
    By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button')
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


    def setUp(self) -> None:  # -> None inseamna ca aceasta functie nu returneaza nimic explicit. Functiile de
        # configurare teste cum ar fi setUp si tearDown sunt adesea definite sa nu returneze nimic
        self.chrome= Driver()
        self.chrome.maximize_window()
        self.chrome.get('https://www.saucedemo.com/')

    def tearDown(self) -> None:
        self.chrome.quit()  # aceasta comanda este pentru a inchide browserul

    @unittest.skip
    def test_sign_in_under_valid_credentials(self):
        self.chrome.find_element(*self.LOGIN_USER_INPUT).send_keys('standard_user')
        self.chrome.find_element(*self.LOGIN_PASSWORD_INPUT).send_keys('secret_sauce')
        self.chrome.find_element(*self.LOGIN_BTN_INPUT).click()
        is_login_button_displayed = False
        try:
            self.chrome.find_element(*self.LOGIN_BTN_INPUT)
            is_login_button_displayed = True
        except:
            pass
        assert is_login_button_displayed == False, "The login was not successful"

    @unittest.skip
    def test_sign_in_no_credentials_inserted(self):
        self.chrome.find_element(*self.LOGIN_BTN_INPUT).click()
        login_message = self.chrome.find_element(*self.LOGIN_ERROR_MESSAGE).text
        self.assertEqual(login_message, 'Epic sadface: Username is required',
                         'Error message is not correct')

    @unittest.skip
    def test_sign_in_user_correct_no_password_inserted(self):
        self.chrome.find_element(*self.LOGIN_USER_INPUT).send_keys('standard_user')
        self.chrome.find_element(*self.LOGIN_BTN_INPUT).click()
        login_message = self.chrome.find_element(*self.LOGIN_ERROR_MESSAGE).text
        self.assertEqual(login_message, 'Epic sadface: Password is required',
                         'Error message is not correct')
    @unittest.skip
    def test_items_sorted(self):
        product_sort_container = Select(self.chrome.find_element(*self.PRODUCT_SORT_CONTAINER))
        product_sort_container.select_by_visible_text('Price (low to high)')
        product_price_list = self.chrome.find_elements(*self.INVENTORY_ITEM_PRICE)
        in_product_price_list_sorted = True
        for i in range(len(product_price_list) - 1):
            if float(product_price_list[i].text.replace("$", "")) > float(
                    product_price_list[i + 1].text.replace("$", "")):
                in_product_price_list_sorted = False
        assert in_product_price_list_sorted == True

    @unittest.skip
    def test_click_continue_shopping(self):
        self.chrome.find_elements(*self.ADD_TO_CART_BTN)[0].click()
        self.chrome.find_element(*self.SHOPPING_CART_LINK).click()
        self.chrome.find_element(*self.CONTINUE_SHOPPING_BTN).click()
        expected_url = 'https://www.saucedemo.com/inventory.html'
        actual_url = self.chrome.current_url
        self.assertEqual(expected_url,actual_url)

    @unittest.skip
    def test_swag_labs_logo_is_displayed(self):
        app_logo = self.chrome.find_element(*self.SWAG_LABS_LOGO).text
        self.assertEqual(app_logo, 'Swag Labs', 'The logo shown is incorrect')

    @unittest.skip
    def test_click_add_product_to_cart(self):
        self.chrome.find_elements(*self.ADD_TO_CART_BTN)[0].click()
        self.chrome.find_element(*self.SHOPPING_CART_LINK).click()
        self.chrome.find_element(*self.CHECKOUT_BTN).click()
        self.chrome.find_element(*self.FIRST_NAME).send_keys('Tudor')
        self.chrome.find_element(*self.LAST_NAME).send_keys('Nanu')
        self.chrome.find_element(*self.POSTAL_CODE).send_keys('810009')
        self.chrome.find_element(*self.CONTINUE_BTN).click()
        self.chrome.find_element(*self.FINISH_BTN).click()
        expected_url = 'https://www.saucedemo.com/checkout-complete.html'
        actual_url = self.chrome.current_url
        expected_message = 'Thank you for your order!'
        actual_message = self.chrome.find_element(*self.ORDER_COMPLETE_MESSAGE).text
        self.assertEqual(expected_url,actual_url)
        self.assertEqual(expected_message,actual_message)
        self.chrome.find_element(*self.BACK_TO_PRODUCTS).click()

    @unittest.skip
    def test_click_cancel_add_product_to_cart(self):
        self.chrome.find_elements(*self.ADD_TO_CART_BTN)[0].click()
        self.chrome.find_element(*self.SHOPPING_CART_LINK).click()
        self.chrome.find_element(*self.CHECKOUT_BTN).click()
        self.chrome.find_element(*self.CANCEL_BTN).click()
        expected_url = 'https://www.saucedemo.com/cart.html'
        actual_url = self.chrome.current_url
        self.assertEqual(expected_url,actual_url)

    @unittest.skip
    def test_click_add_product_to_cart_and_no_details_inserted(self):
        self.chrome.find_elements(*self.ADD_TO_CART_BTN)[0].click()
        self.chrome.find_element(*self.SHOPPING_CART_LINK).click()
        self.chrome.find_element(*self.CHECKOUT_BTN).click()
        self.chrome.find_element(*self.CONTINUE_BTN).click()
        error_first_name_message = self.chrome.find_element(*self.ERROR_FIRST_NAME_MESSAGE).text
        self.assertEqual(error_first_name_message, 'Error: First Name is required',
                         'Error message is not correct')

