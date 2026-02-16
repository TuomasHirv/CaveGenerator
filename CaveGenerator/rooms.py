import random
from collections import deque
import math
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
    def __init__(self, width, length, mountains):
        self.length = length
        self.width = width
        self.tile_map = self.create_mountain(mountains)

    def create_mountain(self, n):
        if n == 0:
            return [[0 for _ in range(self.width)] for _ in range(self.length)]
        tilemap = [[0 for _ in range(self.width)] for _ in range(self.length)]
        while n > 0:
            (start_x, start_y) = (random.randint(5, self.width-5), random.randint(5, self.length-5))
            descent = 0.05
            height = 0.6
            tilemap[start_y][start_x] = height

            #Trying out a cleaner way to check tiles around recursively.
            tiles = deque([(start_x, start_y)])
            visited = set([(start_x, start_y)])

            while tiles:
                nx, ny = tiles.popleft()
                if tilemap[ny][nx] > 0.05:
                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1), (1,1), (-1, -1)]:
                        next_x, next_y = (nx + dx, ny + dy)
                        if not (next_x, next_y) in visited and self.width > next_x >= 0 and self.length > next_y >= 0: 
                            distance = math.hypot(next_x-start_x, next_y-start_y)
                            if tilemap[next_y][next_x] < height - (distance*descent):
                                tilemap[next_y][next_x] = height - (distance*descent)
                                tiles.append((next_x, next_y))
                            visited.add((next_x, next_y))
            n -= 1

        return tilemap

    def check_if_empty(self, x, y):
        if self.tile_map[x][y] < 1:
            return True
        else:
            return False
        
    def check_if_not_room(self, x, y):
        if self.tile_map[x][y] != 1:
            return True
        else:
            return False
    
    def check_for_weigth(self, x, y):
        #Here we check for the terrain weight
        if self.tile_map[x][y] < 1:
            return self.tile_map[x][y]+0.5
        elif self.tile_map[x][y] == 4:
            #Making it cheaper to traverse on already created roads
            return 0
        else:
            return 0.4

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
            #Counting how many times a tile is used for a route
            #It is quite interesting since it is cheaper to reuse route tiles
            if self.check_if_not_room(point[1],point[0]):
                if self.tile_map[point[1]][point[0]] == 5:
                    self.tile_map[point[1]][point[0]] = 6
                elif self.tile_map[point[1]][point[0]] == 4:
                    self.tile_map[point[1]][point[0]] = 5
                else:
                    self.tile_map[point[1]][point[0]] = 4

def create_rooms(grid, room_amount):
    room_current_amount = 0
    max_attempts = 100000
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