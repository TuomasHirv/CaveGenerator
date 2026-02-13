import pytest
import a_star

def test_distance():
    """Basic check to test distance"""
    p1 = (0, 0)
    p2 = (3, 3)
    
    dist = a_star.distance(p1, p2)

    assert round(dist) == 4


