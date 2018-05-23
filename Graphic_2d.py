from init import *
from Commands_2d import *
from bot import *
from superbot import *


def fill_checker(screen, width, x:int, y:int, color, is_king):
    r=width//16
    pygame.draw.circle(screen, (100+color*50, 100, 100+color*50), (int((x+0.5)*width//8), int((y+0.5)*width//8)), r )
    if is_king:
        pygame.draw.circle(screen, (200, 200, 0), (int((x + 0.5) * width // 8), int((y + 0.5) * width // 8)), int(r // 1.5), 1)
        pygame.draw.circle(screen, (200, 200, 0), (int((x + 0.5) * width // 8), int((y + 0.5) * width // 8)), int(r // 2.5), 1)
    if color==v.current_player:
        pygame.draw.circle(screen, (100+color*50, 150, 100+color*50), (int((x + 0.5) * width // 8), int((y + 0.5) * width // 8)), r, 2)

def graph_checkers():

    for x, string in enumerate(v.field_checkers):
        for y, cell in enumerate(string):
            if cell:
                fill_checker(v.window, v.width, x, y, cell[0].color, cell[0].is_king)

def fill_cell_red(x:int, y:int):
    pygame.draw.circle(v.window, ((250, 0, 0)), (int((x+0.5)*v.width//8), int((y+0.5)*v.width//8)), int(v.width//16), 3)


def graph(type):
#    print('c')
    v.field_checkers, v.current_player, v.count_checkers = init()
    screen = pygame.Surface((v.width, v.width))
    square = pygame.Surface((v.width//8, v.width//8))


    while v.done:
        if v.count_checkers[0]==0 or v.count_checkers[1]==0:
            win_screen = pygame.Surface((v.width, v.width))
            win(win_screen)
            StartScreen.Menu(v.window, v.width, [v.KEY_RESTART], background = win_screen).menu()
            break

        valids=[]

        if type == 1 and v.current_player == -1:
            bot_step()
        if type == 2 and v.current_player == -1:
            superbot()
        else:
            valids = Commands_processing()

        graph_field_2d(v.window, screen, square)
        graph_checkers()
        for valid in valids:
            fill_cell_red(valid[0], valid[1])

        pygame.display.flip()

def graph_field_2d(window, screen, square):
        window.blit(screen, (0, 0))
        screen.fill((15,15,15))
        square.fill((220, 220, 220))
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    screen.blit(square, (50 * i, 50 * j))




