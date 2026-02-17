"""Testing user input functionality"""

import config
from main import input_user_values, default_config

def test_input_correct():
    """
    Testing if the user input function changes config.
    """
    assert config.WIDTH == 100
    assert config.LENGTH == 75
    assert config.ROOM_AMOUNT == 10

    test_width = 50
    test_length = 20
    test_rooms_amount = 10
    test_mountains = 10
    input_user_values(test_width, test_length, test_rooms_amount, test_mountains)

    assert config.WIDTH == test_width
    assert config.LENGTH == test_length
    assert config.ROOM_AMOUNT == test_rooms_amount
    assert config.MOUNTAINS == test_mountains


def test_default_config():
    """
    Testing that defaulting the config works fine.
    """
    config.WIDTH = 30
    config.LENGTH = 30
    config.ROOM_AMOUNT = 3
    config.MOUNTAINS = 1

    default_config()

    assert config.WIDTH == 100
    assert config.LENGTH == 75
    assert config.ROOM_AMOUNT == 10
    assert config.MOUNTAINS == 3


def test_too_many_rooms(capsys):
    """
    When given too many rooms per tile it should default the config and print into console
    """
    test_width = 3
    test_length = 3
    test_rooms = 10
    test_mountains = 20
    input_user_values(test_width, test_length, test_rooms, test_mountains)
    captured = capsys.readouterr()

    assert "Too many rooms using defaults" in captured.out

    assert config.WIDTH == 100
    assert config.LENGTH == 75
    assert config.ROOM_AMOUNT == 10
    assert config.MOUNTAINS == 3

def test_low_numbers():
    """
    Given too low numbers the function should default to set numbers
    """
    test_width = 10
    test_length = 10
    test_rooms = 1
    test_mountains = 0
    input_user_values(test_width, test_length, test_rooms, test_mountains)

    assert config.WIDTH == 20
    assert config.LENGTH == 20
    assert config.ROOM_AMOUNT == 3
    assert config.MOUNTAINS == 0
