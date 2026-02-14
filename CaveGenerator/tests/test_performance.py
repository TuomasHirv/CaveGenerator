import pytest
import random

from bowyer_watson import bowyer_watson
from prims import prims
from a_star import A_star


@pytest.mark.parametrize("amount", [100, 200, 300, 400])
def test_b_w_benchmark(benchmark, amount):
    """B_W should run in nlogn time."""
    #Here i test it with increasing amount to check how its run time increases.
    length = amount+10
    width = amount+10
    points = [(random.randint(0, length-1), random.randint(0, width-1)) for _ in range(amount)]

    result = benchmark(bowyer_watson, points, length, width)

    assert result != None

@pytest.mark.parametrize("size", [20, 40, 80, 160])
def test_a_star(benchmark, size):
    """A_star should run in ElogV time. E = amount of connections, V = amount of tiles"""
    #Increasing the size of the grid and at the same time increasing the size of the required path.
    start = (0, 0)
    end = (size-1, size-1)

    result = benchmark(A_star, start, end, size, size)

    assert result != None

@pytest.mark.parametrize("points", [100, 200, 300, 400])
def test_prims(benchmark, points):
    """Prims should run in ElogV time. E = connections between points, V = number of rooms"""
    