def countdown(start):
    if start < 0:
        print('Abort mission!')
    for i in range(start, -1, -1):
        if i == 0:
            print('Liftoff?')
        elif i % 4 == 0:
            print('Uh oh!')
        else:
            print(i)
if __name__ == '__main__':
    countdown(10)