"""Testing height_to_color"""
from main import height_to_color

def test_correct():
    """Testing the correct values"""
    h = 0.5
    goal = (255*h, 255*h, 255*h)

    col = height_to_color(h)
    assert col == goal


def test_incorrect_low():
    """Testing with a too low value"""
    h = -1
    goal = (0, 0, 0)

    col = height_to_color(h)
    assert col == goal


def test_incorrect_high():
    """Testing with a too high value"""
    h = 2
    goal = (255*0.9, 255*0.9, 255*0.9)

    col = height_to_color(h)
    assert col == goal
