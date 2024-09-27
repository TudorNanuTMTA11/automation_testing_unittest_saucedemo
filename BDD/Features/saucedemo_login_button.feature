Feature: Check that the login button in the SauceDemo website is working properly and I can access my account
    @T1 @negativeTesting
      Scenario Outline: Trying to login with invalid password
      Given I am on the SauceDemo homepage and I want to initiate the login process with invalid password
      When I enter my valid username
      When I enter my invalid "<password>"
      When I click on login button
      Then I receive an error

      Examples:
        |password  |error_message|
        |secret_sauce1|Epic sadface: Username and password do not match any user in this service|
        |secret_sauc  |Epic sadface: Username and password do not match any user in this service|

     @T2 @positiveTesting
       Scenario: I am on the SauceDemo homepage and I want to initiate the login process with valid credentials
       When I enter my valid username
       When I enter my valid password
       When I click on login button
       Then I am redirected to the main page