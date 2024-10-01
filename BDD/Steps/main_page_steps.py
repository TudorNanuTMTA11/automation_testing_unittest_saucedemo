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

@when('Items are sorted from Z to A')
def step_impl(context):
    context.main_page.i_click_on_the_option_name_Z_to_A()

@when ('I click on the option Add to cart')
def step_impl(context):
    context.main_page.i_click_on_the_add_to_cart_button()

@when ('I click the option Remove')
def step_impl(context):
    context.main_page.i_click_on_the_remove_button()

@then ('The product is removed from cart')
def step_impl(context):
    context.main_page.the_product_is_removed_from_cart()



