"""Testing Bowyer_Watson implementation"""
import random
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
