# Rakenne
Ohjelmisto pyörii main.py tiedostosta.
Main functiossa on 2 osaa. Syöte osa ja Visualisointi osa. Syöte osassa käyttäjä syöttää haluamansa muuttujat ohjelmaan. Sen lopussa initialisoidaan grid rakenne, johon muut osa visualisoidaan.
- Visualisointi ja generointi tapahtuu osissa, syöte osan jälkeen.

- Ohjelmisto on eritelty eri tiedostoihin:
    rooms.py: Sisältää grid ja room olion. Siellä on myös niihin liittyvä logiikka.
    bowyer_watson.py: Sisältää logiikan Bowyer_watson algoritmille.
    prims.py:sisältää Prims algoritmin logiikan
    a_star.py: sisältää A* algoritmin.
    Tämä on aika simppeli, mutta tehdessä generointia näissä on mukana myös apufunktioita jotka auttavat niitten kutsumista main.py:stä

- Testaus on tests tiedostossa:
    Testit jakautuvat unittesteihin (pytest)
    Benchmark testeihin (benchmark)

# O-analyysi
- Lisätietoa löytyy performance_documentation.md tiedostosta.

- Bowyer_watson:
    test_b_w_benchmark[100]       6,600.7917 (17.57)
    test_b_w_benchmark[200]      25,643.0615 (68.27)
    test_b_w_benchmark[300]      62,383.0647 (166.10)
    test_b_w_benchmark[400]     103,794.4000 (276.35)

    Hyväksyttävä. noin n^2

- A*
    test_a_star[20]                 409.3170 (1.09)
    test_a_star[40]               1,743.4972 (4.64)
    test_a_star[80]               7,394.2774 (19.69)
    test_a_star[160]             31,194.8688 (83.06)

    Hyväksyttävä. noin slog(s) (kun s on tiilien määrä (syöte*syöte = s))

- Prims
    test_prims[100]                 375.5854 (1.0)
    test_prims[200]                 800.8028 (2.13)
    test_prims[400]               1,803.4187 (4.80)
    test_prims[800]               3,994.4695 (10.64)

    Hyväksyttävä. noin nlog(n). (n on karsittavien yhteyksien määrä)

Algoritmit toimivat todella nopeasti.

# Puutteet
- En koe, että työssä olisi mitään kriittistä puutetta.
- A* (tie generaatio) omaa nyt hieman enemmän vivahdetta kuin aikaisemmin, mutta siihen voi aina lisätä asioita.

# Kielimallit
GEMINI PRO
- Pygamen ymmärtäminen
    En ollut aikaisemmin käyttänyt tätä.
    Esimerkiksi:
        Piirtäminen 
        Piirtäminen kuvaan ei suoraan ruudulle.
        Kuvan siirtäminen
        Pelin aikaiset syötteet.
- Yleinen muistin virkistäminen
    En ole käyttänyt pythonia vähään aikaan.
    Asiat kuten miten kutsun set() ja miten voin tehdä eri data rakenteita.
    Kyselin myös mitkä asiat tekevät koodista hitaampia kuten:
        Funktio kutsut eri tiedostoihin.
        Heuristiikka (euclidian/manhattan)
- Muutti koodia hienommaksi
    Tämä tosin tehtiin vain kerran rooms.py tiedostossa, koska muut kerrat geminin koodi rikkoi sovelluksen.
    Se kuitenkin antoi hyviä ideoita miten parantaa koodia.
- Yleinen kysely algoritmin ideasta
    InCircle oli haastava minulle (determinantti).
    Prims perus idea (minimi määrä yhteyksiä, jotka ovat mahdollisimman pieniä).
Tämä oli Gemini suosima rakenne:
´´´
for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1),]:
    next_x, next_y = (x + dx, y + dy)
´´´
(Tämä on itse rakennettu, mutta aikaisemmin tein tämä if statementeillä. Nyt toi ottaa eri suunnat rekursiivisesti suunta listasta)

Lähteet:
https://en.wikipedia.org/wiki/Prim%27s_algorithm

https://en.wikipedia.org/wiki/Bowyer%E2%80%93Watson_algorithm

https://vazgriz.com/119/procedurally-generated-dungeons/