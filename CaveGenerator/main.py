import pygame


import config
from rooms import create_rooms, Grid


def input_user_values(user_width, user_length, user_room_amount):
    if (user_room_amount < user_width*user_length/3):
        config.width = user_width
        config.length = user_length
        config.room_amount = user_room_amount

        config.screen_width = config.width*config.tile_size
        config.screen_length = config.length*config.tile_size
    else:
        print("Too many rooms using defaults!")


def main():
    #First we get user inputs.
    input_mode = True
    while input_mode:
        input_error = False
        try:
            user_width = int(input("Enter the grid width between 20 and 100 as an integer: "))
            user_length = int(input("Enter the grid length between 20 and 100 as an integer: "))
            user_room_count = int(input("Enter the amount of rooms as an integer. Grid size must be big enough for the rooms: "))
        except ValueError:
            print("Invalid input! Using defaults")
            input_error = True
        
        if not input_error:
            input_user_values(user_width, user_length, user_room_count)

            grid = Grid(config.width, config.length)

            if create_rooms(grid):
                print("Success!")
                input_mode = False
                
                break


    
    #Then we move to the game.
    pygame.init()
    screen = pygame.display.set_mode((config.screen_width, config.screen_length))


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        screen.fill((0, 0, 0))

        for row in range(config.length):
            for col in range(config.width):
                color = config.void_col
                if grid.tile_map[row][col] == 1: color = config.floor_col
                if grid.tile_map[row][col] == 2: color = config.wall_col
                #if grid.tile_map[row][col] == 3: color = config.added_space_col
                
                pygame.draw.rect(screen, color, 
                                 (col * config.tile_size, row * config.tile_size, config.tile_size - 1, config.tile_size - 1))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()