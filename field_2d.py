def field_2d():
    field = [[[0] for i in range(8)] for j in range(8)]
    s = 0
    size_x = 8
    size_y = 8

    for y in range(size_y):
        for x in range(size_x):
            if (x + y) % 2 == 0:
                field[x][y] = 0
            else:
                field[size_x - 1 - x][size_y - 1 - y] = 1
    return field

