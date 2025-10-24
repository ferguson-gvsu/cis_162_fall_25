import math

def distance(x1, y1, x2, y2):
    a = x2 - x1
    b = y2 - y1
    return math.sqrt(a**2 + b**2)
    #return (a**2 + b**2) ** 0.5

def is_in_circle(x1, y1, x2, y2, radius):
    d = distance(x1, y1, x2, y2)
    return d < radius

d = distance(0, 0, 1, 1)
print(d)
print(math.sqrt(2))
print(0.5, is_in_circle(0, 0, 1, 1, 0.5))
print(math.pi, is_in_circle(0, 0, 1, 1, math.pi))