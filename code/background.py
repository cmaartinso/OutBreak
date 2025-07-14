#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import win_width, entity_speed
from code.entity import Entity


class Background(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= entity_speed[self.name]
        if self.rect.right <= 0:
            self.rect.left = win_width
