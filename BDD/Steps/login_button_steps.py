from behave import *

@given('I am on the SauceDemo homepage and I want to initiate the login process with invalid password')
def step_impl(context):
    context.inventory_page.open_inventory_page()

@when('I enter username {username}')
def step_impl(context,username):
    context.inventory_page.insert_username(username)

@when('I enter password "{user_password}"')
def step_impl(context, user_password):
    context.inventory_page.insert_invalid_password(user_password)

@when('I click on login button')
def step_impl(context):
    context.inventory_page.click_login_button()

@then('I receive an error')
def step_impl(context):
    context.inventory_page.login_failed()

@when('I enter my valid username')
def step_impl(context):
    context.inventory_page.insert_username()

@when('I enter my valid password')
def step_impl(context):
    context.inventory_page.insert_password()

@then('I am redirected to the main page')
def step_impl(context):
    context.inventory_page.main_page()

@when('I do not enter username {username}')
def step_impl(context,username):
    context.inventory_page.insert_username(username)

@when('I do not enter password "{user_password}"')
def step_impl(context, user_password):
    context.inventory_page.insert_invalid_password(user_password)

