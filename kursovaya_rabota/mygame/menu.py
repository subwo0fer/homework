from abc import ABCMeta, abstractmethod
import pygame
import time
from buildings import Wall, Fire
from settings import HEIGHT, WIDTH

class Inventory(pygame.sprite.Sprite):

    def __init__(self, player, screen):
        super().__init__()
        self.image = pygame.image.load('pictures/inventory.png')
        self.rect = self.image.get_rect()
        self.screen = screen

        self.rect.left = 34
        self.rect.bottom = HEIGHT - 34

        self.player = player
        self.drawing = False

        self.inv = pygame.sprite.Group()

    def fill(self):
        self.inv = self.player.show_inventory()
        j = 0
        k = 0
        for i, item in enumerate(self.inv):
            if i in range(0, 6):
                item.rect.left = 40 + i * 42
                item.rect.bottom = 477
            if i in range(6, 12):
                item.rect.left = 40 + j * 42
                item.rect.bottom = 477 + 41
                j += 1
            if i in range(12, 18):
                item.rect.left = 40 + k * 42
                item.rect.bottom = 477 + 84
                k += 1


class BuildingMenu(object):

    def __init__(self, screen):
        self.screen = screen
        self.drawing = False
        self.drawing_info = False
        self.buildings = pygame.sprite.Group()
        self.buildings.add(Wall(34, 60))
        self.buildings.add(Fire(34, 130))


    def execute(self, mouse_point):

        for i, building in enumerate(self.buildings):

            if building.rect.collidepoint(mouse_point):
                if i == 0:
                    self.screen.blit(pygame.image.load('pictures/wall_info.png'), mouse_point)
                if i == 1:
                    self.screen.blit(pygame.image.load('pictures/fire_info.png'), mouse_point)
                return building
