from main import height_to_color
import pytest

def test_correct():
    h = 0.5
    goal = (255*h, 255*h, 255*h)

    col = height_to_color(h)
    assert col == goal


def test_correct():
    h = -1
    goal = (0, 0, 0)

    col = height_to_color(h)
    assert col == goal


def test_correct():
    h = 2
    goal = (255*0.9, 255*0.9, 255*0.9)

    col = height_to_color(h)
    assert col == goal