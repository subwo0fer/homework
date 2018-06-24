import pygame
from settings import *
import random

class Wood(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('pictures/wood (2).png')
        self.rect = self.image.get_rect()

        self.rect.centerx = random.randint(1, WORLD_H)
        self.rect.bottom = random.randint(1, WORLD_W)

class Rock(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('pictures/rock (1).png')
        self.rect = self.image.get_rect()

        self.rect.centerx = random.randint(1, WORLD_H)
        self.rect.bottom = random.randint(1, WORLD_W)

class Flint(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('pictures/flint (1).png')
        self.rect = self.image.get_rect()

        self.rect.centerx = random.randint(1, WORLD_H)
        self.rect.bottom = random.randint(1, WORLD_W)
