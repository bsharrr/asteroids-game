import pygame 
from constants import *


def main():
    pygame.init()
    game_window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(game_window, color="black", rect=None, special_flags=0)
        pygame.display.flip()



if __name__=="__main__":
    main()