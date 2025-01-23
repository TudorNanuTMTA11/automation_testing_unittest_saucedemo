 # Section 1: Packages to be installed

 ## Introduction

 BDD framework is linked with GHERKIN language. In Python, Gherkin is implemented with help of behave library.
 There are some browsers or drivers which are suported such as Firefox, Chrome and Edge .Furthermore, supported Python version is 3.12.

 ## Installation

 To install BDD framework, it has to be created a text file called behave.ini, where it is necessary to install Ini plugin which support .ini files. Package to be installed is behave-html-formatter. After that, it will be opened files which are renamed as .feature. Then it is installed Gherkin plugin which allows the files to become Cucumber files.

 ### Ini plugin

 Provides ".ini" files support. The following features are available:
Syntax highlighting, formatting, code folding, and viewing structure for .ini files
Detection of duplicate properties and sections
The ability to navigate to a property via the Go to Symbol action

### Behave-html-formatter package

It can be installed by using the command pip install behave-html-formatter or by install it from packages. Then, in behave.ini file write  the sequence [behave.formatters]
html=behave_html_formatter:HTMLFormatter

### Gherkin language
Adds support for the Gherkin language, which is used by the Cucumber testing tool.
Provides coding assistance for step definitions

## Selenium
For interaction with web elements it will be necessary installation of selenium library. This can be done by using the command pip install -U selenium.

## Driver
For interacting with the browser , Selenium needs a driver which will be instantiated through Driver class , available in seleniumbase library.

The driver will be specified through sending its name as argument of the Driver class constructor , if it is not specified it will be sent the name of the implicit browser from the system where the code is run. Seleniumbase library from where Driver class is imported can be installed by using the command pip install seleniumbase.

## Project cloning and running
For cloning we can use the command git clone TudorNanuTMTA11/automation_testing_unittest_saucedemo

For executing the tests we can write in console behave -f html -o test-report.html for all tests or for a single test write behave -f html -o test-report.html followed by --tags=@T1 for example

# Section 2: Project structure
The project is composed of the following structure:

root named "automation_testing_unittest_saucedemo

directory named "BDD"

directory named "Features"

directory named "Pages"

directory named "Steps"

saucedemo_login_button.feature.py -> test file contains feature, tests which are structured as: scenario outline/scenario, given, when, then

for login into the website function

saucedemo_main_page.feature.py -> test file contains feature, tests which are structured as: scenario outline/scenario, given, when, then

for realising different purchases

inventory_page.py -> contains methods and functions which are used for allowing the tests for accesing the website to work and a class 

which contains the speciffic selectors

main_page.py -> contains methods and functions which are used for allowing the tests for purchasing items to work and a class which 

contains the speciffic selectors

login_button_steps.py -> contains the steps which are defined in features designed for accesing the website and then for generate the 

test report in html format

main_page_steps.py -> contains the steps which are defined in features designed for using the website principal page and then for 

generate the test report in html format

behave.ini -> file for enabling Ini plugin

browser.py -> file for accessing the browser

environment.py -> file for designing the framework

test-report.html -> file for accesing the report in browser

# Section 3 : Automation testing project objectives
Automation testing project has as foundation the site "https://www.saucedemo.com/", with the logo "SwagLabs".

The objectives are testing the login functionality which is performed with the help of positive testing, negative testing and functional 

testing.

Furthermore, testing of the inventory functionality, was done through positive testing, negative testing and functional testing.

Also, the purpose of the project was creating .py files and generating a html-type execution report, with the scope of presenting and 

interpreting the results.

# Section 4 : Deadlines
The accepted deadline for finalising all the testing for the website in scope was 15.09.2024. Until then, all testing must be performed, 

all reports must be generated. The scope of this project was purely an automation one, and no defect management activities were done. 

For defect identification I created a separate manual testing project which covers this type of testing activities.

# Section 5: Description of the tests that were performed + testing types and techniques used

All the tests that were performed that were created in the unittest framework using positive testing, negative testing and functional 

testing.

All the tests that were created were passed during the test execution phase.



