from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import logging
from Pages.inventory_page import Inventory_page

class Browser:
    s = Service(ChromeDriverManager().install())
    chrome = webdriver.Chrome(service=s)
    logging.basicConfig(level=logging.INFO)

    def maximise_windows(self):
        self.chrome.maximize_window()

    def close_browser(self):
        self.chrome.quit()