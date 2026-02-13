import pytest
import config


import rooms

def test_grid_creation():
    """
    Testing if grid creation functions
    """
    width = 100
    length = 100
    grid = rooms.Grid(width, length)

    assert grid.tile_map[0][0] == 0
    assert grid.tile_map[width-1][length-1] == 0

def test_room_creation():
    """
    Testing creating 1 room
    """
    grid = rooms.Grid(20, 20)
    points = rooms.create_rooms(grid, 1)

    assert len(points) != 0

def test_creation_minimum_space():
    """
    Testing creating on the smallest grid the most rooms
    """
    grid = rooms.Grid(20, 20)
    points = rooms.create_rooms(grid, (20/20)*3)

    assert len(points) != 0

def test_too_many_rooms(capsys):
    """
    Testing creating too many rooms
    """
    grid = rooms.Grid(20, 20)

    points = rooms.create_rooms(grid, 400)
    captured = capsys.readouterr()
    assert len(points) != 0
    assert "Couldn't fit all the rooms into the grid" in captured.out

def test_if_empty():
    """
    Testing if atleast 24 tiles are filled.
    """
    grid = rooms.Grid(20, 20)
    points = rooms.create_rooms(grid, 1)
    counter = 0
    for x in range(0, 19):
        for y in range(0, 19):
            if not grid.check_if_empty(x, y):
                counter+=1
                if counter == 24:
                    break
    assert counter >= 24




