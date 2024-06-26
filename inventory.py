from selenium.webdriver.common.by import By
from unittest import TestCase
from selenium.webdriver.support.select import Select
from seleniumbase import Driver


class Test_Inventory(TestCase):
    PRODUCT_SORT_CONTAINER = (By.XPATH, '//*[@class= "product_sort_container"]')
    INVENTORY_ITEM_PRICE = (By.XPATH, '//*[@class = "inventory_item_price"]')
    LOGIN_USER_INPUT = (By.ID, 'user-name')
    LOGIN_PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BTN_INPUT = (By.ID, 'login-button')
    ADD_TO_CART_BTN = (By.XPATH, '//button[contains(text(),"Add to cart")]')
    INVENTORY_ITEM_NAME = (By.XPATH, '//*[@class = "inventory_item_name"]')
    SHOPPING_CART_CONTAINER_SAUCE_LABS_BACKPACK = (By.XPATH, '//*[@class = "shopping_cart_container"]')
    SHOPPING_CART_LINK = (By.CLASS_NAME, 'shopping_cart_link')
    REMOVE_SAUCE_LABS_BACKPACK_BTN_INPUT = (By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button')
    SWAG_LABS_LOGO = (By.XPATH,'//*[@class = "app_logo"]')
    CHECKOUT_BTN = (By.ID,'checkout')
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
    CANCEL_BTN = (By.ID,'cancel')
    BACK_TO_PRODUCTS = (By.ID, 'back-to-products')



    def setUp(self) -> None:  # -> None inseamna ca aceasta functie nu returneaza nimic explicit. Functiile de
        # configurare teste cum ar fi setUp si tearDown sunt adesea definite sa nu returneze nimic
        self.chrome = Driver()
        self.chrome.maximize_window()
        self.chrome.get('https://www.saucedemo.com/inventory.html')
        self.chrome.find_element(*self.LOGIN_USER_INPUT).send_keys('standard_user')
        self.chrome.find_element(*self.LOGIN_PASSWORD_INPUT).send_keys('secret_sauce')
        self.chrome.find_element(*self.LOGIN_BTN_INPUT).click()

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_items_sorted_after_price_low_to_high(self):
        product_sort_container = Select(self.chrome.find_element(*self.PRODUCT_SORT_CONTAINER))
        product_sort_container.select_by_visible_text('Price (low to high)')
        product_price_list = self.chrome.find_elements(*self.INVENTORY_ITEM_PRICE)
        in_product_price_list_sorted = True
        for i in range(len(product_price_list) - 1):
            if float(product_price_list[i].text.replace("$", "")) > float(
                    product_price_list[i + 1].text.replace("$", "")):
                in_product_price_list_sorted = False
        assert in_product_price_list_sorted == True

    def test_items_sorted_after_price_high_to_low(self):
        product_sort_container = Select(self.chrome.find_element(*self.PRODUCT_SORT_CONTAINER))
        product_sort_container.select_by_visible_text('Price (high to low)')
        product_price_list = self.chrome.find_elements(*self.INVENTORY_ITEM_PRICE)
        in_product_price_list_sorted = True
        for i in range(len(product_price_list) - 1):
            if float(product_price_list[i + 1].text.replace("$", "")) < float(
                    product_price_list[i].text.replace("$", "")):
                in_product_price_list_sorted = True
        assert in_product_price_list_sorted == True

    def test_items_sorted_after_name_A_to_Z(self):
        product_sort_container = Select(self.chrome.find_element(*self.PRODUCT_SORT_CONTAINER))
        product_sort_container.select_by_visible_text('Name (A to Z)')
        product_name_list = self.chrome.find_elements(*self.INVENTORY_ITEM_NAME)
        in_product_name_list_sorted = True
        for i in range(len(product_name_list) - 1):
            if str(product_name_list[i]) > str(product_name_list[i + 1]):
                in_product_name_list_sorted = False
        assert in_product_name_list_sorted == True

    def test_items_sorted_after_name_Z_to_A(self):
        product_sort_container = Select(self.chrome.find_element(*self.PRODUCT_SORT_CONTAINER))
        product_sort_container.select_by_visible_text('Name (Z to A)')
        product_name_list = self.chrome.find_elements(*self.INVENTORY_ITEM_NAME)
        in_product_name_list_sorted = True
        for i in range(len(product_name_list) - 1):
            if str(product_name_list[i + 1]) < str(product_name_list[i]):
                in_product_name_list_sorted = True
        assert in_product_name_list_sorted == True

    def test_click_remove_sauce_labs_backpack(self):
            self.chrome.find_element(*self.REMOVE_SAUCE_LABS_BACKPACK_BTN_INPUT).click()

    def test_swag_labs_logo_is_displayed(self):
            app_logo = self.chrome.find_element(*self.SWAG_LABS_LOGO).text
            self.assertEqual(app_logo, 'Swag Labs', 'The logo shown is incorrect')

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

    def test_remove_product_from_cart(self):
        self.chrome.find_elements(*self.ADD_TO_CART_BTN)[0].click()
        self.chrome.find_element(*self.SHOPPING_CART_LINK).click()
        self.chrome.find_element(*self.REMOVE_PRODUCT).click()
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
        self.assertEqual(expected_url, actual_url)
        self.assertEqual(expected_message, actual_message)

    def test_click_add_product_to_cart_and_no_details_inserted(self):
        self.chrome.find_elements(*self.ADD_TO_CART_BTN)[0].click()
        self.chrome.find_element(*self.SHOPPING_CART_LINK).click()
        self.chrome.find_element(*self.CHECKOUT_BTN).click()
        self.chrome.find_element(*self.CONTINUE_BTN).click()
        error_first_name_message = self.chrome.find_element(*self.ERROR_FIRST_NAME_MESSAGE).text
        self.assertEqual(error_first_name_message, 'Error: First Name is required',
                         'Error message is not correct')

    def test_click_add_product_to_cart_but_only_first_name_inserted(self):
        self.chrome.find_elements(*self.ADD_TO_CART_BTN)[0].click()
        self.chrome.find_element(*self.SHOPPING_CART_LINK).click()
        self.chrome.find_element(*self.CHECKOUT_BTN).click()
        self.chrome.find_element(*self.FIRST_NAME).send_keys('Tudor')
        self.chrome.find_element(*self.CONTINUE_BTN).click()
        error_last_name_message = self.chrome.find_element(*self.ERROR_LAST_NAME_MESSAGE).text
        self.assertEqual(error_last_name_message, 'Error: Last Name is required',
                         'Error message is not correct')

    def test_click_add_product_but_no_postal_code_inserted(self):
        self.chrome.find_elements(*self.ADD_TO_CART_BTN)[0].click()
        self.chrome.find_element(*self.SHOPPING_CART_LINK).click()
        self.chrome.find_element(*self.CHECKOUT_BTN).click()
        self.chrome.find_element(*self.FIRST_NAME).send_keys('Tudor')
        self.chrome.find_element(*self.LAST_NAME).send_keys('Nanu')
        self.chrome.find_element(*self.CONTINUE_BTN).click()
        error_postal_code_message = self.chrome.find_element(*self.ERROR_POSTAL_CODE_MESSAGE).text
        self.assertEqual(error_postal_code_message, 'Error: Postal Code is required',
                         'Error message is not correct')

    def test_click_continue_shopping(self):
        self.chrome.find_elements(*self.ADD_TO_CART_BTN)[0].click()
        self.chrome.find_element(*self.SHOPPING_CART_LINK).click()
        self.chrome.find_element(*self.CONTINUE_SHOPPING_BTN).click()
        expected_url = 'https://www.saucedemo.com/inventory.html'
        actual_url = self.chrome.current_url
        self.assertEqual(expected_url,actual_url)

    def test_click_cancel_add_product_to_cart(self):
        self.chrome.find_elements(*self.ADD_TO_CART_BTN)[0].click()
        self.chrome.find_element(*self.SHOPPING_CART_LINK).click()
        self.chrome.find_element(*self.CHECKOUT_BTN).click()
        self.chrome.find_element(*self.CANCEL_BTN).click()
        expected_url = 'https://www.saucedemo.com/cart.html'
        actual_url = self.chrome.current_url
        self.assertEqual(expected_url,actual_url)











