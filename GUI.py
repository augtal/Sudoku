import pygame
import sys
import random

window_WIDTH, window_HEIGHT = 800, 600
screen = pygame.display.set_mode((window_WIDTH, window_HEIGHT))
pygame.display.set_caption("Sudoku")
screen.fill((255, 255, 255))

def main():
    pygame.init()

    run = True
    fps = 30
    clock = pygame.time.Clock()

    while run:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        pygame.display.update()

if __name__=='__main__':
    main()