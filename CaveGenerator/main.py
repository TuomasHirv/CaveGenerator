import pygame
from rooms import create_rooms, Grid
import config


def main():
    pygame.init()
    screen = pygame.display.set_mode((config.screen_width, config.screen_length))
    grid = Grid(config.width, config.length)

    create_rooms(grid)

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
                if grid.tile_map[row][col] == 3: color = config.added_space_col
                
                pygame.draw.rect(screen, color, 
                                 (col * config.tile_size, row * config.tile_size, config.tile_size - 1, config.tile_size - 1))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()