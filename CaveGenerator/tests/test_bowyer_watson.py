"""Testing Bowyer_Watson implementation"""
import random
from collections import defaultdict
import bowyer_watson


def test_super_triangle():
    """Testing super triangle creation"""
    (a, b, c) = bowyer_watson.get_super_triangle(100, 100)
    margin = max(100, 100)*10

    assert a == (-margin, -margin)
    assert b == (100//2, margin *2)
    assert c == (100 + margin, -margin)

def test_bowyer_watson():
    """Testing that bowyer watson creates enough and not too many connections"""
    n = 10
    random_points = set()
    width = 50
    length = 50
    while len(random_points) < n:
        random_points.add((random.randint(0, width-1), random.randint(0, length-1)))

    connections = bowyer_watson.bowyer_watson(random_points, width, length)

    assert len(connections) >= (2*n - 3)
    assert len(connections) <= (3*n - 6)


def test_points_line():
    """when points are in a line returns nothing"""
    point_line = set()
    point_line.add((3, 0))
    point_line.add((2, 0))
    point_line.add((4, 0))
    point_line.add((5, 0))
    point_line.add((6, 0))
    point_line.add((1, 0))
    connections = bowyer_watson.bowyer_watson(point_line, 10, 10)

    assert len(connections) == 0


def test_points_line_mirrored():
    """when points are in a line returns nothing on another axis"""
    point_line = set()
    point_line.add((0, 3))
    point_line.add((0, 2))
    point_line.add((0, 4))
    point_line.add((0, 5))
    point_line.add((0, 6))
    point_line.add((0, 1))
    connections = bowyer_watson.bowyer_watson(point_line, 10, 10)

    assert len(connections) == 0


def test_square():
    """when given a square of points returns 2 triangles (always the same)"""
    #((0, 0), (3, 0)), ((0, 0), (0, 3)), ((0, 3), (3, 0))
    #((3, 0), (3, 3)), ((0, 3), (3, 3)), ((0, 3), (3, 0))
    point_square = set()
    point_square.add((0,0))
    point_square.add((0,3))
    point_square.add((3,0))
    point_square.add((3,3))
    connections = bowyer_watson.bowyer_watson(point_square, 10, 10)

    assert connections == [((3, 0), (3, 3)),
                           ((0, 0), (3, 0)),
                           ((0, 3), (3, 3)),
                           ((0, 0), (0, 3)),
                           ((0, 3), (3, 0))]


def test_triangles_and_all_points():
    """test that all edges and points are in a triangle"""
    n = 100
    random_points = set()
    width = 200
    length = 200
    while len(random_points) < n:
        random_points.add((random.randint(0, width-1), random.randint(0, length-1)))
    connections = bowyer_watson.bowyer_watson(random_points, width, length)
    edges_dict = reindex_connections(connections)
    #Checking every point by making sure that their edges loop back in 3 steps
    assert len(edges_dict) == len(random_points)

    while len(random_points) > 0:
        point = random_points.pop()
        if len(edges_dict[point]) == 0:
            assert False
        for first in edges_dict[point]:
            correct = False
            second_point = first[1]
            for second in edges_dict[second_point]:
                if second == first:
                    continue

                third_point = second[1]
                for third in edges_dict[third_point]:
                    if point == third[1]:
                        correct = True
                        break
                if correct:
                    break
            if not correct:
                assert False

def test_no_edge_crossings():
    """tests that no edges in the triangulation intersect"""
    n = 100
    random_points = set()
    width = 200
    length = 200
    while len(random_points) < n:
        random_points.add((random.randint(0, width-1), random.randint(0, length-1)))

    connections = bowyer_watson.bowyer_watson(random_points, width, length)

    edges = set()
    for a, b in connections:
        edges.add(tuple(sorted((a, b))))


    edges = list(edges)
    for i in range(len(edges)):
        a, b = edges[i]
        for j in range(i + 1, len(edges)):
            c, d = edges[j]

            if len({a, b, c, d}) < 4:
                continue

            if segments_intersect(a, b, c, d):
                assert False

def segments_intersect(p1, q1, p2, q2):
    """checks if lines cross each other"""
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return True
    return False

def orientation(a, b, c):
    """checks the orientation of a line with a given point"""
    val = (b[1] - a[1]) * (c[0] - b[0]) - (b[0] - a[0]) * (c[1] - b[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2

def reindex_connections(edges_list):
    """Indexes connections to a dictionary"""
    #So i can reliably and quickly check all edges from all points
    edges_dict = defaultdict(set)
    for edge in edges_list:
        edges_dict[edge[0]].add((edge[0], edge[1]))
        edges_dict[edge[1]].add((edge[1], edge[0]))
    return edges_dict
