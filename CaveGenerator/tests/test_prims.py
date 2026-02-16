import pytest
import prims

def test_distance():
    """Basic test to show distance works."""
    #This test isnt too specific as i think the distance function is quite provable mathematically.
    point_1 = (0, 0)
    point_2 = (1, 1)

    dist = prims.distance(point_1, point_2)

    assert dist == 2


def test_reindex_edges():
    """Basic test for reindexing indexes as it is quite simple"""
    list = [((0,0), (1,1)), ((1,1), (2,2)), ((2,2), (0,0)), ]

    conns = prims.reindex_connections(list)

    assert len(conns[(0,0)]) == 2
    assert len(conns[(1,1)]) == 2
    assert len(conns[(2,2)]) == 2

def test_prims():
    """Prims should always give n-1 connections (n is node amount) But i have added additional code that sometimes adds new routes"""
    list = [((0,0), (1,1)), ((1,1), (2,2)), ((2,2), (0,0))]

    conns = prims.prims(list)

    assert len(conns) >= 2
