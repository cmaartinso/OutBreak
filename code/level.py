#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random

import pygame
from pygame.event import Event
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Const import c_white, win_width, menu_option, EVENT_ENEMY, SPAWN_TIME, color_green, color_cyan, EVENT_TIMEOUT, \
    TIMEOUT_STEP, TIMEOUT_LEVEL
from code.EntityMediator import EntityMediator
from code.enemy import Enemy
from code.entity import Entity
from code.entityFactory import EntityFactory
from code.player import Player


class Level:
    def __init__(self, window, name, game_mode, player_score: list[int]):
        self.player1_score = player_score[0]
        self.player2_score = player_score[1]
        self.timeout = TIMEOUT_LEVEL  # 20 segundos
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.player1_score = player_score[0] if len(player_score) > 0 else 0
        self.player2_score = player_score[1] if len(player_score) > 1 else 0
        self.entity_list: list[Entity] = []
        bg = EntityFactory.get_entity((self.name + 'Bg').lower())
        if bg:
            self.entity_list.extend([b for b in bg if b is not None])
        player = EntityFactory.get_entity('Player1')
        player.score = player_score[0]
        self.entity_list.append(player)
        if game_mode in [menu_option[1], menu_option[2]]:
            player = EntityFactory.get_entity('Player2')
            player.score = player_score[1]
            self.entity_list.append(player)
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self, player_score: list[int] ):
        if self.name.lower() == 'level2':
            pygame.mixer_music.load('./asset/level2_som.mp3')
        else:
            pygame.mixer_music.load(f'./asset/level1_som.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, Player):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if ent.name == 'Player1':
                    self.level_text(14, f'Player1 - Health: {ent.health} | Score: {ent.score}', color_green, (10, 20))
                if ent.name == 'Player2':
                    self.level_text(14, f'Player2 - Health: {ent.health} | Score: {ent.score}', color_cyan, (10, 35))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2', 'Enemy3'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player1':
                                player_score[0] = ent.score
                            if isinstance(ent, Player) and ent.name == 'Player2':
                                player_score[1] = ent.score
                        return True

            found_player = False
            for en in self.entity_list:
                if isinstance(en, Player):
                    found_player = True

            if not found_player:
                return False

            # printed text
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000: .1f}s', c_white, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', c_white, (10, 445))
            self.level_text(14, f'entidades: {len(self.entity_list)}', c_white, (10, 460))
            pygame.display.flip()
            # Collisions
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple) -> None:
        text_font: Font = pygame.font.SysFont("Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
