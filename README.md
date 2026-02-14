[![codecov](https://codecov.io/gh/TuomasHirv/CaveGenerator/graph/badge.svg?token=TVX9WDK5WS)](https://codecov.io/gh/TuomasHirv/CaveGenerator)

# CaveGenerator
Aineopintojen harjoitustyö. Helsingin Yliopiston kurssiin.

Projekti tehdään Pythonilla.
Osaan myös C, C#, haskell kieliä.

Tavoitteena on luoda sovellus joka:
1. Asettaa satunnaisesti huoneita alueelle
2. Löytää niitten välisiä yhteyksiä triangulaatiolla. Bowyer-Watson algorithm
3. Mahdollisesti karsii niistä osan. Prim’s algorithm
4. Käyttäen A* algoritmia rakentaa tunneleita, minimoiden tarvittavien tunneleiden määrän.

Projektin ydin on verkoston luomisessa. Erityisen tärkeitä ovat triangulaatio karsiminen pitäen kaikki huoneet yhteydessä verkkoon ja A* algoritmilla tehtävä tunnelien minimointi.

Bowyer-Watson on O(N log N) (Missä N on pisteitten,tässä tilanteessa huoneitten määrä)
Prim's algorithm is O(V^2) (Missä V on verticien määrä)
A* taas on käytännössä usein O(nlogn) (Missä N on pisteitten määrä)

Kannattaa muistaa, että A* algoritmi suoritettaisiin jokaiselle tunnelille. Se tarkoittaa samalla, että se suoritetaan monesti(Kasvattaa aika-arviota), mutta myös sitä, että se suoritetaan pienemmille kokonaisuuksille(Pienentää n:ää)

Kurssimateriaalissa annettu materiaali mitä aion käyttää:
https://vazgriz.com/119/procedurally-generated-dungeons/
Uskon, että kurssin aikana joudun tutkimaan algoritmeja lisää, sillä tämä antoi minulle vain nopean käsityksen siitä, mitä projektissa tulee olemaan.

Opiskelen tietojenkäsittelytieteen kandidaatti (TKT) tutkintoa



# Install instructions

Clone the repository.
Move your Console to the repository root and then to the CaveGenerator directory. 
run poetry install
poetry add pygame
then run
python main.py
or
python3 main.py
