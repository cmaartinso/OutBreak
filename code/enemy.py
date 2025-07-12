#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import entity_speed, win_width
from code.entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        self.rect.centerx -= entity_speed[self.name]


