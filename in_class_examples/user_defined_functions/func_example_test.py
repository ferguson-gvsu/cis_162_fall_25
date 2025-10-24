import math

def distance(x1, y1, x2, y2):
    x_diff = (x2 - x1)**2
    y_diff = (y2 - y1)**2
    return math.sqrt(x_diff + y_diff)

def is_in_circle(x1, y1, x2, y2, rad):
    return distance(x1, y1, x2, y2) <= rad