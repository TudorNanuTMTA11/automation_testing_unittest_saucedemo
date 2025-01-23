Feature: Check that the login button in the SauceDemo website is working properly and I can access my account
    @T1 @negativeTesting
      Scenario Outline: Trying to login with invalid password
      Given I am on the SauceDemo homepage and I want to initiate the login process
      When I enter username "<username>"
      When I enter password "<password>"
      When I click on login button
      Then I receive a error "<error_message>"

      Examples:
      |username     |  password     |error_message |
      |standard_user|  secret_sauce1|Epic sadface: Username and password do not match any user in this service |
      |standard_user|  secret_sauc  |Epic sadface: Username and password do not match any user in this service |

     @T2 @positiveTesting
       Scenario: I am on the SauceDemo homepage and I want to initiate the login process with valid credentials
      Given I am on the SauceDemo homepage and I want to initiate the login process
       When I enter username "standard_user"
       When I enter password "secret_sauce"
       When I click on login button
       Then I am redirected to the main page

      @T3 @negativeTesting
        Scenario: I am on the SauceDemo homepage and I want to initiate the login process with no credentials inserted
        Given I am on the SauceDemo homepage and I want to initiate the login process
        When I click on login button
        Then I receive a error "Epic sadface: Username is required"

       @T4 @negativeTesting
         Scenario: I am on the SauceDemo homepage and I want to initiate the login process with valid user and no password inserted
          When I enter username "standard_user"
          When I click on login button
          Then I receive a error "Epic sadface: Password is required"

