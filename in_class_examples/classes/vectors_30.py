class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        s = f"<{self.x}, {self.y}>"
        return s
    
    #def __int__(self):
    #    return self.x + self.y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        new_vec = Vector2D(x, y)
        return new_vec
        #return Vector2D(x, y)

        
v = Vector2D(1, 2)
w = Vector2D(3, -1)
print(v)
#print(int(v))
f_string = f"v is: {v}"
print(f_string)
up = Vector2D(0, 1)
print(f"up is {up}")
print(f"v + up = {v + up}")
print(f"v + 3 = {v + 3}")