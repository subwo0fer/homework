import pygame
from settings import *
import random

class Wood(pygame.sprite.Sprite):

    def __init__(self):
        super(Wood, self).__init__()

        self.image = pygame.image.load('pictures/wood.jpg')
        self.rect = self.image.get_rect()

        self.rect.centerx = random.randint(1, WIDTH)
        self.rect.bottom = random.randint(1, HEIGHT)

class Rock(pygame.sprite.Sprite):

    def __init__(self):
        super(Rock, self).__init__()

        self.image = pygame.image.load('pictures/rock.jpg')
        self.rect = self.image.get_rect()

        self.rect.centerx = random.randint(1, WIDTH)
        self.rect.bottom = random.randint(1, HEIGHT)


