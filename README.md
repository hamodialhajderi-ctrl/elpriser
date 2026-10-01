# Elprisanalys

## Mål
Målet med projektet är att hämta elpriser från ett externt API, analysera dyraste 
och billigaste tider under dygnet, och spara resultatet i en CSV-fil. Projektet 
tränar grundläggande Python-koncept: API-anrop, felhantering, objektorienterad 
programmering (klasser och arv), samt filhantering.

## Metod
Programmet hämtar prisdata från det öppna API:et "Elpriset just nu" 
(elprisetjustnu.se) med hjälp av biblioteket `requests`. Varje pristillfälle 
representeras som ett objekt av klassen `Prisobservation`. Den tidpunkt med 
dygnets högsta pris representeras istället av barnklassen `ToppPrisObservation`, 
som ärver från `Prisobservation` men även sparar en anledning. Resultatet analyseras 
och sparas till en CSV-fil med hjälp av standardbiblioteket `csv`.

## Resultat
Programmet skriver ut högsta, lägsta och genomsnittligt pris för det valda datumet 
och elområdet, samt vilken tidpunkt som hade dygnets högsta pris. Resultatet sparas 
i filen `elpriser.csv`.

## Analys
[Skri## Analys
Resultatet visar tydligt att elpriset varierar mycket under dygnet. Det högsta priset 
inträffade vid 18:45 (2,56 SEK/kWh), vilket troligen beror på att det är då flest 
människor lagar mat, duschar och använder el samtidigt efter jobb/skola — alltså hög 
efterfrågan. Lägsta priset var 1,10 SEK/kWh, förmodligen under natten eller tidig 
morgon då förbrukningen är lägre. Medelpriset låg på cirka 1,63 SEK/kWh. Detta visar 
att det kan löna sig att flytta elkrävande aktiviteter (tvätt, laddning av elbil osv.) 
till tider med lägre pris

## Reflektion
## Reflektion
Det här projektet var utmanande eftersom jag är nybörjare i Python och innan projektet 
visste jag nästan ingenting om elpriser eller hur elmarknaden fungerar. Jag fick lära 
mig nästan allt från grunden: hur man hämtar data från ett API, hur klasser och arv 
fungerar i praktiken, hur man hanterar fel med try/except, och hur man sparar data till 
en CSV-fil. Jag lärde mig också hur man använder VS Code och Jupyter Notebook, bland 
annat hur man kör celler, skiljer på kod- och markdown-celler och felsöker när något 
inte fungerar som förväntat. Om jag gjorde om projektet skulle jag förmodligen planera 
strukturen (klasser, funktioner) tydligare från början istället för att bygga allt 
steg för steg.

## Installation
1. Klona repot: `git clone <GitHub-länk>`
2. Installera beroenden: `pip install requests`
3. Öppna `elpris_projekt.ipynb` i VS Code eller Jupyter och kör cellerna i ordning.

## GitHub-länk
https://github.com/hamodialhajderi-ctrl/elpriser]