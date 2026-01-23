Määrittelydokumentti
Tämä dokumentti määrittelee Helsingin Yliopiston Tietojenkäsittelytieteen kandiohjelman Aineopintojen harjoitustyö: Algoritmit ja tekoäly (periodi 3), Monimuoto-opetus kurssin toteutusta.
2026


Aihe
Tämän työn tavoitteena on toteuttaa ohjelma, joka generoi luolaston proseduraalisesti kokonaisuudessaan ja esittää sen visuaalisesti generoinnin jälkeen.


Luolaston generointi perustuu monivaiheiseen prosessiin, jossa eri algoritmit vastaavat eri osista lopullista rakennetta.
1. tilaan asetetaan huoneita. Varmistetaan, että huoneet eivät ole päällekkäin.
2. Luodaan yhteyksiä huoneitten välille käyttäen triangulaatiota
3. Karsitaan yhteyksiä
4. Rakennetaan yhteyksistä konkreettisia tunneleita.

Työn lopputuloksena syntyy visuaalisesti esitettävä luolasto, joka demonstroi kehittyneiden geometria-algoritmien käyttöä käytännön ohjelmointitehtävässä.

Ohjelmointikielet
Python


Algoritmit
Delaunay-triangulaatiota. (Tarkemmin Bowyer-Watson algoritmia)  https://vazgriz.com/119/procedurally-generated-dungeons/
Prim's: algoritmi karsimaan yhteyksiä ilman, että jokin huone olisi poissa verkosta.
A*: luomaan konkreettisia tunneleita yhteyksien perusteella.