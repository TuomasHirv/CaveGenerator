# Viikkoraportti, viikko 6

Tällä viikolla loin kiinnostavamman generaation.
Optimoin A* uudestaan sitä varten.

## Tein:
1. Kenttään lisätään kukkuloita.
2. A* välttää kukkulan tilejä niitten korkeuden perusteella (0.1-0.9)
3. A* yrittää uudelleen käyttää aikaisempia teitä.
4. A* luo yhden tien kerrallaan ja se painetaan kenttään ennen seuraavaa generaatiota.
5. Laitoin aikasemman version omaan branchiinsä nimellä: before-weighted-generation.

## Haastavaa oli
Haastava asia oli muuttaa A* nopeaksi

## Opin tekemään kiinnostavamman generaatio algoritmin.
A* antaa mahdollisuuden luoda kiinnostavampia reittejä jos lisää eri paikoille painoja.
Käytin tätä hyväksi siinä, että se nyt välttää eri maastoja ja preferoi aikaisemmin luotuja teitä.

Opin siitä, kuinka python kutsuu funktioita jotka ovat eri tiedostoissa. Opin myös, että Euclidian distance on hidas.


## Epäselvyyksiä ei ole tällä hetkellä.
- Onko vielä jotain mitä kannattaisi tehdä projektiin?

## Seuraavalla viikolla.
- Loput dokumentaatiot, joita en ole vielä tehnyt.
- Pieniä juttuja UI:n kanssa ehkä.

## AI:n käyttö
- Tutkin mahdollisia maaston luonti algoritmeja. Päätin käyttää omaa simppeliä versiota AI:n sijaan.
- Uusien selvempien värien valitseminen maastolle.
- Sain myös selville, että on mahdollista käyttää Manhattan etäisyyttä Euclidian etäisyyden sijaan.
- Sain selville myös optimoinnista: Funktiot jotka eivät ole ns inline ovat hitaita. Euclidian distance on hidas.