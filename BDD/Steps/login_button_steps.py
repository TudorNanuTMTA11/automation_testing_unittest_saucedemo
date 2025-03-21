

from behave import *


@given('I am on the SauceDemo homepage and I want to initiate the login process')
def step_impl(context):
    context.login_page.open_login_page()


@when('I enter username "{username}"')
def step_impl(context, username):
    context.login_page.insert_username(username)


@when('I enter password "{user_password}"')
def step_impl(context, user_password):
    context.login_page.insert_password(user_password)


@when('I click on login button')
def step_impl(context):
    context.login_page.click_login_button()


@then('I am redirected to the main page')
def step_impl(context):
    context.login_page.main_page()


@then('I receive "{error_type}" error "{error_message}"')
def step_impl(context, error_type, error_message):
    if error_type == "invalid_password":
        context.login_page.error_message_invalid_password_is_displayed(error_message)
    elif error_type == "invalid_username":
        context.login_page.error_message_invalid_username_is_displayed(error_message)
    elif error_type == "first_name_is_required":
        context.main_page.error_message_first_name_is_displayed(error_message)
    elif error_type == "last_name_is_required":
        context.main_page.error_message_last_name_is_displayed(error_message)
    elif error_type == "postal_code_is_required":
        context.main_page.error_message_postal_code_is_displayed(error_message)
    else:
         "Error: Unknown error has required"













