import pygame
from settings import *
from buildings import *
from resources import *

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('pictures/player.jpg')
        self.rect = self.image.get_rect()

        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT / 2

        self.max_hor_speed = 10
        self.max_ver_speed = 10
        self.current_hor_speed = 0
        self.current_ver_speed = 0

        self.inventory = pygame.sprite.Group()

    def update(self, *args):

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

        if self.current_hor_speed > 0:
            if self.rect.right > WORLD_H - 10:
                self.current_hor_speed = 0

        if self.current_hor_speed < 0:
            if self.rect.left < 0:
                self.current_hor_speed = 0

        if self.current_ver_speed > 0:
            if self.rect.bottom > WORLD_W - 10:
                self.current_ver_speed = 0

        if self.current_ver_speed < 0:
            if self.rect.top < 0:
                self.current_ver_speed = 0

        for group_of_resource in args:
            for res in group_of_resource:
                pass









        self.rect.move_ip((self.current_hor_speed, self.current_ver_speed))
        #self.rect.move_ip((0, self.current_ver_speed))




    def collide(self, group_of_resource):
        for res in group_of_resource:
            if pygame.sprite.collide_rect(self, res):


                if self.current_hor_speed > 0 and self.current_ver_speed < 0:
                    self.rect.top = res.rect.bottom
                    return
                    # ВВЕРХ И ВПРАВО

                if self.current_hor_speed < 0 and self.current_ver_speed < 0:
                    self.rect.top = res.rect.bottom
                    return
                    # ВВЕРХ И ВЛЕВО

                if self.current_hor_speed > 0 and self.current_ver_speed > 0:
                    self.rect.bottom = res.rect.top
                    return
                    # ВНИЗ И ВПРАВО

                if self.current_hor_speed < 0 and self.current_ver_speed > 0:
                    self.rect.bottom = res.rect.top
                    return
                    # ВНИЗ И ВЛЕВО



                if self.current_hor_speed > 0:
                    self.rect.right = res.rect.left


                if self.current_hor_speed < 0:
                    self.rect.left = res.rect.right


                if self.current_ver_speed < 0:
                    self.rect.top = res.rect.bottom


                if self.current_ver_speed > 0:
                    self.rect.bottom = res.rect.top


    def gather_resource(self, group_of_resource):

        for res in group_of_resource:
            if pygame.sprite.collide_circle(self, res):
                keys = pygame.key.get_pressed()

                if keys[pygame.K_q]:
                    if len(self.inventory) < 18:
                        self.inventory.add(res)
                        group_of_resource.remove(res)
                    else:
                        print('ИНВЕНТАРЬ ПОЛОН')

    def sort_inventory(self):
        for i, item in enumerate(self.inventory):
            item.rect.centery = 670

            item.rect.centerx = i * 38 + 100

    def show_inventory(self):
        return self.inventory

    def build_some(self, what_to_build, where, buildings):

        if type(what_to_build) == Wall:
            bufer = 0
            bufer_del = 2
            for item in self.inventory:
                if type(item) == Rock:
                    bufer += 1
            if bufer >= 2:
                buildings.add(Wall(where[0], where[1] + 17))

                for item in self.inventory:
                    if type(item) == Rock and bufer_del > 0:
                        self.inventory.remove(item)
                        bufer_del -= 1



        if type(what_to_build) == Fire:
            count_woods = 0
            count_flints = 0
            count_del_woods = 3
            count_del_flints = 1

            for item in self.inventory:
                if type(item) == Wood:
                    count_woods += 1
                if type(item) == Flint:
                    count_flints += 1

            if count_woods >= 2 and count_flints >= 1:
                buildings.add(Fire(where[0], where[1] + 17))

                for item in self.inventory:
                    if type(item) == Wood and count_del_woods > 0:
                        self.inventory.remove(item)
                        count_del_woods -= 1

                    if type(item) == Flint and count_del_flints > 0:
                        self.inventory.remove(item)
                        count_del_flints -= 1






"""
class Inventory(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((340, 34))
        self.image.fill(BLUE)
        self.rect = pygame.Rect(30, 600, 340, 34)
"""
