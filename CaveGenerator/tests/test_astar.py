import pytest
import a_star

def test_distance():
    """Basic check to test distance"""
    p1 = (0, 0)
    p2 = (3, 3)
    
    dist = a_star.distance(p1, p2)

    assert round(dist) == 4


def test_trace_route():
    """Test for route tracing function"""
    n = 10
    route = [[None for _ in range(n)] for _ in range(n)]

    for x in range(n-1):
        for y in range(n-1):
            if x == 0 and y == y:
                route[x][y] = (-1, -1)
            elif x > 0:
                route[x][y] = (x-1, y)
            else:
                route[x][y] = (x, y-1)
    
    path = a_star.trace_route(route, (0,0), (n-1, n-1))

    assert path != None

def test_trace_fail_route():
    """Test for route tracing function"""
    n = 10
    route = [[None for _ in range(n)] for _ in range(n)]

    for x in range(n-1):
        for y in range(n-1):
            if x == 0 and y == y:
                route[x][y] = (-1, -1)
            elif x > 0:
                route[x][y] = (x-1, y)
            else:
                route[x][y] = (x, y-1)
    
    path = a_star.trace_route(route, (n-1, n-1), (0,0))

    assert path == None



def test_a_star():
    """Testing the a_star function directly"""
    n = 35

    p1 = (5, 3)

    p2 = (31, 25)

    a_star.A_star(p1, p2, n, n)


def test_whole_file():
    """Testing the whole file run from starter"""
    n = 35

    edge_1 = ((5, 3), (31, 25))
    edge_2 = ((0, 0), (10, 10))
    edge_3 = ((8, 8), (8, 30))
    edge_4 = ((31, 25), (5, 3))
    edge_5 = ((15, 0), (20, 5))

    list = [edge_1, edge_2, edge_3, edge_4, edge_5]

    routes = a_star.starter(list, n, n)

    assert len(routes) == 5

def test_whole_file_asymmetrical():
    """Testing if the file works with a screen that isnt symmetrical"""
    width = 20
    length = 70
    edge_1 = ((5, 3), (19, 60))
    edge_2 = ((0, 0), (width-1, length-1))
    edge_3 = ((8, 50), (8, 30))
    edge_4 = ((width-1, length-1), (0, 0))
    edge_5 = ((15, 0), (18, 5))

    list = [edge_1, edge_2, edge_3, edge_4, edge_5]

    routes = a_star.starter(list, length, width)

    assert len(routes) == 5

def test_whole_file_asymmetrical_flipped():
    """Testing if the file works with a screen that isnt symmetrical"""
    width = 70
    length = 20
    edge_1 = ((5, 3), (60, 19))
    edge_2 = ((0, 0), (width-1, length-1))
    edge_3 = ((8, 8), (8, 17))
    edge_4 = ((width-1, length-1), (0, 0))
    edge_5 = ((15, 0), (20, 5))

    list = [edge_1, edge_2, edge_3, edge_4, edge_5]

    routes = a_star.starter(list, length, width)

    assert len(routes) == 5