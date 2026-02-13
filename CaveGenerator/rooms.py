import random


class Room:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def carve_room(self, grid):
        y = self.y
        x = self.x

        h = self.h
        w = self.w

        for row in range(y, y + h):
            for col in range(x, x + w):
                grid.tile_map[row][col] = 1
        
        for col in range(x, x + w):
            grid.tile_map[y][col] = 2
            grid.tile_map[y + h - 1][col] = 2

        for row in range(y, y + h):
            grid.tile_map[row][x] = 2
            grid.tile_map[row][x + w - 1] = 2

        for row in range(y - 1, y + h + 1):
            for col in range(x - 1, x + w + 1):
                if 0 <= row < grid.length and 0 <= col < grid.width:
                    if grid.tile_map[row][col] == 0:
                        grid.tile_map[row][col] = 3
        point = (x+(w// 2), y+(h// 2))
        return point

class Grid():
    def __init__(self, width, length):
        self.tile_map = [[0 for _ in range(width)] for _ in range(length)]
        self.length = length
        self.width = width

    def check_if_empty(self, x, y):
        if self.tile_map[x][y] == 0:
            return True
        else:
            return False
        
    def check_if_not_room(self, x, y):
        if self.tile_map[x][y] != 1:
            return True
        else:
            return False

    def validation_rooms(self, x, y, w, h):
        tiles = [(col, row) for row in range(y, y + h) for col in range(x, x + w)]
        validation = True
        for tile in tiles:
            if not self.check_if_empty(tile[1], tile[0]): 
                validation = False
                break
        return validation
    def carve_route(self, route):
        for point in route:
            if self.check_if_not_room(point[1],point[0]):
                self.tile_map[point[1]][point[0]] = 4

def create_rooms(grid, room_amount):
    room_current_amount = 0
    max_attempts = 1000
    attempts = 0

    center_tiles = []

    while room_current_amount < room_amount and attempts < max_attempts:
        w, h = random.randint(4, 8), random.randint(4, 8)
        x, y = random.randint(0, grid.width - w), random.randint(0, grid.length - h)
        if grid.validation_rooms(x, y, w, h):
            my_room = Room(x, y, w, h)

            center_tiles.append(my_room.carve_room(grid))
            room_current_amount+=1
        attempts += 1
    if attempts >= max_attempts:
        print("Couldn't fit all the rooms into the grid")
        return center_tiles
    return center_tiles


def create_routes(list, grid):
    for route in list:
        grid.carve_route(route)