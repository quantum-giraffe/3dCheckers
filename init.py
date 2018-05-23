from classChecker import Checker


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
#    count_checkers[0]=0
    return (field_checkers, current_player, count_checkers)

