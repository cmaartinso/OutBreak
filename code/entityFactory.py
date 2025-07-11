#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import win_width
from code.background import Background
from code.player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'level1bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'level1bg{i}', (0, 0)))
                    list_bg.append(Background(f'level1bg{i}', (win_width, 0)))
                return list_bg
            case 'Player1':
                return Player('Player1',(10,340))
            case 'Player2':
                return Player('Player2', (15, 360))


