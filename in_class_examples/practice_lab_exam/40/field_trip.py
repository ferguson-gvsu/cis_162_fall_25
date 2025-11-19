import math

def calculate_cost(num_students, students_per_bus, bus_price):
    #num_buses_float = num_students / students_per_bus
    #print(math.ceil(num_buses_float))
    num_buses_int = num_students // students_per_bus
    if num_students % students_per_bus != 0:
        num_buses_int += 1
    #if num_buses_float > num_buses_int:
    #    num_buses_int += 1
    return [num_buses_int, num_buses_int * bus_price]

if __name__ == '__main__':
    print(calculate_cost(21, 12, 5))
    print(calculate_cost(21, 7, 5))