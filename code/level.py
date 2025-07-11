#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Const import c_white, win_width, menu_option
from code.entity import Entity
from code.entityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 20000  # 20 segundos
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('level1bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        if game_mode in [menu_option[1], menu_option[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))

    def run(self):
        pygame.mixer_music.load(f'./asset/level1_som.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # printed text
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000: .1f}s', c_white, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', c_white, (10, 445))
            self.level_text(14, f'entidades: {len(self.entity_list)}', c_white, (10, 460))
            pygame.display.flip()
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont("Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
