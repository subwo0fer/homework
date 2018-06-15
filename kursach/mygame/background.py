import pygame
from settings import *

class Background(pygame.sprite.Sprite):

    def __init__(self):

        super(Background, self).__init__()

        self.image = pygame.image.load('pictures/background.jpg')
        self.rect = self.image.get_rect()

        self.rect.bottom = HEIGHT
