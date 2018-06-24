import pygame
from settings import *

class Background(pygame.sprite.Sprite):

    def __init__(self, bottom, right, pic_time_of_date):

        super().__init__()

        self.image = pygame.image.load(pic_time_of_date)
        self.rect = self.image.get_rect()

        self.rect.bottom = bottom
        self.rect.left = right
