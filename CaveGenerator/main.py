import pygame


import config
from rooms import create_rooms, Grid
from bowyer_watson import bowyer_watson
from prims import prims
from a_star import starter

def default_config():
    config.room_amount = 10
    config.width = 100
    config.length = 75
    config.mountains = 3


def input_user_values(user_width, user_length, user_room_amount, mountains_amount):
    if (user_room_amount < user_width*user_length/3):
        config.width = max(20, user_width)
        config.length = max(20, user_length)
        config.room_amount = max(3, user_room_amount)
        config.mountains = mountains_amount
        config.screen_width = config.width*config.tile_size
        config.screen_length = config.length*config.tile_size
    else:
        default_config()
        print("Too many rooms using defaults!")

def height_to_color(height):
    height = max(0.0, min(0.9, height))

    return (255*height, 255*height, 255*height)
    


def main():
    stage = 0
    done = True
    #First we get user inputs.
    points = []
    connections = None
    input_mode = True
    while input_mode:
        input_error = False
        try:
            user_width = int(input("Enter the grid width between 20 and 100 as an integer: "))
            user_length = int(input("Enter the grid length between 20 and 100 as an integer: "))
            user_room_count = int(input("Enter the amount of rooms as an integer >=3. Grid size must be big enough for the rooms: "))
            mountains_amount = int(input("Enter the amount of mountains as an integer: "))
        except ValueError:
            print("Invalid input!")
            input_error = True
        
        if not input_error:
            #Most of the logic is done here
            input_user_values(user_width, user_length, user_room_count, mountains_amount)

            grid = Grid(config.width, config.length, config.mountains)
            print("Use the space bar to view the generation in stages!")
            input_mode = False
            break

    

    #Then we move to the game.
    pygame.font.init()
    pygame.init()
    screen = pygame.display.set_mode((config.screen_width, config.screen_length))

    image = pygame.Surface(screen.get_size())

    image.fill((0, 0, 0))
    speed = 3
    offsetY = 0
    offsetX = 0
    running = True
    while running:
        #Adding ability to view cave generation step by step
        if not done:
            image, grid, points, connections = draw_in_stages(stage, image, grid, points, connections)
            done = True
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w]:
            offsetY += speed
        if keys_pressed[pygame.K_s]:
            offsetY -= speed
        if keys_pressed[pygame.K_a]:
            offsetX += speed
        if keys_pressed[pygame.K_d]:
            offsetX -= speed

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if stage < 5:
                        stage += 1
                        done = False
        screen.blit(image, (offsetX, offsetY))

        pygame.display.flip()

    pygame.quit()

def draw_in_stages(stage, image, grid, points, connections):
    match stage:
        case 1:
            image.fill((0, 0, 0))
            points = create_rooms(grid, config.room_amount)

            draw_grid(image, grid)
            draw_center_points(image, points)
            return image, grid, points, None
        case 2:
            image.fill((0, 0, 0))
            connections = bowyer_watson(points, config.width, config.length)

            draw_grid(image, grid)
            draw_center_points(image, points)
            draw_room_connections(image, connections)
            return image, grid, points, connections
        case 3:
            image.fill((0, 0, 0))
            connections = prims(connections)

            draw_grid(image, grid)
            draw_center_points(image, points)
            draw_room_connections(image, connections)
            return image, grid, points, connections
        case 4:
            image.fill((0, 0, 0))
            paths = starter(connections, config.length, config.width, grid)
            #create_routes(paths, grid)

            draw_grid(image, grid)
            draw_center_points(image, points)
            draw_room_connections(image, connections)
            return image, grid, points, connections
        case 5:
            image.fill((0, 0, 0))
            draw_grid(image, grid)
            return image, grid, points, connections




def draw_grid(screen, grid):
    for row in range(config.length):
        for col in range(config.width):
            color = config.void_col
            if grid.tile_map[row][col] < 1: color = height_to_color(grid.tile_map[row][col])
            if grid.tile_map[row][col] == 1: color = config.floor_col
            if grid.tile_map[row][col] == 2: color = config.wall_col
            if grid.tile_map[row][col] == 4: color = config.route_col
            if grid.tile_map[row][col] == 5: color = config.route_worn_col
            if grid.tile_map[row][col] == 6: color = config.route_2xworn_col
            pygame.draw.rect(screen, color, (col * config.tile_size, row * config.tile_size, config.tile_size, config.tile_size))


def draw_center_points(screen, points):
    if points != []:
        for p in points:
            pos_x = (p[0] * config.tile_size) + config.tile_size/2
            pos_y = (p[1] * config.tile_size) + config.tile_size/2
            pygame.draw.circle(screen, (255, 0, 0), (pos_x, pos_y), 4)

def draw_room_connections(screen, connections):
    if connections != None:
        for conn in connections:
            p1, p2 = conn

            start_pos = (p1[0] * config.tile_size + config.tile_size / 2, p1[1] * config.tile_size + config.tile_size / 2)
            end_pos = (p2[0] * config.tile_size + config.tile_size / 2, p2[1] * config.tile_size + config.tile_size / 2)

            pygame.draw.line(screen, (255, 255, 0), start_pos, end_pos, 1)




if __name__ == "__main__":
    main()
