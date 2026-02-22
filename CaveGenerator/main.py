"""Main module to run the application"""
import pygame


import config
from rooms import create_rooms, Grid
from bowyer_watson import bowyer_watson
from prims import prims
from a_star import starter

def default_config():
    """Changes config back to default"""
    config.ROOM_AMOUNT = 10
    config.WIDTH = 100
    config.LENGTH = 75
    config.MOUNTAINS = 3


def input_user_values(user_width, user_length, user_room_amount, mountains_amount):
    """Changes config based on inputted values"""
    if user_room_amount < user_width*user_length/3:
        config.WIDTH = max(20, user_width)
        config.LENGTH = max(20, user_length)
        config.ROOM_AMOUNT = max(3, user_room_amount)
        config.MOUNTAINS = mountains_amount
        config.SCREEN_WIDTH = config.WIDTH*config.TILE_SIZE
        config.SCREEN_LENGTH = config.LENGTH*config.TILE_SIZE
    else:
        default_config()
        print("Too many rooms using defaults!")

def height_to_color(height):
    """Returns the color associated with height"""
    height = max(0.0, min(0.9, height))

    return (255*height, 255*height, 255*height)



def main():
    """Performs running the application"""
    stage = 0
    done = True
    #First we get user inputs.
    points = []
    connections = None
    input_mode = True
    while input_mode:
        input_error = False
        try:
            text = "Width between 20 and 100 as an integer: "
            user_width = int(input(text))
            text = "Length between 20 and 100 as an integer: "
            user_length = int(input(text))
            text ="Amount ofRooms as an integer >=3. Grid size must be big enough for the rooms: "
            user_room_count = int(input(text))
            text ="Amount of Mountains as an integer: "
            mountains_amount = int(input(text))
        except ValueError:
            print("Invalid input!")
            input_error = True
        input_mode = False
        if not input_error:
            #Most of the logic is done here
            input_user_values(user_width, user_length, user_room_count, mountains_amount)

            grid = Grid(config.WIDTH, config.LENGTH, config.MOUNTAINS)
            print("Use the space bar to view the generation in stages!")
            input_mode = False
            break



    #Then we move to the game.
    pygame.font.init()
    pygame.init()
    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_LENGTH))

    image = pygame.Surface(screen.get_size())

    image.fill((0, 0, 0))
    speed = 3
    offset_y = 0
    offset_x = 0
    running = True
    while running:
        #Adding ability to view cave generation step by step
        if not done:
            values = draw_in_stages(stage, image, grid, points, connections)
            image, grid, points, connections = values
            done = True
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w]:
            offset_y += speed
        if keys_pressed[pygame.K_s]:
            offset_y -= speed
        if keys_pressed[pygame.K_a]:
            offset_x += speed
        if keys_pressed[pygame.K_d]:
            offset_x -= speed

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if stage < 5:
                        stage += 1
                        done = False
        screen.blit(image, (offset_x, offset_y))

        pygame.display.flip()

    pygame.quit()

def draw_in_stages(stage, image, grid, points, connections):
    """Generates and draws in stages"""
    match stage:
        case 1:
            image.fill((0, 0, 0))
            points = create_rooms(grid, config.ROOM_AMOUNT)

            draw_grid(image, grid)
            draw_center_points(image, points)
            return image, grid, points, None
        case 2:
            image.fill((0, 0, 0))
            connections = bowyer_watson(points, config.WIDTH, config.LENGTH)

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
            starter(connections, config.LENGTH, config.WIDTH, grid)

            draw_grid(image, grid)
            draw_center_points(image, points)
            draw_room_connections(image, connections)
            return image, grid, points, connections
        case 5:
            image.fill((0, 0, 0))
            draw_grid(image, grid)
            return image, grid, points, connections




def draw_grid(screen, grid):
    """Draws the grid on to image"""
    for row in range(config.LENGTH):
        for col in range(config.WIDTH):
            color = config.VOID_COL

            if grid.tile_map[row][col] < 1:
                color = height_to_color(grid.tile_map[row][col])
            if grid.tile_map[row][col] == 1:
                color = config.FLOOR_COL
            if grid.tile_map[row][col] == 2:
                color = config.WALL_COL
            if grid.tile_map[row][col] == 4:
                color = config.ROUTE_COL
            if grid.tile_map[row][col] == 5:
                color = config.ROUTE_WORN_COL
            if grid.tile_map[row][col] == 6:
                color = config.ROUTE_2XWORN_COL

            rect = (col * config.TILE_SIZE,
                    row * config.TILE_SIZE,
                    config.TILE_SIZE,
                    config.TILE_SIZE)
            pygame.draw.rect(screen, color, rect)


def draw_center_points(screen, points):
    """Draws centerpoints of rooms"""
    if points != []:
        for p in points:
            pos_x = (p[0] * config.TILE_SIZE) + config.TILE_SIZE/2
            pos_y = (p[1] * config.TILE_SIZE) + config.TILE_SIZE/2
            pygame.draw.circle(screen, (255, 0, 0), (pos_x, pos_y), 4)

def draw_room_connections(screen, connections):
    """Draws connections between centerpoints"""
    if connections is not None:
        for conn in connections:
            p1, p2 = conn

            start_pos = (p1[0] * config.TILE_SIZE + config.TILE_SIZE / 2,
                        p1[1] * config.TILE_SIZE + config.TILE_SIZE / 2)

            end_pos = (p2[0] * config.TILE_SIZE + config.TILE_SIZE / 2,
                       p2[1] * config.TILE_SIZE + config.TILE_SIZE / 2)

            pygame.draw.line(screen, (255, 255, 0), start_pos, end_pos, 1)




if __name__ == "__main__":
    main()
