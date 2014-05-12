#!/usr/bin/python
import math
import pygame
from pygame.locals import *
from sys import exit

try:
    import android
except ImportError:
    android = None

class Engine(object):
    def __init__(self,
                 color='white',
                 font=None,
                 font_size=22,
                 FPS=32,
                 size=(800,480)):
        
        pygame.init()
        pygame.display.init()
        
        try:
            info = pygame.display.Info()        
            diag = math.hypot(info.current_w,
                              info.current_h) / android.get_dpi()
            
            width, height = (info.current_w, info.current_h)
            self.SW = width  / size[0]
            self.SH = height / size[1]
            self.window = pygame.display.set_mode((width, height))

        except AttributeError:
            self.window = pygame.display.set_mode(size)
            self.SW = 1
            self.SH = 1

        if android:
            android.init()
            android.map_key(android.KEYCODE_BACK, pygame.K_ESCAPE)
     
            
    
