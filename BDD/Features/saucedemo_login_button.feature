Feature: Check that the login button in the SauceDemo website is working properly and I can access my account
    @T1 @negativeTesting
      Scenario Outline: Trying to login with invalid password
      Given I am on the SauceDemo homepage and I want to initiate the login process with invalid password
      When I enter username "<username>"
      When I enter password "<password>"
      When I click on login button
      Then I receive an error

      Examples:
      |username     |  password     |error_message |
      |standard_user|  secret_sauce1|Epic sadface: Username and password do not match any user in this service |
      |standard_user|  secret_sauc  |Epic sadface: Username and password do not match any user in this service |

     @T2 @positiveTesting
       Scenario: I am on the SauceDemo homepage and I want to initiate the login process with valid credentials
       When I enter my valid username
       When I enter my valid password
       When I click on login button
       Then I am redirected to the main page

      @T3 @negativeTesting
        Scenario: I am on the SauceDemo homepage and I want to initiate the login process with no credentials inserted
        When I do not enter username "<username>"
        When I do not enter password "<password>"
        When I click on login button
        Then I receive an error

       @T4 @negativeTesting
         Scenario: I am on the SauceDemo homepage and I want to initiate the login process with valid user and no password inserted
         When I enter my valid username
         When I do not enter password "<password>"
         When I click on login button
         Then I receive an error
