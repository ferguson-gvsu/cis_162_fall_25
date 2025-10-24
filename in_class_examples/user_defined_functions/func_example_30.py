import math

def distance(x1, y1, x2, y2):
    a = x2 - x1
    b = y2 - y1
    return math.sqrt(a**2 + b**2)

def is_in_circle(x1, y1, x2, y2, radius):
    d = distance(x1, y1, x2, y2)
    return d <= radius
print(is_in_circle(0, 0, 0, 1, 0.5))
print(is_in_circle(0, 0, 0, 1, 2))
print(is_in_circle(0, 0, 0, 1, 1))
x = 12
if x > 20:
    pass
print("hello")