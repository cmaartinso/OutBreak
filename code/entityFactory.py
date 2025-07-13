#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Const import win_width
from code.background import Background
from code.enemy import Enemy
from code.player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'level1bg':
                list_bg = []
                for i in range(7): # level1bg images number
                    list_bg.append(Background(f'level1bg{i}', (0, 0)))
                    list_bg.append(Background(f'level1bg{i}', (win_width, 0)))
                return list_bg
            case 'level2bg':
                list_bg = []
                for i in range(7): # level2bg images number
                    list_bg.append(Background(f'level2bg{i}', (0, 0)))
                    list_bg.append(Background(f'level2bg{i}', (win_width, 0)))
                return list_bg
            case 'Player1':
                return Player('Player1',(10,340))
            case 'Player2':
                return Player('Player2', (15, 370))
            case 'Enemy1':
                return Enemy('Enemy1', (win_width + 10, random.randint(320,400)))
            case 'Enemy2':
                return Enemy('Enemy2', (win_width + 10, random.randint(320, 400)))
            case 'Enemy3':
                return Enemy('Enemy3', (win_width + 10, random.randint(320, 400)))
