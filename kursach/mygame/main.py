import pygame
import sys

from pygame import *
from settings import *
from player import Player
from background import Background
from resources import Wood, Rock, Flint
from menu import *

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
flints = pygame.sprite.Group()
buildings = pygame.sprite.Group()

# Menu
show_inventory = ShowInventoryCommand(player, screen)
show_buildings_menu = ShowBuildingsMenuCommand(screen)

# fill objects



# fill groups
for i in range(10):
    woods.add(Wood())

for i in range(10):
    rocks.add(Rock())

for i in range(10):
    flints.add(Flint())



def main():
    mouse_point = (0, 0)
    while True:
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit(0)
            elif e.type == pygame.MOUSEBUTTONDOWN:
                mouse_point = pygame.mouse.get_pos()
                #print(mouse_point)

        #print(mouse_point)
        screen.fill(GREEN)

        player.update()
        player.collide(woods)
        player.collide(rocks)
        player.collide(flints)
        player.collide(buildings)

        player.gather_resource(woods)
        player.gather_resource(rocks)
        player.gather_resource(flints)

        pygame.sprite.spritecollideany(player, woods)
        pygame.sprite.spritecollideany(player, rocks)
        pygame.sprite.spritecollideany(player, flints)
        pygame.sprite.spritecollideany(player, buildings)

        screen.blit(background.image, background.rect)
        screen.blit(player.image, player.rect)

        woods.draw(screen)
        rocks.draw(screen)
        flints.draw(screen)
        buildings.draw(screen)

        show_inventory.execute()
        what_to_build = show_buildings_menu.execute(mouse_point)

        if what_to_build:
            asd = what_to_build



        if mouse_point[0] in range(player.rect[0] - 100, player.rect[0] + 100):
            if mouse_point[1] in range(player.rect[1] - 100, player.rect[1] + 100):
                player.build_some(asd, mouse_point, buildings)
                #print('Сработала постройка')
                asd = None





        pygame.display.flip()
        clock.tick(20)

main()
