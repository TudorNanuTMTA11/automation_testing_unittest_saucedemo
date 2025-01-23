from browser import Browser
from Pages.inventory_page import Inventory_page
from Pages.main_page import Main_page
def before_all(context):
    context.browser = Browser()
    context.browser.maximise_windows()
    context.inventory_page = Inventory_page()
    context.main_page = Main_page()

def after_all(context):
    context.browser.close_browser()