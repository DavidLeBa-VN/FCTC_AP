import math
def polysum(n, s):
    area = 0.25 * n * s * s / math.tan(math.pi/n)
    perimeter = n * s
    return round(area + perimeter * perimeter, 4)