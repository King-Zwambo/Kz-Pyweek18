import pygame
from pygame.locals import *

class Image(object):
    def __init__(self):
        self.images = {}

    def load(self, name, pathfile, alpha=True):
        if alpha == True:
            img = pygame.image.load(pathfile).convert_alpha()
        else:
            img = pygame.image.load(pathfile).convert()

        self.images.update({name:img})
        
    def scale(self, name, SW=1, SH=1):
        img = self.images[name]
        self.images[name] = pygame.transform.scale(img,
                                                   (int(img.get_width()*SW),
                                                    int(img.get_height()*SH)))

    def get_image(self, name):
        return self.images[name]
