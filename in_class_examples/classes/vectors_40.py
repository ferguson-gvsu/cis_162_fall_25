class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        s = f"<{self.x}, {self.y}>"
        return s
    
    def add(self, other):
        x = self.x + other.x
        y = self.y + other.y
        new_vec = Vector2D(x, y)
        return new_vec

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        new_vec = Vector2D(x, y)
        return new_vec
        #return Vector2D(x, y)

v = Vector2D(1, 2)
#v_str = str(v)
print(f'v is {v}')
w = Vector2D(10, -5)
print(f'w is {w}')
up = Vector2D(0, 1)
print(f'up is {up}')
res = v + up
print(f'v + up = {res}')