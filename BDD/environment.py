from BDD.browser import Browser

def before_all(context):
    context.browser = Browser()
    context.browser.maximise_windows()

def after_all(context):
    context.browser = Browser()
    context.browser.close_browser()