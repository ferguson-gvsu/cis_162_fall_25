class Part:
    next_id  = 1
    def __init__(self, name):
        self.name = name
        self.id = Part.next_id
        Part.next_id += 1

part_1 = Part('Steering Wheel')
part_2 = Part('Brake pad')
part_3 = Part('X')
print(part_1.name, part_1.id)
print(part_2.name, part_2.id)
print(part_3.name, part_3.id)