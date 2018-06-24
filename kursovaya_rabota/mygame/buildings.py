import pygame
from settings import *

class Wall(pygame.sprite.Sprite):

    def __init__(self, cent, bott):
        super().__init__()

        self.image = pygame.image.load('pictures/wall.jpg')
        self.rect = self.image.get_rect()

        self.rect.centerx = cent
        self.rect.bottom = bott

        self.health = 100

        #self.requirenments = {'rock':2}

    def update(self):
        if self.health <= 0:
            self.kill()

class Fire(pygame.sprite.Sprite):

    def __init__(self, cent, bott):
        super().__init__()

        self.image = pygame.image.load('pictures/fire(1).png')
        self.rect = self.image.get_rect()

        self.rect.centerx = cent
        self.rect.bottom = bott
        self.health = 20


    def update(self):
        if self.health <= 0:
            self.kill()
