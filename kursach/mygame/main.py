import pygame
import sys

from pygame import *
from settings import *
from player import Player
from background import Background
from resources import Wood, Rock

pygame.init()
pygame.display.set_caption('MyBeautyGame')

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# Objects
player = Player()
background = Background()

# Groups
woods = pygame.sprite.Group()
rocks = pygame.sprite.Group()

# fill objects



# fill groups
for i in range(10):
    woods.add(Wood())

for i in range(10):
    rocks.add(Rock())



def main():
    while True:
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit(0)

        screen.fill(GREEN)

        player.update()
        player.collide(woods)
        player.collide(rocks)
        player.gather_resource(woods)
        player.gather_resource(rocks)

        pygame.sprite.spritecollideany(player, woods)
        pygame.sprite.spritecollideany(player, rocks)

        screen.blit(background.image, background.rect)
        screen.blit(player.image, player.rect)

        woods.draw(screen)
        rocks.draw(screen)

        player.sort_inventory()

        pygame.display.flip()
        clock.tick(60)

main()