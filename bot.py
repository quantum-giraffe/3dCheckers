import random
import Values as v
import classChecker

def bot_step():
    print(int(9.9))
    checkers=[]
    for i in range(8):
        for j in range(8):
            if v.field_checkers[i][j] and v.field_checkers[i][j][0].color == -1:
                checkers.append([i,j])
    val = [[], False]
    current_checker = []
    while len(val[0])==0:
        current = int(random.random()*v.count_checkers[0])
        if current > 0:
            print(checkers,current)
            current_checker = v.field_checkers[checkers[current][0]][checkers[current][1]]
            print(current_checker)
            val = current_checker[0].valid_steps()
    to = int(random.random()*len(val[0]))
    print(to)
    print(val)
    print(val[to])

    current_checker[0].step(val[0][to][0], val[0][to][1])