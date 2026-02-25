Tehty 25.02.26

# Coverage
https://app.codecov.io/gh/TuomasHirv/CaveGenerator
Coverage = 69.76%
Tämä johtuu erityisesti siitä, että main branchin pytestiä en osaa laittaa osaksi testejä.
Main.py coverage = 20%

Muitten tiedostojen coverage on 100% 
- Tämä johtuu erityisesti siitä, että tiedostoissa tehdään yksittäisiä testejä ja koko tiedoston testi.

# Test commands.
- Testit voidaan toistaa komennolla:
'poetry run pytest --ignore=tests/test_performance.py'
- Performanssi testit kannattaa pyörittää erikseen komennolla. (Lisä tietoa saa poistamalla viimeisen flagin.)
'poetry run pytest tests/test_performance.py --benchmark-columns=mean'

# Test cases by file

## A_star.py
(trace_route gets a grid where every point along a path points to the earlier one)
- Test for tracing a route in n by n uniform grid.
- Test for tracing failure.

- Testing that the basic functionality of A* algorithm works.

- Testing whole file with edges and an expected output for every path.

- Since the program failed for asymmetrical grid size i created additional tests for that.
- These also test for length of path given.

## Bowyer_watson

- Testing creating super triangle. Simple test.
- Testing bowyer watson to make sure it gives the amount of connections that is between the maximum amount and minimum.

## Prims algorithm

- Testing distance algorithm is simple.
- Testing for prims culling edges. This is supposted to always be n-1 (n = amount of points). But now i add additional connections in the function so it no longer can look at that.

## User Input.
- Simple tests (These arent algorithmic and dont need same detail)
- Tests for: Correct input. Too many rooms. Too low numbers.
- Correct input -> config.py changes.
- Too many rooms -> uses default.
- Too low numbers -> uses minimum numbers.
- Tests that setting default works.

## Height to color
- Simple tests (These arent algorithmic and dont need same detail)
- Tests that it defaults to acceptable numbers. (high/low)
- Tests that acceptable numbers work. 

## Rooms
- Simple tests (These arent algorithmic and dont need same detail)
- Grid, Room, Route, Mountain creation.
- Testing that rooms can be created in minimum space.
- Testing that too many rooms gives error but still returns the rooms that could be made.
- Testing that check_if_empty function checks tiles.

# Performance tests

- Run A*, Prims, Bowyer_watson. Four times with increasing inputs.
test_a_star[20]                 364.3226 (1.0)
test_a_star[40]               1,512.1990 (4.15)
test_a_star[80]               6,507.1560 (17.86)
test_a_star[160]             28,142.1649 (77.25)

- input doubles every time. Actual size is size*size and as such quadruples.
- (1.0) -> (4.15) -> (17.86) -> (77.25)
- Time increase is about nlog(n)


test_prims[100]                 366.5701 (1.01)
test_prims[200]                 792.8042 (2.18)
test_prims[400]               1,747.9945 (4.80)
test_prims[800]               3,852.0595 (10.57)
- Input doubles and it is used directly as the amount of points in system.
- (1.01) -> (2.18) -> (4.80) -> (10.57)
- Time increase is about nlog(n). 

test_b_w_benchmark[100]       6,798.7349 (18.66)
test_b_w_benchmark[200]      26,055.2975 (71.52)
test_b_w_benchmark[300]      58,337.3389 (160.13)
test_b_w_benchmark[400]     106,585.9800 (292.56)
- Input doubles everytime and is used directly.
- (18.66) -> (71.52) -> (160.13) -> (292.56)
- This is about n^2 But that is acceptable.