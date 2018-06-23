import pygame
from settings import *
import random

class Wood(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('pictures/wood (2).png')
        self.rect = self.image.get_rect()

        self.rect.centerx = random.randint(1, 900)
        self.rect.bottom = random.randint(1, 600)

class Rock(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('pictures/rock (1).png')
        self.rect = self.image.get_rect()

        self.rect.centerx = random.randint(1, 900)
        self.rect.bottom = random.randint(1, 600)

class Flint(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('pictures/flint (1).png')
        self.rect = self.image.get_rect()

        self.rect.centerx = random.randint(1, 900)
        self.rect.bottom = random.randint(1, 600)
