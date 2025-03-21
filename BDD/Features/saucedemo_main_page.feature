Feature: Check if I can use properly the website
  Background:
    Given I am logged in to the website with the username "standard_user" and password "secret_sauce"

  @T5 @positiveTesting
    Scenario: I want to sort the items from low price to high price
    When I click on the sort button
    When I click the option Price(low to high)
    Then Prices are sorted from low to high

  @T6 @positiveTesting
  Scenario: I want to sort the items from A to Z
  When I click the option Name(A to Z)
  Then Items are sorted from A to Z

  @T7 @positiveTesting
  Scenario: I want to sort the items from high price to low price
    When I click the option Price(high to low)
    Then Prices are sorted from high to low

  @T8 @positiveTesting
  Scenario: I want to sort the items from Z to A
    When I click the option Name(Z to A)
    Then Items are sorted from Z to A

  @T9 @positiveTesting
  Scenario: I want to see the website logo displayed
     Then I see the website logo displayed

  @T10 @positiveTesting
  Scenario: I want to remove sauce backpack item from cart
    When I click on the option Add to cart
    When I click the option Remove
    Then The item is removed from cart

  @T11 @positiveTesting
  Scenario: I want to buy a product from the website
    When I introduce the first and last name, "Tudor" and "Nanu"
    When I introduce the zip/postal code "810009"
    When I click on the continue button
    When I click on the finish button
    Then I click on back to products button

  @T12 @positiveTesting
  Scenario: I want to remove a product from the cart
    When I click on remove button
    When I click on the finish button
    Then I am redirected back to the main page

  @T13 @negativeTesting
  Scenario: I want to buy a product from the website but without inserting the details
    When I click on the option Add to cart
    When I click on the shopping cart icon
    When I click on checkout button
    When I click on the continue button
    Then I receive "first_name_is_required" error "Error: First Name is required"


  @T14 @negativeTesting
  Scenario: I want to buy a product from the website but only inserting the first name
    When I click on the option Add to cart
    When I click on the shopping cart icon
    When I click on checkout button
    When I introduce the first name "Tudor"
    When I click on the continue button
    Then I receive "last_name_is_required" error "Error: Last Name is required"

  @T15 @negativeTesting
  Scenario: I want to buy a product from the website but only inserting the first and last name
    When I click on the option Add to cart
    When I click on the shopping cart icon
    When I click on checkout button
    When I introduce the first and last name, "Tudor" and "Nanu"
    When I click on the continue button
    Then I receive "postal_code_is_required" error "Error: Postal Code is required"


  @T16 @positiveTesting
  Scenario: I want to click continue shopping
    Given I am logged in to the website with the username "standard_user" and password "secret_sauce"
    When I click on the shopping cart icon
    When I click on the continue shopping button


  @T17 @positiveTesting
  Scenario: I want to cancel the order
    When I click on the cancel button
    Then I am redirected to the cart page











