import pygame
from settings import *
from buildings import *
from resources import *
import pyganim
import sys

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        #self.image = pygame.image.load('pictures/player (1).png')
        #self.rect = self.image.get_rect()

        self.image = pygame.Surface((40, 56))
        self.image.fill(pygame.Color(COLOR))
        self.rect = pygame.Rect(300, 300, 40, 56)
        self.image.set_colorkey(pygame.Color(COLOR))

        self.rect.centerx = WORLD_W / 2
        self.rect.bottom = WORLD_H / 2

        self.max_hor_speed = 5
        self.max_ver_speed = 5
        self.current_hor_speed = 0
        self.current_ver_speed = 0

        self.health = 100

        self.inventory = pygame.sprite.Group()

        # анимация вверх
        boltAnim = []
        for anim in ANIMATION_UP:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimUp = pyganim.PygAnimation(boltAnim)
        self.boltAnimUp.play()

        # анимация влево
        boltAnim = []
        for anim in ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()

        # анимация вправо
        boltAnim = []
        for anim in ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()

        # анимация влево
        boltAnim = []
        for anim in ANIMATION_DOWN:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimDown = pyganim.PygAnimation(boltAnim)
        self.boltAnimDown.play()

        # анимация по умолчанию
        self.boltAnimStay = pyganim.PygAnimation(ANIMATION_STAY)
        self.boltAnimStay.play()



    def update(self, *args):

        keys = pygame.key.get_pressed()


        if keys[pygame.K_LEFT]:
            self.current_hor_speed = -self.max_hor_speed
            self.image.fill(pygame.Color(COLOR))
            self.boltAnimLeft.blit(self.image, (0, 0))

        elif keys[pygame.K_RIGHT]:
            self.current_hor_speed = self.max_hor_speed
            self.image.fill(pygame.Color(COLOR))
            self.boltAnimRight.blit(self.image, (0, 0))

        elif keys[pygame.K_UP]:
            self.current_ver_speed = - self.max_ver_speed
            self.image.fill(pygame.Color(COLOR))
            self.boltAnimUp.blit(self.image, (0, 0))

        elif keys[pygame.K_DOWN]:
            self.current_ver_speed = self.max_ver_speed
            self.image.fill(pygame.Color(COLOR))
            self.boltAnimDown.blit(self.image, (0, 0))

        else:
            self.current_hor_speed = self.current_ver_speed = 0
            self.image.fill(pygame.Color(COLOR))
            self.boltAnimStay.blit(self.image, (0, 0))

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

        #for group_of_resource in args:
            #for res in group_of_resource:
                #pass



        if self.health <= 0:
            sys.exit(0)





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
