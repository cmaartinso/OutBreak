#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from pygame.font import Font

from code.Const import win_width, menu_option, c_white, color_y, color_g


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuIniciar.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        selected_option = 0
        pygame.mixer_music.load('./asset/menu_iniciar_som.mp3')
        pygame.mixer_music.play(-1)
        while True:
            # DRAW IMAGES
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "OutBreak", color_g, ((win_width / 2), 100))

            for i in range(len(menu_option)):
                if i == selected_option:
                    self.menu_text(20, menu_option[i], color_y, (win_width / 2, 300 + 30 * i))
                else:
                    self.menu_text(20, menu_option[i], c_white, (win_width / 2, 300 + 30 * i))
            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # End Pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # DOWN KEY
                        if selected_option < len(menu_option) - 1:
                            selected_option += 1
                        else:
                            selected_option = 0
                    if event.key == pygame.K_UP:  # UP KEY
                        if selected_option > 0:
                            selected_option -= 1
                        else:
                            selected_option = len(menu_option) - 1
                    if event.key == pygame.K_RETURN:  # ENTER
                        return menu_option[selected_option]

    def menu_text(self, text_size: int, text, text_color: tuple, text_center_pos: tuple):
        text_font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)
        text = str(text)  # string
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)
