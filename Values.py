from field_2d import *
import pygame

width = 400
field=field_2d()
field_checkers=[[[] for i in range(8)] for j in range(8)]
current_player=1
count_checkers=[12]*2
done = True

window = pygame.display.set_mode((width, width))
pygame.display.set_caption('Checkers')