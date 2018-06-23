import pygame
from settings import *

class Background(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.image = pygame.image.load('pictures/background.png')
        self.rect = self.image.get_rect()

        self.rect.bottom = 1000
