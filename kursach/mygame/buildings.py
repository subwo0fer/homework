import pygame
from settings import *

class Wall(pygame.sprite.Sprite):

    def __init__(self, cent, bott):
        super().__init__()

        self.image = pygame.image.load('pictures/wall.jpg')
        self.rect = self.image.get_rect()

        self.rect.centerx = cent
        self.rect.bottom = bott

        self.requirenments = {'rock':2}

class Fire(pygame.sprite.Sprite):

    def __init__(self, cent, bott):
        super().__init__()

        self.image = pygame.image.load('pictures/fire(1).png')
        self.rect = self.image.get_rect()

        self.rect.centerx = cent
        self.rect.bottom = bott
