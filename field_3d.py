def field_3d():
    field = [[[[0] for i in range(8)] for j in range(8)] for k in range (8)]
    s = 0
    size_x=8
    size_y=8
    size_z=8

    for z in range (size_z):
        for y in range (size_y):
            for x in range (size_x):
                if (x+y+z)%2==0:
                    field[x][y][z]=1
                else:
                    field[size_x-1-x][size_y-1-y][size_z-1-z]=2