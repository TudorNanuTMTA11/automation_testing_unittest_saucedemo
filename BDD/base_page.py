
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import logging

from browser import Browser
from selectors_list import Selectors_List



class Base_page(Browser,Selectors_List):
       

        # metoda asta se apeleaza in login_page
        # putem sa o mai apelam ori de cate ori avem nevoie in oricare fisiere de tip pages


        def check_error_message(self,by, selector, expected_error_message):
                # metoda presence_of_element_located primeste doi parametrii: tipul selectorului si valoarea selectorului
                def check_error_message(self, by, selector, expected_error_message):
                        # metoda presence_of_element_located primeste doi parametrii: tipul selectorului si valoarea selectorului
                        error_message_web_element = WebDriverWait(self.chrome, 20).until(
                                EC.presence_of_element_located((by, selector)))
                        actual_error_message_text = error_message_web_element.text
                        assert expected_error_message == actual_error_message_text, f"Error, the message is incorrect. Expected: {expected_error_message}, actual: {actual_error_message_text}"



        def the_first_name_is_inserted(self, first_name):
                try:
                   self.chrome.find_element(*self.FIRST_NAME).send_keys(first_name)
                   logging.info('The first name is inserted')
                except Exception as t:
                        logging.error(f'An error occurred while using the first name : {str(t)}')

        def the_last_name_is_inserted(self,last_name):
                try:
                   self.chrome.find_element(*self.LAST_NAME).send_keys(last_name)
                   logging.info('The last name is inserted')
                except Exception as t:
                        logging.error(f'An error occurred while using the last name : {str(t)}')

        def the_postal_code_is_inserted(self, postal_code):
                try:
                   self.chrome.find_element(*self.POSTAL_CODE).send_keys(postal_code)
                   logging.info('The postal code is inserted')
                except Exception as t:
                        logging.error(f'An error occurred while using the postal code : {str(t)}')

        def insert_username(self, username):
                try:
                        self.chrome.find_element(*self.USER_NAME).send_keys(username)
                except Exception as i:
                        logging.error(f"An error occurred while using the username : {str(i)}")

        def click_login_button(self):
                try:
                        login_button = self.chrome.find_element(*self.LOGIN_BUTTON)
                        if login_button:
                                login_button.click()
                        else:
                                raise AssertionError('Login button element was not found')
                except Exception as i:
                        logging.error(f"An error occurred while clicking the login button : {str(i)}")

        def insert_password(self, user_password):
                try:
                        self.chrome.find_element(*self.PASSWORD).send_keys(user_password)
                except Exception as i:
                        logging.error(f"An error occurred while using the password: {str(i)}")

        def error_message_invalid_password_is_displayed(self, expected_error_message):
            self.check_error_message(*self.PASSWORD, expected_error_message)

        def error_message_invalid_username_is_displayed(self, expected_error_message):
            self.check_error_message(*self.USER_NAME, expected_error_message)


