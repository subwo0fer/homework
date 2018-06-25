import pygame
from resources import Flint, Wood, Rock

class Building(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((34, 34))
        self.rect = self.image.get_rect()

        self.health = 100

    def update(self):
        if self.health <= 0:
            self.kill()


class Wall(Building):
    def __init__(self, cent, bott):
        super().__init__()

        self.image = pygame.image.load('pictures/wall.jpg')

        self.rect.centerx = cent
        self.rect.bottom = bott

        self.requirenments = {Rock: 2}

class Fire(Building):
    def __init__(self, cent, bott):
        super().__init__()

        self.image = pygame.image.load('pictures/fire(1).png')
        self.rect = self.image.get_rect()

        self.rect.centerx = cent
        self.rect.bottom = bott

        self.health = 20

        self.requirenments = {Wood: 3, Flint: 1}
