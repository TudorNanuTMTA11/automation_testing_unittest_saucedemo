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

The driver will be specified through sending its name as argument of the Driver class constructor , if it is not specified it will be sent the name of the implicit browser from the system where the code is ruled.
Seleniumbase library from where Driver class is imported can be installed by using the command  **pip install selenimbase**.


### Unittest library

It id a predefined library in python, so it is not necessary to be installed anything else to be used,only to import it through the command **import unittest**

### Pachetul html-testRunner

HtmlTest runner este un utilitar pentru executarea testelor care salveaza rezultatele  in fisiere html cu scopul prezentarii rezultatelor intr-un mod care poate fi citit cu usurinta.

Pentru utilizare este nevoie de:
- instalare: pip install html-testRunner
- import: import HtmlTestRunner
  


## Clonarea si rularea proiectului

Pentru clonare putem sa ne folosim de comanda **git clone TudorNanuTMTA11/automation_testing_unittest_saucedemo**

Pentru rularea proiectului se poate rula fisierul suita_teste.py astfel incat sa rulam toate testele, sau se poate rula cate un test individual din fisierul corespunzator, prin apasarea butonului verde aflat in stanga testului.


# Sectiunea 2: Structura proiectului

<p> Proiectul ,al carui nume este "ProiectFinal" se compune din:</p>

<p> Directoryul numit "ProiectFinal"</p>

<p> Directoryul numit "reports"</p>

<p> In cadrul directoryului "reports" se gaseste fisierul html "Test Results_2024-06-24_14-38-05.html</p>

<p> Fisierul de tip Python "___init__.py"</p>

<p> Fisierul de tip Python "inventory.py"</p>

<p> Fisierul de tip Python "login.py"</p>

<p> Fisierul de tip Python "suita_teste.py"</p>

# Sectiunea 3 : Obiectivele proiectului de testare automata

<p> Proiectul de testare automata are ca si baza site-ul "https://www.saucedemo.com/", cu logo-ul "SwagLabs".</p>

<p> Drept obiective,sunt testarea functionalitatii de logare,care se atinge prin testarea pozitiva,adica testarea logarii cu credentiale 

  valide </p>

<p> De asemenea, testarea functionalitatii de inventory, de asemenea atinsa prin testare pozitiva,adica testarea achizitionarii unui

produs</p>

<p> Precum si crearea unei suite de teste dar si generarea unui raport de executie de tip html, cu scopul de a prezenta si 

interpreta rezultatele </p>

# Section 4 : Deadlines(30.07.2024)

<p> Implementation of  personal portfolio:Deadline viewing  video course: From the day you get access until the final of the next day

  Deadline, 15.11.2024 </p>

<p> Finalizare documentatie librarie unittest + eficientizare cod  -> 30.07.2024 </p>

# Section 5: Description of the tests ruled+testing types and techniques used 

<p> In Python file "login.py" there were ruled 4 tests. </p>

<p> Tehnica de testare folosita este frameworkul unittest, transpusa in teste prin TestCase in cod, mai explicit cazuri de testare.</p>

<p> Primul test este de a verifica logarea cu credentiale valide, este testare pozitiva, </p>

 
