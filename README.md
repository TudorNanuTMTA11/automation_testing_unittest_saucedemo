# Sectiunea 1: Pachete de instalat

## Introducere

Limbajul Python este legat de Selenium WebDriver. Pachetul selenium este folosit pentru interactiunea automata cu browserele web din Python.

Exista cateva browsere sau drivere care sunt suportate precum Firefox, Chrome si Internet Explorer la fel ca si protocolul Remote. De asemenea, versiunile Python suportate sunt Python 3.8

## Instalare

Instalarea pachetelor se va face cu ajutorul utilitarului pip, care vine la pachet cu instalarea programului python, cu conditia ca la instalare sa se bifeze adaugarea acestuia la variabilele de mediu (environment variables).

Drept mentiune suplimentara, pentru a crea medii izolate si securizate de Python, se poate lua in considerare utilizarea virtualenv.


### Selenium

Pentru interactiunea cu elementele web va fi necesara instalarea librariei selenium. Acest lucru se face folosind comanda **pip install -U selenium**. 

### Drivere
Pentru a interactiona cu browserul, Selenium are nevoie de un driver care va fi instantiat prin intermediul clasei Driver, disponibila in libraria seleniumbase. 

Driverul va putea fi specificat prin trimiterea numelui acestuia ca argument al constructorului clasei Driver, iar daca acesta nu este specificat se va trimite numele browserului implicit din sistemul pe care ruleaza codul.

Libraria seleniumbase din care este importata clasa Driver se poate instala folosind comanda **pip install selenimbase**.


### Libraria unittest

Este o librarie predefinita in python, asa ca nu e necesar sa fie instalat altceva pentru a-l folosi, ci doar sa o importam prin comanda **import unittest**

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

# Sectiunea 4 : Deadline-uri(30.07.2024)

<p> Implementare portofoliu personal:Deadline vizualizare curs video: Din ziua in care primesti acces pana in următoarea zi la final

  Deadline, 15.11.2024 </p>

<p> Finalizare documentatie librarie unittest + eficientizare cod  -> 30.07.2024 </p>

# Sectiunea 5: Descrierea testelor facute+ tipurile si tehnicile de testare folosite

<p> In fisierul de Python "login.py" au fost efectuate 4 teste. </p>

<p> Tehnica de testare folosita este frameworkul unittest, transpusa in teste prin TestCase in cod, mai explicit cazuri de testare.</p>

<p> Primul test este de a verifica logarea cu credentiale valide, este testare pozitiva, </p>

 
