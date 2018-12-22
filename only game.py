import sys
import pygame
from design.hero import Hero
def run_game():
  pygame.init()
  screen = pygame.display.set_mode((400,400))
  pygame.display.set_caption('Game')
  hero = Hero(screen)
  while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                hero.orientation = 'left'
                hero.move = True
            elif event.key == pygame.K_RIGHT:
                hero.orientation = 'right'
                hero.move = True
            if event.key == pygame.K_UP:
                hero.orientation = 'up'
                hero.move = True
            if event.key == pygame.K_DOWN:
                hero.orientation = 'down'
                hero.move = True
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT,pygame.K_UP, pygame.K_DOWN]:
                hero.move = False
    hero.ltie()
    pygame.display.flip()


run_game()

