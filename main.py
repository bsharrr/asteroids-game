import pygame 
from constants import *


def main():
    #Setup pygame window
    pygame.init()
    game_window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Setup the game FPS
    game = pygame.time.Clock()
    dt = 0
    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(game_window, color="black", rect=None, special_flags=0)
        pygame.display.flip()
        game.tick(60)
        dt = game.tick(60) / 1000



if __name__=="__main__":
    main()