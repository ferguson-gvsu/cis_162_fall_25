def countdown(start):
    if start < 0:
        print('Abort mission!')
    i = start
    while i >= 0:
        if i == 0:
            print('Liftoff?')
        elif i%4 == 0:
            print('Uh oh!')
        else:
            print(i)
        i -= 1
countdown(10)