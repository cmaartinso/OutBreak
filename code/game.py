#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import win_width, win_height, menu_option
from code.menu import Menu
from code.level import Level


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(win_width, win_height))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [menu_option[0], menu_option[1], menu_option[2]]:
                player_score = [0,0] #[Player1, Player2]
                level = Level(self.window, 'Level1', menu_return, [0,0])
                level_return = level.run(player_score)
                if level_return:
                    level = Level(self.window, 'Level2', menu_return, [0, 0])
                    level_return = level.run(player_score)

            elif menu_return == menu_option[4]:
                pygame.quit()  # Close window
                quit()  # end pygame
            else:
                pass


    