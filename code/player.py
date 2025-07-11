#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.Const import entity_speed, win_width, win_height
from code.entity import Entity


class Player(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP] and self.rect.top > 0:
            self.rect.centery -= entity_speed[self.name]
        if pressed_key[pygame.K_DOWN] and self.rect.bottom < win_height:
            self.rect.centery += entity_speed[self.name]
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= entity_speed[self.name]
        if pressed_key[pygame.K_RIGHT] and self.rect.right < win_width:
            self.rect.centerx += entity_speed[self.name]

        pass
