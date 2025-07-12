import pygame

# C
color_g = (85, 107, 47)
c_white = (255, 255, 255)
color_y = (152, 251, 152)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
entity_speed = {
    'level1bg0': 0,
    'level1bg1': 1,
    'level1bg2': 2,
    'level1bg3': 3,
    'level1bg4': 4,
    'level1bg5': 3,
    'level1bg6': 5,
    'Player1': 3,
    'Player2': 3,
    'Enemy1': 1,
    'Enemy2': 1,
    'Enemy3':2,
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

# W
win_width = 600
win_height = 480
