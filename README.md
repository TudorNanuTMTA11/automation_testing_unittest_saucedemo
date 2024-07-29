# Sectiunea 1: Pachete de instalat

## Pachetul Selenium

### Introducere

<p>Limbajul Python este legat de Selenium WebDriver. Pachetul selenium este folosit pentru interactiunea automata cu browserele web din Python.</p>

<p>Exista cateva browsere sau drivere care sunt suportate precum Firefox, Chrome si Internet Explorer la fel ca si protocolul Remote.
De asemenea, versiunile Python suportate sunt Python 3.8+.</p>

### Instalare

<p>Daca exista pip in sistem, pur si simplu se instaleaza sau actualizeaza legaturile cu Python prin comanda: pip install -U selenium. Ca si alternativa, se poate descarca distributia sursei din PyPI <https://pypi.org/project/selenium/#files>, apoi se dezarhiveaza si se ruleaza cu comanda: python setup.py install.</p>

<p>Drept mentiune suplimentara, pentru a crea medii izolate si securizate de Python , se poate lua in considerare utilizarea virtualenv.</p>

### Drivere
<p>Selenium are nevoie de un driver pentru a interfata cu browserul ales. </p>
  
<p>Firefox,de exemplu are nevoie de geckodriver.</p>


## Pachetul SeleniumBase

### Instalare

<p>SeleniumBase poate fi instalat din PyPi sau GitHub.</p>

<p>Cum se instaleaza SeleniumBase din PyPi, cu comanda pip install seleniumbase.</p>

<p>Mai sunt si alte comenzi ce pot fi folosite pentru actualizari sau daca sunt folosite mai multe versiuni de Python, precum:
 (Add --upgrade OR -U to upgrade SeleniumBase.), (Add --force-reinstall to upgrade indirect packages.),
  (Use pip3 if multiple versions of Python are present.).</p>

<p> Cum se instaleaza seleniumbase dintr-o clona de GitHub</p>

<p> Prin urmatoarea structura: </p> 

<p> git clone https://github.com/seleniumbase/SeleniumBase.git

  cd SeleniumBase/

pip install -e . </p>

<p> Cum se actualizeaza o instalare existenta dintr-o clona de GithHub</p>

<p>Cu urmatoarea structura:</p>

<p>git pull

  pip install -e .</p>

<p>Descarcarea webdriverelor</p>

<p>SeleniumBase isi descarca automat webdriverele de care are nevoie, precum chromedriver</p>

<p>SeleniumBase automat controleaza actiuni comune ale WebDriver precum lansarea browserelor web inainte de teste,salvarea capturilor

de ecran in timpul esecurilor si inchiderea browserelor web dupa teste</p>

## Pachetul unittest

<p>Este un pachet ce este deja disponibil in libraria standard, asa ca nu e necesar sa fie instalat altceva pentru a-l folosi.</p>

## Pachetul html-testRunner

<p>HtmlTest runner este un rulator de teste al lui unittest care salveaza rezultatele testelor in fisiere html cu scopul prezentarii 

rezultatelor intr-un mod care poate fi citit de om.</p>

<p> Cum se foloseste</p>

<p> Cu structura: 
  
  import HtmlTestRunner

import unittest</p>

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

 
