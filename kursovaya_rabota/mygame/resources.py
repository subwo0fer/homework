import pygame
from settings import WORLD_H, WORLD_W
import random

class Resource(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((34, 34))
        self.rect = self.image.get_rect()

        self.rect.centerx = random.randint(1, WORLD_H)
        self.rect.bottom = random.randint(1, WORLD_W)


class Wood(Resource):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('pictures/wood (2).png')

class Rock(Resource):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('pictures/rock (1).png')

class Flint(Resource):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('pictures/flint (1).png')
