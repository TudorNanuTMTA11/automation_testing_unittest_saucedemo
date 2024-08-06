# Section 1: Packages to be installed

## Introduction

Python language is linked with Selenium WebDriver. Selenium package is used for automated interaction with web browsers from Python.

There are some browsers or drivers which are suported such as Firefox, Chrome and Edge as same as Remote protocol.Furthermore, supported Python version Python are 3.8

## Installation

Packages installation are made with the help of pip utilitary , which comes at package with installation of python package , with the condition that at the installing to be ticked its addition at the environment variable).

As additional note, for creating isolated and secured Python environments, take in consideration using virtualenv.


### Selenium

For interaction with web elements it will be necessary installation of selenium library. This can be done by using the command  **pip install -U selenium**. 

### Driver
For interacting with the browser , Selenium needs a driver which will be instantiated through Driver class , available in seleniumbase library. 

The driver will be specified through sending its name as argument of the Driver class constructor , if it is not specified it will be sent the name of the implicit browser from the system where the code is run.
Seleniumbase library from where Driver class is imported can be installed by using the command  **pip install selenimbase**.


### Unittest library

It is a predefined library in python, so it is not necessary to be installed anything else to be used,only to import it through the command **import unittest**

###  html-testRunner package

HtmlTest runner is a utilitary for executing the tests which save the results in html files with the objective of the presenting of the results in a easy-readable way scopul.

For using the package it is necessary of:
- installation: pip install html-testRunner
- import: import HtmlTestRunner
  
## Project cloning and running

For c;oning we can use the command  **git clone TudorNanuTMTA11/automation_testing_unittest_saucedemo**

For executing the test we can run the file suita_teste.py or we can run tests individually from the appropiate file through clicking the green button located in the left side of the test. 


# Section 2: Project structure

 The project is composed of the following structure:

- root named "automation_testing_unittest_saucedemo
- directory numit "reports" containing all the execution reports generated through running which have the following naming convention: Test Results_yyyy-mm-dd_hh-mm-ss.html
- inventory.py -> test file covering the validation of the inventory page
- login.py -> test file covering the validation of the login page
- suita_teste.py -> test automation suite containing references to all the tests that were created

# Section 3 : Automation testing project objectives

Automation testing project has as foundation the site "https://www.saucedemo.com/", with the logo "SwagLabs".

The objectives are testing the login functionality which is performed with the help of positive testing, negative testing and functional testing.

Furthermore, testing of the inventory functionality, was done through positive testing, negative testing and functional testing.

Also, the purpose of the project was designing a test suite and generating a html-type execution report, with the scope of presenting and interpreting the results. 

# Section 4 : Deadlines 

The accepted deadline for finalising all the testing for the website in scope was 15.08.2024.
Until then, all testing must be performed, all reports must be generated.
The scope of this project was purely an automation one, and no defect management activities were done. For defect identification I created a separate manual testing project which covers this type of testing activities. 


# Section 5: Description of the tests that were performed + testing types and techniques used 

All the tests that were performed that were created in the unittest framework using positive testing, negative testing and functional testing.

All the tests that were created were passed during the test execution phase.
 
