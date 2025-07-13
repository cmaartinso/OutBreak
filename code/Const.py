import pygame

# C
color_g = (85, 107, 47)
c_white = (255, 255, 255)
color_y = (152, 251, 152)
color_green = (0,128,0)
color_cyan = (0,128,128)

# E
EVENT_ENEMY = pygame.USEREVENT
entity_speed = {
    'level1bg0': 0,
    'level1bg1': 1,
    'level1bg2': 2,
    'level1bg3': 3,
    'level1bg4': 4,
    'level1bg5': 3,
    'level1bg6': 5,
    'Player1': 3,
    'Player1Shot': 3,
    'Player2': 3,
    'Player2Shot': 3,
    'Enemy1': 1,
    'Enemy2': 2,
    'Enemy3':2,

}

ENTITY_HEALTH = {
    'level1bg0': 999,
    'level1bg1': 999,
    'level1bg2': 999,
    'level1bg3': 999,
    'level1bg4': 999,
    'level1bg5': 999,
    'level1bg6': 999,
    'level2bg0': 999,
    'level2bg1': 999,
    'level2bg2': 999,
    'level2bg3': 999,
    'level2bg4': 999,
    'level2bg5': 999,
    'level2bg6': 999,
    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy2': 50,
    'Enemy3':60,
}

ENTITY_DAMAGE = {
    'level1bg0': 0,
    'level1bg1': 0,
    'level1bg2': 0,
    'level1bg3': 0,
    'level1bg4': 0,
    'level1bg5': 0,
    'level1bg6': 0,
    'level2bg0': 0,
    'level2bg1': 0,
    'level2bg2': 0,
    'level2bg3': 0,
    'level2bg4': 0,
    'level2bg5': 0,
    'level2bg6': 0,
    'Player1': 1,
    'Player1Shot': 30,
    'Player2': 1,
    'Player2Shot': 25,
    'Enemy1': 15,
    'Enemy2': 20,
    'Enemy3':25,
}

ENTITY_SCORE = {
    'level1bg0': 0,
    'level1bg1': 0,
    'level1bg2': 0,
    'level1bg3': 0,
    'level1bg4': 0,
    'level1bg5': 0,
    'level1bg6': 0,
    'level2bg0': 0,
    'level2bg1': 0,
    'level2bg2': 0,
    'level2bg3': 0,
    'level2bg4': 0,
    'level2bg5': 0,
    'level2bg6': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 100,
    'Enemy2': 120,
    'Enemy3':130,
}

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 15,
}
# M
menu_option = ('NEW GAME 1P',
               'NEW GAME 2P - Cooperative',
               'NEW GAME 2P - Competitive',
               'SCORE',
               'EXIT')

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                    'Player2': pygame.K_LCTRL}

# S
SPAWN_TIME = 2000
# W
win_width = 600
win_height = 480
