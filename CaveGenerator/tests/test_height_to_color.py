from main import height_to_color
import pytest

def test_correct():
    h = 0.5
    benchmark = (255*h, 255*h, 255*h)

    col = height_to_color(h)
    assert col == benchmark


def test_correct():
    h = -1
    benchmark = (0, 0, 0)

    col = height_to_color(h)
    assert col == benchmark


def test_correct():
    h = 2
    benchmark = (255*0.9, 255*0.9, 255*0.9)

    col = height_to_color(h)
    assert col == benchmark