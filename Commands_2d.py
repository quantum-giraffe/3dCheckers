import pygame
import sys
import Values as v
global current_player

def Commands_processing():

    global done
    try:
        Commands_processing.step_started
    except:
        Commands_processing.step_started = False

    try:
        if Commands_processing.valids:
            pass
    except:
        Commands_processing.valids = []

    try:
        pos=Commands_processing.pos
        pos1=Commands_processing.pos1
    except:
        Commands_processing.pos=(0,0)
        Commands_processing.pos1=(0,0)

    print(Commands_processing.step_started)
    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            done = False
#            sys.exit()
        if not Commands_processing.step_started:
            if pygame.mouse.get_pressed()[0]:
#                print(1)
                pos = (pygame.mouse.get_pos()[0] // (v.width // 8), pygame.mouse.get_pos()[1] // (v.width // 8))
                Commands_processing.pos = pos
                if  v.field_checkers[pos[0]][pos[1]]:
#                    print(pos)
#                    print(field_checkers[pos[0]][pos[1]])
#                    print('a',v.field_checkers[pos[0]][pos[1]][0].color)
#                    print('b',v.current_player)
                    if  v.field_checkers[pos[0]][pos[1]][0].color == v.current_player:
#                        print(pos)
#                        print(1.1)
                        Commands_processing.valids = v.field_checkers[pos[0]][pos[1]][0].valid_steps()
#                        print(1.2)

                        Commands_processing.step_started=True
#                        print(2)
                        break

        while Commands_processing.step_started:
#            print(3)
            flag=False
            for event in pygame.event.get():
                if event.type == pygame.K_ESCAPE:
                    Commands_processing.step_started = False
                    break
                if pygame.mouse.get_pressed()[0]:
                    pos1 = (pygame.mouse.get_pos()[0] // (v.width // 8), pygame.mouse.get_pos()[1] // (v.width // 8))
                    Commands_processing.pos1 = pos1
    #                for i, x in enumerate(field_checkers):
    #                    print(field_checkers[i])
    #                print(pos1)
                    if pos1 == pos:
                        Commands_processing.step_started = False
                        Commands_processing.valids = []
                        break
                    if Commands_processing.valids.count(pos1):

                        if v.field_checkers[pos[0]][pos[1]][0].step(pos1[0], pos1[1]):
                            Commands_processing.pos=pos1
                            pos = Commands_processing.pos
                            Commands_processing.valids = v.field_checkers[pos[0]][pos[1]][0].cut_steps()
#                            print(v.count_checkers)
#                            print(Commands_processing.step_started)
                            flag=True
                            break
#                        print('c', v.current_player)
                        else:
                            Commands_processing.step_started = False
                            Commands_processing.valids = []

            if flag:
                break
        break

    return Commands_processing.valids