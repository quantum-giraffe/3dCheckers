from math import *
from field_2d import *

field=field_2d()

class Checker:

    def __init__(self, color:int, x:int, y:int, is_king=False, z=-1):
        assert(0<=x<8 and 0<=y<8 and -1<=z<8)
        assert(color==-1 or color==1)
#        print((x,y))
        self.x = x
        self.y = y
        self.z = z
        self.color = color
        self.is_king = is_king


    def __str__(self):
        return str(self.color)
    def __repr__(self):
        return 'Checker'+str(self.color)

    def single_steps(self, field_checkers):

        A = []
        color=field_checkers[self.x][self.y][0].color
        for i in (-1, 1):
#            print('self.x,y: ',self.x,self.y)
#            print('i,j: ',i,j)
            B = (self.x + i, self.y - color)
#            print('B: ',B)
            if 0 <= B[0] < 8 and 0 <= B[1] < 8 and field[B[0]][B[1]] == 1:
                if not field_checkers[B[0]][B[1]]:
                    A.append(B)
#        print('A: ',A)
        return A

    def cut_steps(self, field_checkers):
        A = []
        for i in (-1, 1):
            for j in (-1, 1):
                B = (self.x + i, self.y + j)
                if 0 <= 2*B[0] - self.x < 8 and 0 <= 2*B[1] - self.y < 8 and field[B[0]][B[1]] == 1:
#                    print()
                    if field_checkers[B[0]][B[1]] and field_checkers[B[0]][B[1]][0].color != \
                            field_checkers[self.x][self.y][0].color:
#                        print(B[0], ' - ', self.x, ":", B[1], ' - ', self.y)
                        if not field_checkers[2 * B[0] - self.x][2 * B[1] - self.y] :
                            A.append((2 * B[0] - self.x, 2 * B[1] - self.y))
        return A

    def king_steps(self, field_checkers):
        A = []
        for sign_x in (-1, 1):
            for sign_y in (-1, 1):
                k=1
                while (0 <= self.x + k * sign_x < 8) and (0 <= self.y + k * sign_y < 8) and \
                    not field_checkers[self.x + k*sign_x][self.y + k*sign_y]:
                    B = (self.x + k * sign_x, self.y + k * sign_y)
                    k+=1
                    A.append(B)

        return A

    def king_cut_steps(self, field_checkers):
        A = []
        for k in range(1, 7):
            for sign_x in (-1, 1):
                for sign_y in (-1, 1):
                    B = (self.x + k * sign_x, self.y + k * sign_y)
                    if 0 <= B[0] < 8 and 0 <= B[1] < 8 and field[B[0]][B[1]] == 1 and  field_checkers[B[0] - sign_x][B[1] - sign_y]:
                        if (field_checkers[B[0]-sign_x][B[1]-sign_y][0].color != field_checkers[self.x][self.y][0].color)\
                                and not field_checkers[B[0]][B[1]]:
                            i = 1
                            while (0 <= self.x + i * sign_x < 8) and (0 <= self.y + i * sign_y < 8) and \
                                    not field_checkers[self.x + i * sign_x][self.y + i * sign_y]:
                                i+=1
                            if i==k-1:
                                A.append(B)

        return A

    def valid_steps(self, field_checkers, current_player):
        if self.is_king:
            cuts=self.king_cut_steps(field_checkers)
            if len(cuts)>0:
                return [cuts, False]
            else:
                if not all_cut_steps(field_checkers, current_player):
                    return [self.king_steps(field_checkers), True]
                else:
                    return [[], True]
        else:
            cuts=self.cut_steps(field_checkers)
            if len(cuts)>0:
#                print(cuts)
                return [cuts, False]
            else:
                if not all_cut_steps(field_checkers, current_player):
                    return [self.single_steps(field_checkers), True]
                else:
                    return [[], True]

    def step(self, x_new, y_new, field_checkers, current_player, count_checkers):
        valid=self.valid_steps(field_checkers, current_player)
        if self.z==-1:
            if not valid[0].count((x_new, y_new)):
                pass
#                return -1
            else:
                if valid[1]:
#                    print('здесь')
                    current_player *= -1
#                    print(current_player)
                    field_checkers[x_new][y_new].append(Checker(self.color, x_new, y_new, self.is_king))
                else:
                    for i in range (1, abs(x_new - self.x)):
                        if  field_checkers[int(self.x+i*copysign(1, x_new - self.x))][int(self.y + i*copysign(1, y_new - self.y))]:
                            count_checkers[int(field_checkers[int(self.x+i*copysign(1, x_new - self.x))][int(self.y + i*copysign(1, y_new - self.y))][0].color*0.5+0.5)] -= 1
                            field_checkers[int(self.x + i * copysign(1, x_new - self.x))][
                                int(self.y + i * copysign(1, y_new - self.y))].pop()
                            field_checkers[x_new][y_new].append(Checker(self.color, x_new, y_new, self.is_king))
#                            print('тут')
                    if y_new == 3.5 - self.color * 3.5:
                        field_checkers[x_new][y_new][0].is_king = True
                    if not field_checkers[x_new][y_new][0].cut_steps(field_checkers):
                        current_player *= -1
                    else:
                        field_checkers[int(self.x)][int(self.y)].pop()
                        return True

                if y_new == 3.5 - self.color * 3.5:
                    field_checkers[x_new][y_new][0].is_king = True

                field_checkers[int(self.x)][int(self.y)].pop()
                return False






def all_cut_steps(field_checkers, current_player):

    for string in field_checkers:
        for cell in string:
            if cell:
                if cell[0].color == current_player:
                    if cell[0].is_king:
                        if len(cell[0].king_cut_steps(field_checkers)) > 0:
                            return True
                    else:
                        if cell[0].cut_steps(field_checkers):
                            return True
    return False



