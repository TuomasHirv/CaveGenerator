import pygame
import random

room_amount = 10

tile_size = 10
width = 100
length = 75

screen_width = width*tile_size
screen_length = length*tile_size

void_col = (0,0,0)
wall_col = (100, 100, 100)
floor_col = (200, 200, 200)
added_space_col = (50, 50, 50)


class Room:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

def carve_room(grid, room):
    for row in range(room.y, room.y + room.h):
        for col in range(room.x, room.x + room.w):
            grid.tile_map[row][col] = 1

            if row == room.y:
                grid.tile_map[row][col] = 2
                if row -1 >= 0:
                    grid.tile_map[row-1][col] = 3

            if col == room.x:
                grid.tile_map[row][col] = 2
                if col -1 >= 0:
                    grid.tile_map[row][col-1] = 3
            
            if row == room.y + room.h - 1:
                grid.tile_map[row][col] = 2
                if row +1 < length:
                    grid.tile_map[row+1][col] = 3
            
            if col == room.x + room.w - 1:
                grid.tile_map[row][col] = 2
                if col+1  < width:
                    grid.tile_map[row][col+1] = 3





class Grid():
    def __init__(self, width, length):
        self.tile_map = [[0 for _ in range(width)] for _ in range(length)]
    def check_if_empty(self, x, y):
        if self.tile_map[x][y] == 0:
            return True
        else:
            return False

def create_rooms(grid):
    room_current_amount = 0
    while room_current_amount < room_amount:
        w, h = random.randint(4, 8), random.randint(4, 8)
        x, y = random.randint(0, width - w), random.randint(0, length - h)
        my_room = Room(x, y, w, h)

        carve_room(grid, my_room)
        room_current_amount+=1

def main():
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_length))
    grid = Grid(width, length)

    create_rooms(grid)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        screen.fill((0, 0, 0))

        for row in range(length):
            for col in range(width):
                color = void_col
                if grid.tile_map[row][col] == 1: color = floor_col
                if grid.tile_map[row][col] == 2: color = wall_col
                if grid.tile_map[row][col] == 3: color = added_space_col
                
                pygame.draw.rect(screen, color, 
                                 (col * tile_size, row * tile_size, tile_size - 1, tile_size - 1))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()