# Viikkoraportti, viikko 5

Tällä viikolla sain A_star ja Prims algoritmit liitettyä projektiin.
Tein myös unittestit ohjelmaan ja hieman performanssi testejä.
## Tein:
1. Yhteydet karsitaan käyttäen prims algoritmia.
2. Yhteyksien perusteella muodostetaan reittejä jotka täytetään erillisellä funktiolla
3. Lisäsin todella kattavat unittestit ohjelmistoon.
4. Tein performanssi testejä.

## Haastavaa oli
Prims ja Performanssi testit. En ole aikaisemmin käyttänyt niitä.
Opin kuitenkin hyvin siitä, miten prims algoritmi voidaan optimoida käyttäen erityyppisiä data structuureja.
Performanssi testit ovat uusia, mutta opin niistäkin paljon.
A_star on helpompi ja olen aikaisemmin käyttänyt sitä. 
(Tosin sitä koodia voisi tehdä paremman näköiseksi ainakin)

## Opin sen, että minun Bowyer_watson algoritmi on naiivi.
Tehdessäni performanssi testin huomasin, että algoritmi toimii n^2 ajassa eikä nlogn ajassa.
Tämä pitää korjata. Saan ehkä lisää performanssi testejä tehtyä.

## Epäselväksi jäi Bowyer_Watson algoritmin optimointi.
Olettaisin, että ongelma on se, että katson läpi liikaa asioita tehdessäni in_circle testin, mutta en ole vielä varma.
On toinen algoritmi (saman tyyppinen) nimeltä Divide_and_Conquer, missä pisteet leikataan kahtia. En kuitenkaan usko, että minun kannattaa vaihtaa siihen.

## Seuraavalla viikolla aion optimoida algoritmeja toimimaan paremmin.
Tämä tulee olemaan haastavaa, toivottavasti muut algoritmit noudattavat haluttuja aika vaatimuksia.
Saatan tehdä lisää unittestejä main.py tiedostoa varten.
Saatan tehdä lisä toiminnallisuuksia ohjelmiston visualisointia varten.


## AJAT (Teen näitä hieman myöhässä, niin olen unohtanut millä päivällä tein mitä)
- tein noin 5 tuntia A_star ja Prims algoritmia.
- 2 tuntia pytestejä (muutin hieman koodia samalla kun huomasin asioita testeistä.)
- alle 1 tunti performanssi testejä.