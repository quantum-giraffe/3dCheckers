from field_2d import *
import pygame
from init import init

KEY_PLAY = '         Играть'
KEY_CONTINUE = '     Продолжить'
KEY_EXIT = '          Выйти'
KEY_RESTART = '   Начать заново'
KEY_SINGLE = '     Один игрок'
KEY_DOUBLE = '     Два игрока'
KEY_SIMPLE = '       Простой'
KEY_DIFFICULT = '      Сложный'

background_image = pygame.image.load('check1.jpg')



width = 400
field=field_2d()
done = True

field_checkers, current_player, count_checkers = init()



window = pygame.display.set_mode((width, width))
pygame.display.set_caption('Checkers')