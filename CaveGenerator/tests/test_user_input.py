import config
from main import input_user_values, default_config

import pytest

def test_input_correct():
    """
    Testing if the user input function changes config.
    """
    assert config.width == 100
    assert config.length == 75
    assert config.room_amount == 10

    test_width = 50
    test_length = 20
    test_rooms_amount = 10
    input_user_values(test_width, test_length, test_rooms_amount)

    assert config.width == test_width
    assert config.length == test_length
    assert config.room_amount == test_rooms_amount


def test_default_config():
    """
    Testing that defaulting the config works fine.
    """
    config.width = 30
    config.length = 30
    config.room_amount = 3

    default_config()

    assert config.width == 100
    assert config.length == 75
    assert config.room_amount == 10


def test_too_many_rooms(capsys):
    """
    When given too many rooms per tile it should default the config and print into console
    """
    test_width = 3
    test_length = 3
    test_rooms = 10

    input_user_values(test_width, test_length, test_rooms)
    captured = capsys.readouterr()

    assert "Too many rooms using defaults" in captured.out

    assert config.width == 100
    assert config.length == 75
    assert config.room_amount == 10

def test_low_numbers():
    """
    Given too low numbers the function should default to set numbers
    """
    test_width = 10
    test_length = 10
    test_rooms = 1

    input_user_values(test_width, test_length, test_rooms)

    assert config.width == 20
    assert config.length == 20
    assert config.room_amount == 3
