def my_func(a, b):
    if a == b:
        raise ValueError('Cannot operate on identical ints', a, b)

try:
    my_func(2, 3)
except ValueError as e:
    print(f"Encountered exception: {e}")
    for arg in e.args:
        print(f'Arg: {arg}')