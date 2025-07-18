#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.Const import entity_speed, win_width, win_height, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, ENTITY_SHOT_DELAY
from code.PlayerShot import PlayerShot

from code.entity import Entity


class Player(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= entity_speed[self.name]
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < win_height:
            self.rect.centery += entity_speed[self.name]
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= entity_speed[self.name]
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < win_width:
            self.rect.centerx += entity_speed[self.name]
            pass

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            pressed_key = pygame.key.get_pressed()
            if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
                return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx + 20, self.rect.centery - 10))
            else:
                return None
        else:
            return None
