import pygame
from settings import *

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()

        self.image = pygame.image.load('pictures/player.jpg')
        self.rect = self.image.get_rect()

        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT / 2

        self.max_hor_speed = 5
        self.max_ver_speed = 5
        self.current_hor_speed = 0
        self.current_ver_speed = 0

        self.inventory = pygame.sprite.Group()

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.current_hor_speed = -self.max_hor_speed
        elif keys[pygame.K_RIGHT]:
            self.current_hor_speed = self.max_hor_speed
        elif keys[pygame.K_UP]:
            self.current_ver_speed = - self.max_ver_speed
        elif keys[pygame.K_DOWN]:
            self.current_ver_speed = self.max_ver_speed

        else:
            self.current_hor_speed = self.current_ver_speed = 0

        self.rect.move_ip((self.current_hor_speed, 0))
        self.rect.move_ip((0, self.current_ver_speed))

    def collide(self, group_of_resource):
        for res in group_of_resource:
            if pygame.sprite.collide_rect(self, res):

                if self.current_hor_speed > 0:
                    self.rect.right = res.rect.left
                    #self.current_hor_speed = self.current_ver_speed = 0

                if self.current_hor_speed < 0:
                    self.rect.left = res.rect.right
                    #self.current_hor_speed = self.current_ver_speed = 0

                if self.current_ver_speed < 0:
                    self.rect.top = res.rect.bottom
                    #self.current_hor_speed = self.current_ver_speed = 0

                if self.current_ver_speed > 0:
                    self.rect.bottom = res.rect.top
                    #self.current_hor_speed = self.current_ver_speed = 0

    def gather_resource(self, group_of_resource):

        for res in group_of_resource:
            if pygame.sprite.collide_circle(self, res):
                keys = pygame.key.get_pressed()

                if keys[pygame.K_q]:
                    self.inventory.add(res)
                    group_of_resource.remove(res)

    def sort_inventory(self):

        for i, item in enumerate(self.inventory):
            item.rect.centery = 670

            item.rect.centerx = i * 38 + 100

    def show_inventory(self):
        return self.inventory





"""
class Inventory(pygame.sprite.Sprite):

    def __init__(self):
        super(Inventory, self).__init__()

        self.image = pygame.Surface((340, 34))
        self.image.fill(BLUE)
        self.rect = pygame.Rect(30, 600, 340, 34)
"""
