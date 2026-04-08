"""This is a file for unittesting prims-algorithm"""
import prims
import bowyer_watson

def test_distance():
    """Basic test to show distance works."""
    #This test isnt too specific as i think the distance function is quite provable mathematically.
    point_1 = (0, 0)
    point_2 = (1, 1)

    dist = prims.distance(point_1, point_2)

    assert dist == 2


def test_reindex_edges():
    """Basic test for reindexing indexes as it is quite simple"""
    edges = [((0,0), (1,1)), ((1,1), (2,2)), ((2,2), (0,0)), ]

    conns = prims.reindex_connections(edges)

    assert len(conns[(0,0)]) == 2
    assert len(conns[(1,1)]) == 2
    assert len(conns[(2,2)]) == 2

def test_prims():
    """Prims should always give n-1 connections (n is node amount)"""
    #Currently i am adding additional connections for a more interesting generation.
    edges = [((0,0), (1,1)), ((1,1), (2,2)), ((2,2), (0,0))]

    conns, _ = prims.prims(edges)

    assert len(conns) == 2

def test_large_sample():
    """Checking prims with a larger sample of points"""
    points = [(23, 45), (7, 88), (56, 12), (90, 3), (4, 67),
            (81, 44), (12, 22), (34, 56), (77, 88), (9, 10),
            (65, 5), (50, 50), (30, 70), (11, 3), (88, 99),
            (2, 14), (40, 41), (18, 77), (61, 33), (25, 80),
            (73, 11), (36, 90), (5, 6), (47, 24), (68, 17),
            (26, 58), (91, 41), (13, 8), (82, 61), (29, 14),
            (0, 0), (99, 99), (46, 73), (19, 39), (37, 62),
            (6, 84), (55, 31), (42, 20), (79, 16), (84, 3),
            (3, 97), (63, 43), (21, 29), (33, 68), (14, 55),
            (7, 77), (49, 5), (59, 60), (95, 2), (88, 44)]
    connections = bowyer_watson.bowyer_watson(points, 100, 100)

    culled_connections, _ = prims.prims(connections)
    checked_points = set()
    for a, b in culled_connections:
        checked_points.add(a)
        checked_points.add(b)

    assert checked_points == set(points)
    assert len(culled_connections) == len(points) - 1


def test_hardcoded():
    """testing prims algorithm with a hardcoded expected value"""
    points = [(0, 0),
            (2, 0),
            (4, 0),
            (0, 2),
            (2, 2),
            (4, 2),
            (0, 4),
            (2, 4),
            (4, 4),
            (2, 6),
    ]
    connections = bowyer_watson.bowyer_watson(points, 10, 10)

    culled, _ = prims.prims(connections)
    expected = [
    ((2, 2), (0, 2)),
    ((0, 2), (0, 0)),
    ((0, 0), (2, 0)),
    ((0, 2), (0, 4)),
    ((0, 4), (2, 4)),
    ((2, 0), (4, 0)),
    ((2, 2), (4, 2)),
    ((2, 4), (2, 6)),
    ((2, 4), (4, 4)),
    ]
    assert culled == expected


def test_disconnected_grid():
    """testing how prims works with a disconnected grid"""
    edges = [
    ((30, 34), (6, 46)),
    ((6, 46), (36, 28)),
    ((36, 28), (21, 29)),
    ((21, 29), (26, 21)),
    ((26, 21), (14, 6)),
    ((14, 6), (35, 37)),
    ((30, 34), (21, 29)),
    ((6, 46), (21, 29)),
    ((14, 6), (21, 29)),
    ((30, 34), (26, 21)),
    ((35, 37), (6, 46)),
    ((36, 28), (35, 37)),
    ((26, 21), (36, 28)),
    ((26, 21), (6, 46)),
    ((35, 37), (30, 34)),
    ((36, 28), (30, 34)),
    ((36, 28), (14, 6)),
    ((35, 37), (26, 21)),
    ((14, 6), (6, 46)),
    ((35, 37), (21, 29)),
    ((27, 2), (8, 49)),
    ((5, 30), (8, 49)),
    ((26, 21), (8, 49)),
    ((14, 6), (43, 42)),
    ((35, 37), (5, 30)),
    ((18, 32), (5, 30)),
    ((36, 28), (5, 30)),
    ((21, 29), (18, 32)),
    ((21, 29), (5, 30)),
    ((35, 37), (5, 30)),
    ]
    expected = [((30, 34), (35, 37)),
    ((30, 34), (36, 28)),
    ((30, 34), (21, 29)),
    ((21, 29), (18, 32)),
    ((21, 29), (26, 21)),
    ((18, 32), (5, 30)),
    ((26, 21), (14, 6)),
    ((5, 30), (8, 49)),
    ((21, 29), (6, 46)),
    ((14, 6), (43, 42)),
    ((8, 49), (27, 2))]
    culled, _ = prims.prims(edges)
    assert culled == expected