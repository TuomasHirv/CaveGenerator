import pygame


import config
from rooms import create_rooms, create_routes, Grid
from bowyer_watson import bowyer_watson
from prims import prims
from a_star import starter

def default_config():
    config.room_amount = 10
    config.width = 100
    config.length = 75


def input_user_values(user_width, user_length, user_room_amount):
    if (user_room_amount < user_width*user_length/3):
        config.width = max(20, user_width)
        config.length = max(20, user_length)
        config.room_amount = max(3, user_room_amount)

        config.screen_width = config.width*config.tile_size
        config.screen_length = config.length*config.tile_size
    else:
        default_config()
        print("Too many rooms using defaults!")




def main():
    #First we get user inputs.
    points = []
    culled_connections = []
    input_mode = True
    while input_mode:
        input_error = False
        try:
            user_width = int(input("Enter the grid width between 20 and 100 as an integer: "))
            user_length = int(input("Enter the grid length between 20 and 100 as an integer: "))
            user_room_count = int(input("Enter the amount of rooms as an integer >=3. Grid size must be big enough for the rooms: "))
        except ValueError:
            print("Invalid input!")
            input_error = True
        
        if not input_error:
            #Most of the logic is done here
            input_user_values(user_width, user_length, user_room_count)

            grid = Grid(config.width, config.length)
            points = create_rooms(grid, config.room_amount)
            connections = bowyer_watson(points, config.width, config.length)
            culled_connections = prims(connections)
            #Below is A*
            paths = starter(culled_connections)
            create_routes(paths, grid)

            if len(points) != 0:
                print("Success!")
                input_mode = False

                break


    #Then we move to the game.
    pygame.font.init()
    pygame.init()
    screen = pygame.display.set_mode((config.screen_width, config.screen_length))


    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        draw_grid(screen, grid)

        draw_center_points(screen, points)
        
        draw_room_connections(screen, culled_connections)

        pygame.display.flip()

    pygame.quit()



def draw_grid(screen, grid):
    for row in range(config.length):
        for col in range(config.width):
            color = config.void_col
            if grid.tile_map[row][col] == 1: color = config.floor_col
            if grid.tile_map[row][col] == 2: color = config.wall_col
            if grid.tile_map[row][col] == 4: color = config.route_col
            pygame.draw.rect(screen, color, (col * config.tile_size, row * config.tile_size, config.tile_size - 1, config.tile_size - 1))


def draw_center_points(screen, points):
    for p in points:
        pos_x = (p[0] * config.tile_size) + config.tile_size/2
        pos_y = (p[1] * config.tile_size) + config.tile_size/2
        pygame.draw.circle(screen, (255, 0, 0), (pos_x, pos_y), 4)

def draw_room_connections(screen, connections):
    for conn in connections:
        p1, p2 = conn

        start_pos = (p1[0] * config.tile_size + config.tile_size / 2, p1[1] * config.tile_size + config.tile_size / 2)
        end_pos = (p2[0] * config.tile_size + config.tile_size / 2, p2[1] * config.tile_size + config.tile_size / 2)

        pygame.draw.line(screen, (255, 255, 0), start_pos, end_pos, 1)




if __name__ == "__main__":
    main()
