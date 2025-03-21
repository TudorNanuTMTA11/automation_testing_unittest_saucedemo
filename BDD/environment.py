from base_page import Base_page
from browser import Browser
from Pages.login_page import Login_page
from Pages.main_page import Main_page
def before_all(context):
    context.browser = Browser()
    context.browser.maximise_windows()
    context.login_page = Login_page()
    context.main_page = Main_page()
    context.base_page = Base_page()

def after_all(context):
    context.browser.close_browser()