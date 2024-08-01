from selenium.webdriver.common.by import By
from unittest import TestCase
from selenium.webdriver.support.select import Select
from seleniumbase import Driver

class Shopping(TestCase):
    SHOPPING_CART_LINK = (By.CLASS_NAME, 'shopping_cart_link')
    CHECKOUT_BTN = (By.ID, 'checkout')
    ADD_TO_CART_BTN = (By.XPATH, '//button[contains(text(),"Add to cart")]')
    REMOVE_SAUCE_LABS_BACKPACK_BTN_INPUT = (By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button')
    SWAG_LABS_LOGO = (By.XPATH, '//*[@class = "app_logo"]')
    PRODUCT_SORT_CONTAINER = (By.XPATH, '//*[@class= "product_sort_container"]')
    INVENTORY_ITEM_PRICE = (By.XPATH, '//*[@class = "inventory_item_price"]')

    def setUp(self) -> None:  # -> None inseamna ca aceasta functie nu returneaza nimic explicit. Functiile de
        # configurare teste cum ar fi setUp si tearDown sunt adesea definite sa nu returneze nimic
        self.chrome = Driver()
        self.chrome.maximize_window()
        self.chrome.get('https://www.saucedemo.com/')

    def tearDown(self) -> None:
        self.chrome.quit()  # aceasta comanda este pentru a inchide browserul

    def test_buying_and_removing_product(self):
              self.chrome.find_elements(*self.ADD_TO_CART_BTN)[0].click()
              self.chrome.find_element(*self.SHOPPING_CART_LINK).click()
              self.chrome.find_element(*self.CHECKOUT_BTN).click()

    def test_click_remove_sauce_labs_backpack(self):
            self.chrome.find_element(*self.REMOVE_SAUCE_LABS_BACKPACK_BTN_INPUT).click()

    def test_swag_labs_logo_is_displayed(self):
            app_logo = self.chrome.find_element(*self.SWAG_LABS_LOGO).text
            self.assertEqual(app_logo, 'Swag Labs', 'The logo shown is incorrect')

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


