import pygame 
from constants import *
from player import Player

def main():
    #Setup pygame window
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Setup the game FPS
    game = pygame.time.Clock()
    dt = 0

    # Instantiate a player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    # Game Loop
    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        
        dt = game.tick(60) / 1000



if __name__=="__main__":
    main()