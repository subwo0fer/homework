import pygame
from settings import WORLD_H, WORLD_W
import random

class Enemy(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.image = pygame.Surface((34, 34))
        self.rect = self.image.get_rect()

        self.rect.centerx = random.randint(1, WORLD_H)
        self.rect.bottom = random.randint(1, WORLD_W)

        self.max_hor_speed = 3
        self.max_ver_speed = 3
        self.current_hor_speed = 0
        self.current_ver_speed = 0

        self.damage = 3

        self.attack_sound = pygame.mixer.Sound('sounds/ghost_attack.ogg')


        self.last = pygame.time.get_ticks()
        self.cooldown_attack = 1000

    def update(self, player):

        if not pygame.sprite.collide_rect(self, player):

            if (self.rect.centerx - player.rect.centerx) > 7:
                self.current_hor_speed = - self.max_hor_speed

            elif player.rect.centerx > self.rect.centerx:
                self.current_hor_speed = self.max_hor_speed
            else:
                self.current_hor_speed = 0

            if (self.rect.centery - player.rect.centery) > 7:
                self.current_ver_speed = - self.max_ver_speed

            elif player.rect.centery > self.rect.centery:
                self.current_ver_speed = self.max_ver_speed
            else:
                self.current_ver_speed = 0

        else:
            self.current_hor_speed = self.current_ver_speed = 0


        self.rect.move_ip((self.current_hor_speed, self.current_ver_speed))


    def collide(self, group_of_resource):
        for res in group_of_resource:
            if pygame.sprite.collide_rect(self, res):
                if self.current_hor_speed > 0:
                    self.rect.right = res.rect.left


                if self.current_hor_speed < 0:
                    self.rect.left = res.rect.right


                if self.current_ver_speed < 0:
                    self.rect.top = res.rect.bottom


                if self.current_ver_speed > 0:
                    self.rect.bottom = res.rect.top

    def attack(self, what_to_attack):

        now = pygame.time.get_ticks()

        if now - self.last >= self.cooldown_attack:
            if pygame.sprite.collide_circle(self, what_to_attack):
                self.last = now
                what_to_attack.health -= self.damage
                self.attack_sound.play()


class Ghost(Enemy):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('pictures/ghost.png')
        self.last = pygame.time.get_ticks()


class Wolf(Enemy):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('pictures/wolf.png')
        self.last = pygame.time.get_ticks()

        self.damage = 10
