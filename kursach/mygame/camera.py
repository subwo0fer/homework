import pygame
from settings import *
from pygame import *


class Camera(object):

    def __init__(self, width, height):
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_configure(self.state, target.rect)

    def camera_configure(self, camera, target_rect):
        l, t, _, _ = target_rect 
        _, _, w, h = camera
        l, t = - l + WIDTH / 2, - t + HEIGHT / 2

        l = min(0, l)
        l = max(- (camera.width - WIDTH), l)
        t = max(- (camera.height - HEIGHT), t)
        t = min(0, t)

        return Rect(l, t, w, h)
