#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import win_width, win_height
from code.menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(win_width, win_height))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass



