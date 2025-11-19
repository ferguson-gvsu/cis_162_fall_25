import math

def calculate_cost(num_students, students_per_bus, bus_price):
    #num_buses = math.ceil(num_students / students_per_bus)
    num_buses = num_students // students_per_bus
    students_leftover = num_students % students_per_bus
    if students_leftover != 0:
        num_buses += 1
    return [num_buses, num_buses * bus_price]

if __name__ == '__main__':
    calculate_cost(30, 10, 5)