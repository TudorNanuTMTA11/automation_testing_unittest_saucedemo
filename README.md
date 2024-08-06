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

For running the project it can be runned the file  suita_teste.py ,in this way all the tests are runned or it can be runned a individual test from the appropiate file through clicking the green button located in the left side of the test. 


# Section 2: Project structure

<p> The project ,which has the name "ProiectFinal is composed of:</p>

<p> Directory named "ProiectFinal"</p>

<p> Directory numit "reports"</p>

<p> In the structure of the directory "reports" there is the html file "Test Results_2024-06-24_14-38-05.html</p>

<p> Python file"___init__.py"</p>

<p> Python file "inventory.py"</p>

<p>  Python file "login.py"</p>

<p>  Python file "suita_teste.py"</p>

# Section 3 : Automation testing project objectives

<p>Automation testing project has as foundation the site "https://www.saucedemo.com/", with the logo "SwagLabs".</p>

<p> The objectives are testing the login functionality which is realised with help of the positive testing, translated in login with valid credentials testing  </p>

<p> Furthermore, testing of inventory functionality, realised through positive testing, translated in testing of purchasing a item.</p>

<p> Also, designing a test suite and generating a html-type execution report, with scope of presenting and interpreting the results. </p>

# Section 4 : Deadlines(30.07.2024)

<p> Implementation of  personal portfolio:Deadline viewing  video course: From the day you get access until the final of the next day

  Deadline, 15.11.2024 </p>

<p> Finalizare documentatie librarie unittest + eficientizare cod  -> 30.07.2024 </p>

# Section 5: Description of the tests ruled+testing types and techniques used 

<p> In Python file "login.py" there were ruled 4 tests. </p>

<p> The test technique used is unittest framework, implemented in tests through TestCase in code, concretely test cases.</p>

<p> First test is to check the login with valid credentials, it is positive testing , </p>

 
