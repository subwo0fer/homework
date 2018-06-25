import pygame
import sys

from settings import SIZE, WORLD_H, WORLD_W, GREEN
from player import Player
from background import Background
from resources import Wood, Rock, Flint
from menu import Inventory, BuildingMenu
from camera import Camera
from enemies import Ghost, Wolf

pygame.init()
pygame.mixer.init()
pygame.display.set_caption('MyBeautyGame')

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# Objects
player = Player()

# Groups
woods = pygame.sprite.Group()
rocks = pygame.sprite.Group()
flints = pygame.sprite.Group()
buildings = pygame.sprite.Group()
background_day = pygame.sprite.Group()
background_night = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# fill groups
for i in range(1, 5):
    for j in range(4):
        background_day.add(Background(i * 1000, j * 1000, 'pictures/background.png'))

for i in range(1, 5):
    for j in range(4):
        background_night.add(Background(i * 1000, j * 1000, 'pictures/background_night.png'))

for i in range(30):
    woods.add(Wood())

for i in range(30):
    rocks.add(Rock())

for i in range(30):
    flints.add(Flint())

for i in range(15):
    enemies.add(Ghost())
    enemies.add(Wolf())


# camera
camera = Camera(WORLD_W, WORLD_H)

# Menu
inventory = Inventory(player, screen)
building_menu = BuildingMenu(screen)


def main():
    what_to_build_now = None
    mouse_point = (0, 0)
    mouse_point_in_world = [0, 0]
    inventory_bool = False
    build_bool = False
    what_to_build = None
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
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

        if pygame.time.get_ticks() // 1000 // 15 % 2 == 0:
            day = True
        else:
            day = False

        screen.fill(GREEN)

        player.update()

        player.collide(woods)
        player.collide(rocks)
        player.collide(flints)
        player.collide(buildings)


        player.gather_resource(woods)
        player.gather_resource(rocks)
        player.gather_resource(flints)

        camera.update(player)

        if day:
            for back in background_day:
                screen.blit(back.image, camera.apply(back))
        else:
            for back in background_night:
                screen.blit(back.image, camera.apply(back))

        #screen.blit(background.image, camera.apply(background))
        screen.blit(player.image, camera.apply(player))

        for w in woods:
            screen.blit(w.image, camera.apply(w))
        for r in rocks:
            screen.blit(r.image, camera.apply(r))
        for f in flints:
            screen.blit(f.image, camera.apply(f))
        for b in buildings:
            screen.blit(b.image, camera.apply(b))

        if not day:
            for b in buildings:
                b.update()
                for enemy in enemies:
                    enemy.attack(b)

            for enemy in enemies:
                screen.blit(enemy.image, camera.apply(enemy))
                enemy.attack(player)
                enemy.update(player)
                enemy.collide(buildings)

        if inventory_bool:
            screen.blit(inventory.image, inventory.rect)
            inventory.fill()
            inventory.inv.draw(screen)

        if build_bool:
            for item in building_menu.buildings:
                screen.blit(item.image, item.rect)
            what_to_build = building_menu.execute(mouse_point)

        if what_to_build:
            what_to_build_now = what_to_build

        if mouse_point_in_world[0] in range(player.rect[0] - 100, player.rect[0] + 100):
            if mouse_point_in_world[1] in range(player.rect[1] - 100, player.rect[1] + 100):
                player.build_some(what_to_build_now, mouse_point_in_world, buildings)
                what_to_build_now = None

        pygame.display.flip()
        clock.tick(30)

main()
