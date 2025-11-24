def prompt_for_int():
    while True:
        try:
            val = int(input())
            return val
        except ValueError:
            print('Invalid integer. Please try again.')

if __name__ == '__main__':
    a = prompt_for_int()
    b = prompt_for_int()