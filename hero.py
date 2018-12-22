import pygame
class Hero():
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load('hero.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = 200
        self.rect.centery = 200
        self.orientation = 'left'
        self.move = False
        self.speed = 1
    def ltie(self):
     if (self.orientation =='left' and self.move):
         self.rect.centerx -= self.speed
     elif (self.orientation == 'right' and self.move):
         self.rect.centerx += self.speed
     elif (self.orientation == 'up' and self.move):
         self.rect.centery -= self.speed
     elif (self.orientation == 'down' and self.move):
         self.rect.centery += self.speed
     self.screen.blit(self.image, self.rect)
