from behave import *

@given('I am logged in to the website')
def step_impl(context):
    context.inventory_page.open_inventory_page()
    context.inventory_page.insert_username()
    context.inventory_page.insert_password()
    context.inventory_page.main_page()

@when('I click on the sort button')
def step_impl(context):
    context.main_page.i_click_on_the_sort_button()

@when('I click the option Price(low to high)')
def step_impl(context):
    context.main_page.i_click_on_the_option_price_low_to_high()

@then('Prices are sorted from low to high')
def step_impl(context):
    context.main_page.prices_are_sorted_from_low_to_high()

@when('I click the option Price(high to low)')
def step_impl(context):
    context.main_page.i_click_on_the_option_price_high_to_low()

@then('Prices are sorted from high to low')
def step_impl(context):
    context.main_page.prices_are_sorted_from_high_to_low()

@when('I click the option Name(A to Z)')
def step_impl(context):
    context.main_page.i_click_on_the_option_name_A_to_Z()

@when('I click the option Name(Z to A)')
def step_impl(context):
    context.main_page.i_click_on_the_option_name_Z_to_A()

@when('Items are sorted from Z to A')
def step_impl(context):
    context.main_page.i_click_on_the_option_name_Z_to_A()

@when('I look on the front of the main page')
def step_impl(context):
    context.main_page.the_logo_is_displayed()

@when ('I click on the option Add to cart')
def step_impl(context):
    context.main_page.i_click_on_the_add_to_cart_button()

@when ('I click the option Remove')
def step_impl(context):
    context.main_page.i_click_on_the_remove_button()

@then ('The product is removed from cart')
def step_impl(context):
    context.main_page.the_product_is_removed_from_cart()

@when('I click on the shopping cart icon')
def step_impl(context):
    context.main_page.the_product_is_added_to_cart()

@when('I click on remove button')
def step_impl(context):
    context.main_page.i_click_on_the_remove_button()

@when('I click on checkout button')
def step_impl(context):
    context.main_page.i_click_on_the_checkout_button()

@when('I introduce the first name')
def step_impl(context):
    context.main_page.the_first_name_is_inserted()

@when('I introduce the last name')
def step_impl(context):
    context.main_page.the_last_name_is_inserted()

@when('I introduce the zip/postal code')
def step_impl(context):
    context.main_page.the_postal_code_is_inserted()

@when('I introduce only the first and last name')
def step_impl(context):
    context.main_page.the_message_error_postal_code_is_required_is_shown()


@when('I do not introduce the zip/postal code')
def step_impl(context):
    context.main_page.the_message_error_postal_code_is_required_is_shown()

@when ('I click on the continue button')
def step_impl(context):
    context.main_page.i_click_on_the_continue_button()
@when ('I click on the finish button')
def step_impl(context):
    context.main_page.i_click_on_the_finish_button()
@then ('I click on back to products button')
def step_impl(context):
    context.main_page.i_click_on_the_back_to_products_button()

@then('I am redirected back to the main page')
def step_impl(context):
    context.main_page.i_click_on_the_back_to_products_button()

@when ('I do not introduce the first name')
def step_impl(context):
    context.main_page.the_message_error_first_name_is_required_is_shown()
@when ('I do not introduce the last name')
def step_impl(context):
    context.main_page.the_message_error_last_name_is_required_is_shown()
@when ('I do not introduce the zip/postal code ')
def step_impl(context):
    context.main_page.the_message_error_postal_code_is_required_is_shown()

@when('I introduce only the first name')
def step_impl(context):
    context.main_page.the_message_error_last_name_is_required_is_shown()

@then('I receive a error')
def step_impl(context):
    context.main_page.the_message_error_first_name_is_required_is_shown()

@when('I click on the continue shopping button')
def step_impl(context):
    context.main_page.i_click_on_the_continue_shopping_button()

@when('I click on the cancel button')
def step_impl(context):
    context.main_page.i_click_on_the_cancel_button()

@then('I am redirected to the cart page')
def step_impl(context):
    context.main_page.i_click_on_the_cancel_button()

@then('Items are sorted from A to Z')
def step_impl(context):
    context.main_page.i_click_on_the_option_name_A_to_Z()

@then('Items are sorted from Z to A')
def step_impl(context):
    context.main_page.i_click_on_the_option_name_Z_to_A()

@then('I see the website logo displayed')
def step_impl(context):
    context.main_page.the_logo_is_displayed()

@then('The item is removed from cart')
def step_impl(context):
    context.main_page.the_product_is_removed_from_cart()



