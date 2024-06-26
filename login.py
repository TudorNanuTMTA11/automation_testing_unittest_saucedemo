from selenium.webdriver.common.by import By
from unittest import TestCase

from seleniumbase import Driver


class Test_Login(TestCase):
    LOGIN_USER_INPUT = (By.ID, 'user-name')
    LOGIN_PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BTN_INPUT = (By.ID, 'login-button')
    LOGIN_ERROR_MESSAGE = (By.XPATH, '//*[@class = "error-message-container error"]')
    # aici definim constantele care sa stocheze valoarea de cautare a selectorului pe care il cautam.Pentru a indica
    # ca o variabila trebuie tratata ca si constanta se folosesc majuscule in denumirea lor

    def setUp(self) -> None:  # -> None inseamna ca aceasta functie nu returneaza nimic explicit. Functiile de
        # configurare teste cum ar fi setUp si tearDown sunt adesea definite sa nu returneze nimic
        self.chrome= Driver()
        self.chrome.maximize_window()
        self.chrome.get('https://www.saucedemo.com/')

    def tearDown(self) -> None:
        self.chrome.quit()  # aceasta comanda este pentru a inchide browserul

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



    def test_sign_in_under_right_user_and_wrong_password(self):
        self.chrome.find_element(*self.LOGIN_USER_INPUT).send_keys('standard_user')
        self.chrome.find_element(*self.LOGIN_PASSWORD_INPUT).send_keys('secret')
        self.chrome.find_element(*self.LOGIN_BTN_INPUT).click()
        login_message = self.chrome.find_element(*self.LOGIN_ERROR_MESSAGE).text
        self.assertEqual(login_message, 'Epic sadface: Username and password do not match any user in this service',
                         'Error message is not correct')

    def test_sign_in_no_credentials_inserted(self):
        self.chrome.find_element(*self.LOGIN_BTN_INPUT).click()
        login_message = self.chrome.find_element(*self.LOGIN_ERROR_MESSAGE).text
        self.assertEqual(login_message, 'Epic sadface: Username is required',
                         'Error message is not correct')

    def test_sign_in_user_correct_no_password_inserted(self):
        self.chrome.find_element(*self.LOGIN_USER_INPUT).send_keys('standard_user')
        self.chrome.find_element(*self.LOGIN_BTN_INPUT).click()
        login_message = self.chrome.find_element(*self.LOGIN_ERROR_MESSAGE).text
        self.assertEqual(login_message, 'Epic sadface: Password is required',
                         'Error message is not correct')

