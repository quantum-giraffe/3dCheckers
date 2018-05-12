import pygame
import Graphic_2d
from classChecker import *
from field_2d import *
from Values import *


for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 1:
            if i < 3:
                field_checkers[j][i].append(Checker(-1, j, i))
            if i > 4:
                field_checkers[j][i].append(Checker(1, j, i))

#for i,x in enumerate(field_checkers):
#    print(field_checkers[i])

while True:
    Graphic_2d.graph()


