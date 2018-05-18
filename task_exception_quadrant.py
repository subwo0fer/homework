def get_quadrant_number(x, y):
    if x > 0 and y > 0:
        return 1
    if x > 0 and y < 0:
        return 4
    if x < 0 and y < 0:
        return 3
    if x < 0 and y > 0:
        return 2
    if x == 0 or y == 0:
        raise ValueError
