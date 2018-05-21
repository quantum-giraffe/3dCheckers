from field_2d import *
import pygame
from classChecker import Checker

KEY_PLAY = '         Играть'
KEY_CONTINUE = '     Продолжить'
KEY_EXIT = '          Выйти'
KEY_RESTART = '   Начать заново'
KEY_SINGLE = '     Один игрок'
KEY_DOUBLE = '     Два игрока'

def init():
    field_checkers = [[[] for i in range(8)] for j in range(8)]
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 1:
                if i < 3:
                    field_checkers[j][i].append(Checker(-1, j, i))
                if i > 4:
                    field_checkers[j][i].append(Checker(1, j, i))
    current_player = 1
    count_checkers = [12] * 2
    return (field_checkers, current_player, count_checkers)

width = 400
field=field_2d()
done = True

field_checkers, current_player, count_checkers = init()



window = pygame.display.set_mode((width, width))
pygame.display.set_caption('Checkers')