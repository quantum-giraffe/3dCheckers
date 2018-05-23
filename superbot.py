import random
import Values as v
import pygame
import sys
import StartScreen
from classChecker import *
import copy


def superbot_step(field, my_color, score=0):
    enemy_color = -my_color
    cuts = 0
    checkers = []
    my_count = 0
    enemy_count = 0
    for i in range(8):
        for j in range(8):
            if field[i][j] and field[i][j][0].color == my_color:
                checkers.append(field[i][j][0])
                my_count += 1
            elif field[i][j] and field[i][j][0].color == my_color:
                enemy_count += 1
    for checker in checkers:
        if all_cut_steps(field, my_color):
            cuts += 1
        valids = checker.valid_steps(field, my_color)[0]
        if valids:
            for valid in valids:
    #            for i in range(8):
    #                print(field[i])
    #            print('o')
                new_field = copy.deepcopy(field)
                if my_count == 0:
                    return score
                elif enemy_count == 0:
                    score += 100
                    return score

    #            print(valid[0], valid[1], new_field, my_color, [1,1])
                elif checker.step(valid[0], valid[1], new_field, my_color, [1,1]):
                    score += superbot_step(new_field, my_color)
                else:
                    score += superbot_step(new_field, enemy_color)
    if cuts==0:
        return score
    return score - my_color

def superbot():
#    print('kkkkk')
    my_color = -1
    all_steps = []
    checkers = []
    gen_score = 0
    for i in range(8):
        for j in range(8):
#            print(v.field[i][j], v.field[i][j][0].color, my_color)
            if v.field_checkers[i][j] and v.field_checkers[i][j][0].color == my_color:
                checkers.append(v.field_checkers[i][j][0])
    for checker in checkers:

        valids = checker.valid_steps(v.field_checkers, my_color)[0]
        for valid in valids:
#            print(valid)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    v.done = False
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
#                        print('q')
                        StartScreen.Menu(v.window, v.width, [v.KEY_CONTINUE, v.KEY_RESTART, v.KEY_EXIT]).menu()
            score = 0
            new_field = copy.deepcopy(v.field_checkers)
            if checker.step(valid[0], valid[1], new_field, my_color, [1, 1]):
                score += superbot_step(new_field, my_color)
            else:
                score += superbot_step(new_field, -my_color)
            gen_score += score
            all_steps.append([score, checker, valid])

    for step in all_steps:
        print('(x1,y1) = ', (step[1].x, step[1].y), '(x2,y2) = ', step[2], 'вероятность = ', step[0]/gen_score)

    rand = random.random()*gen_score
    step1=[]
    while rand > 0:
#        print("adadad")
        step1 = all_steps.pop()
        rand -= step1[0]
    if step1:
        if not step1[1].step(step1[2][0], step1[2][1], v.field_checkers, my_color, v.count_checkers):
            v.current_player *= -1

