import pygame
import sys

from pygame import *
from settings import *
from player import Player
from background import Background
from resources import Wood, Rock, Flint
from menu import *
from camera import *


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



# fill objects



# fill groups
for i in range(10):
    woods.add(Wood())

for i in range(10):
    rocks.add(Rock())

for i in range(10):
    flints.add(Flint())

# camera
camera = Camera(camera_configure, WORLD_W, WORLD_H)

# Menu
show_inventory = ShowInventoryCommand(player, screen)
show_buildings_menu = ShowBuildingsMenuCommand(screen)


def main():
    asd = None
    mouse_point = (0, 0)
    mouse_point_in_world = [0, 0]
    inventory_bool = False
    build_bool = False
    what_to_build = None
    while True:
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit(0)
            elif e.type == pygame.MOUSEBUTTONDOWN:
                mouse_point = pygame.mouse.get_pos()
                mouse_point_in_world[0] = mouse_point[0] - camera.state[0]
                mouse_point_in_world[1] = mouse_point[1] - camera.state[1]
            elif e.type == pygame.KEYDOWN and e.key == pygame.K_i:
                if inventory_bool == False:
                    inventory_bool = True
                else:
                    inventory_bool = False
            elif e.type == pygame.KEYDOWN and e.key == pygame.K_b:
                if build_bool == False:
                    build_bool = True
                else:
                    build_bool = False



        screen.fill(GREEN)

        player.update(woods, rocks, flints, buildings)


        player.collide(woods)
        player.collide(rocks)
        player.collide(flints)
        player.collide(buildings)
        

        player.gather_resource(woods)
        player.gather_resource(rocks)
        player.gather_resource(flints)

        """
        pygame.sprite.spritecollideany(player, woods)
        pygame.sprite.spritecollideany(player, rocks)
        pygame.sprite.spritecollideany(player, flints)
        pygame.sprite.spritecollideany(player, buildings)
        """

        camera.update(player)
        screen.blit(background.image, camera.apply(background))
        screen.blit(player.image, camera.apply(player))

        for w in woods:
            screen.blit(w.image, camera.apply(w))
        for r in rocks:
            screen.blit(r.image, camera.apply(r))
        for f in flints:
            screen.blit(f.image, camera.apply(f))
        for b in buildings:
            screen.blit(b.image, camera.apply(b))

        #rocks.draw(screen)
        #flints.draw(screen)
        #buildings.draw(screen)

        if inventory_bool:
            screen.blit(show_inventory.image, show_inventory.rect)
            show_inventory.fill()
            show_inventory.inv.draw(screen)

        if build_bool:
            for item in show_buildings_menu.buildings:
                screen.blit(item.image, item.rect)
            what_to_build = show_buildings_menu.execute(mouse_point)


        if what_to_build:
            asd = what_to_build



        if mouse_point_in_world[0] in range(player.rect[0] - 100, player.rect[0] + 100):
            if mouse_point_in_world[1] in range(player.rect[1] - 100, player.rect[1] + 100):
                player.build_some(asd, mouse_point_in_world, buildings)
                #print('Сработала постройка')
                asd = None






        pygame.display.flip()
        clock.tick(30)

main()
