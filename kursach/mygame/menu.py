from abc import ABCMeta, abstractmethod
import pygame
import time
from buildings import *
from settings import *

class ShowInventoryCommand(object):

    def __init__(self, player, screen):
        self.player = player
        self.screen = screen
        self.drawing = False

    def execute(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_i]:
            if self.drawing == False:
                self.drawing = True
                time.sleep(0.2)

            else:
                self.drawing = False
                time.sleep(0.2)

        if self.drawing:

            self.player.sort_inventory()
            self.player.show_inventory().draw(self.screen)


class ShowBuildingsMenuCommand(object):


    def __init__(self, screen):
        self.screen = screen
        self.drawing = False
        self.drawing_info = False
        self.buildings = pygame.sprite.Group()
        self.buildings.add(Wall(34, 60))
        self.buildings.add(Fire(34, 100))


    def execute(self, mouse_point):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_b]:
            if self.drawing == False:
                self.drawing = True
                time.sleep(0.2)
            else:
                self.drawing = False
                time.sleep(0.2)

        if self.drawing:
            self.buildings.draw(self.screen)

            for i, building in enumerate(self.buildings):

                if building.rect.collidepoint(mouse_point):
                    if i == 0:
                        self.screen.blit(pygame.image.load('pictures/wall_info.png'), mouse_point)
                    if i == 1:
                        self.screen.blit(pygame.image.load('pictures/fire_info.png'), mouse_point)
                    return building