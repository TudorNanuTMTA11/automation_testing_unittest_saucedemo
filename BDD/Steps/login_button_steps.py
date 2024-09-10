from behave import *

@given("I am on SauceDemo homepage and I want to initiate the login process with invalid password")
def step_impl(context):
    context.inventory_page.open_inventory_page()

@when("I click on username button")
def step_impl(context):
    context.inventory_page.insert_username()

@when("I enter my invalid '{user_password}'")
def step_impl(context, user_password):
    context.inventory_page.insert_invalid_password(user_password)

@when("I click on login button")
def step_impl(context):
    context.inventory_page.click_login_button()

@then("I receive an '{error_message}'")
def step_impl(context, error_message):
    context.inventory_page.login_failed(error_message)
