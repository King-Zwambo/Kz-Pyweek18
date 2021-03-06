#!/usr/bin/python
import math
import pygame
from pygame.locals import *
from sys import exit
from .utilities.audio import *
from .utilities.image import *
from .utilities.strip import *

try:
    import android
except ImportError:
    android = None

def get_color(color):
    try:
        return pygame.color.Color(color)
    except ValueError:
        return color

class Engine(object):
    def __init__(self,
                 color='white',
                 font=None,
                 font_size=22,
                 FPS=32,
                 size=(800,480)):

        pygame.init()
        pygame.display.init()

        #=======================================================
        # Cross-platform Support
        #=======================================================
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

        #=======================================================
        # Attributes
        #=======================================================
        self.x = 0
        self.y = 0
        self.font = pygame.font.Font(font, font_size)
        self.color = get_color(color)
        self.black = get_color('black')
        self.width = self.window.get_width()
        self.height = self.window.get_height()
        self.alpha = 255
        self.mouse = (0, 0)
        self.touch = False
        self.clock = pygame.time.Clock()
        self.FPS = FPS
        
        self.audio = Audio()
        self.image = Image()
        self.strip = Stripify()

    def clear(self):
        self.window.fill(self.black)
    
    def update(self):
        if android:
            self.mouse = (0, 0)
            if android.check_pause():
                android.wait_for_resume()
        else:
            if pygame.mouse.get_pressed()[0]:
                self.mouse = pygame.mouse.get_pos()
            else:
                self.mouse = (0, 0)

        pygame.display.flip()
        self.clock.tick(self.FPS)

    def touching(self):
        return self.mouse != (0, 0)

    def back(self):
        for event in pygame.event.get():
            if (event.type == QUIT or
                event.type == KEYDOWN and event.key == K_ESCAPE):
                return True
            else:
                return False

    def stop(self):
        for event in pygame.event.get():
            if (event.type == QUIT or
                event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                exit()

    def get_sound(self, pathfile):
        return self.audio.sound(pathfile)

    def play_sound(self, sound):
        self.audio.play(sound)

    def get_music(self, pathfile):
        self.audio.music(pathfile)
        return None
        
    def play_music(self, music=None):
        self.audio.loop()
        
    def get_image(self, name, pathfile, alpha=True):
        self.image.load(name, pathfile, alpha)
        self.image.scale(name, self.SW, self.SH)
        return self.image.get_image(name)

    def render_image(self, img, position=(0,0)):
        self.window.blit(img, (position[0] * self.SW, position[1] * self.SH))

    def get_strip(self,
                  name,
                  pathfile,
                  quantity,
                  horizontal=True,
                  alpha=True,
                  seconds=0.75):
        
        self.strip.load(name,
                        pathfile,
                        quantity,
                        horizontal,
                        alpha,
                        self.SW,
                        self.SH)
        
        return Strip(self.window, self.strip.get_strip(name), seconds, self.FPS)

    def render_strip(self, strip, position=(0,0)):
        strip.render((position[0] * self.SW, position[1] * self.SH))    






















            
     
            
    
