Feature: Check if I can use properly the website
  @T5 @positiveTesting
    Scenario: I want to sort the items from low price to high price
    Given I am logged in to the website
    When I click on the sort button
    When I click the option Price(low to high)
    Then Prices are sorted from low to high

    @T6 @positiveTesting
    Scenario: I want to sort the items from A to Z
    Given I am logged in to the website
    When I click on the sort button
    When I click the option Name(A to Z)
    Then Items are sorted from A to Z

     @T7 @positiveTesting
    Scenario: I want to sort the items from high price to low price
    Given I am logged in to the website
    When I click on the sort button
    When I click the option Price(high to low)
    Then Prices are sorted from high to low

     @T8 @positiveTesting
    Scenario: I want to sort the items from Z to A
    Given I am logged in to the website
    When I click on the sort button
    When I click the option Name(Z to A)
    Then Items are sorted from Z to A

     @T9 @positiveTesting
    Scenario: I want to remove sauce backpack item from cart
    Given I am logged in to the website
    When I click on the option Add to cart
    When I click the option Remove
    Then The item is removed from cart

     @T10 @positiveTesting
    Scenario: I want to buy a product from the website
        Given I am logged in to the website
        When I click on the option Add to cart
        When I click on the shopping cart icon
        When I click on checkout button
        When I introduce the details
       When I click on the continue button
        When I click on the finish button
        Then I click on back to products button

     @T11 @positiveTesting
    Scenario: I want to remove a product from the cart
        Given I am logged in to the website
        When I click on the option Add to cart
        When I click on the shopping cart icon
       When I click on remove button
        When I click on checkout button
        When I introduce the details
        When I click on the continue button
        When I click on the finish button
        Then I am redirected back to the main page

      @T12 @negativeTesting
    Scenario: I want to buy a product from the website but without inserting the details
        Given I am logged in to the website
        When I click on the option Add to cart
        When I click on the shopping cart icon
        When I click on checkout button
        When I do not introduce the details
        When I click on the continue button
        Then I receive a error

     @T13 @negativeTesting
    Scenario: I want to buy a product from the website but only inserting the first name
        Given I am logged in to the website
        When I click on the option Add to cart
        When I click on the shopping cart icon
        When I click on checkout button
        When I introduce only the first name
        When I click on the continue button
        Then I receive a error

       @T14 @negativeTesting
    Scenario: I want to buy a product from the website but only inserting the first and last name
        Given I am logged in to the website
        When I click on the option Add to cart
        When I click on the shopping cart icon
        When I click on checkout button
        When I introduce only the first and last name
        When I click on the continue button
        Then I receive a error

        @T15 @positiveTesting
       Scenario: I want to click continue shopping
          Given I am logged in to the website
          When I click on the option Add to cart
          When I click on the shopping cart icon
          When I click on the continue shopping button
          Then I am redirected to the main page

           @T16 @positiveTesting
       Scenario: I want to cancel the order
          Given I am logged in to the website
          When I click on the option Add to cart
          When I click on the shopping cart icon
          When I click on the cancel button
          Then I am redirected to the cart page











