from __future__ import division
import pygame
from pygame.locals import *

class Stripify(object):
    def __init__(self):
        self.images = {}

    def load(self, name, pathfile, quantity, horizontal=True, alpha=True, SW=1, SH=1):
        if alpha == True:
            img = pygame.image.load(pathfile).convert_alpha()
        else:
            img = pygame.image.load(pathfile).convert()

        img = pygame.transform.scale(img, (int(img.get_width()*SW), int(img.get_height()*SH)))

        strip = []
        if horizontal:
            width = int(img.get_width() / quantity)
            height = img.get_height()
            for i in range(quantity):
                strip.append(img.subsurface((int(img.get_width() / quantity * i), 0, width, height)))

        else:
            width = img.get_width()
            height = int(img.get_height() / quantity)
            for i in range(quantity):
                strip.append(img.subsurface((0, int(img.get_height() / quantity * i), width, height)))

        self.images.update({name: strip})
        return strip

    def get_strip(self, name):
        return self.images[name]

class Strip(object):
    def __init__(self, screen, strip, seconds=1, FPS=32):
        self.current = 0
        self.frame = 0
        self.strip = strip
        self.frames = len(strip)

        self.FPS = FPS / self.frames * seconds
        self.window = window
        self.reloop = False

        self.width = self.strip[self.frame].get_width()
        self.height = self.strip[self.frame].get_height()

    def kill(self):
        if self.reloop:
            return True
        else:
            return False

    def render(self, position=(0,0)):
        self.window.blit(self.strip[self.frame], position)
        self.current += 1
        if (self.frame + 1) * self.FPS < self.current:
            self.frame += 1
            if self.frame > self.frames-1:
                self.frame = 0
                self.current = 0
                self.reloop = True
        else:
            self.reloop = False

            
