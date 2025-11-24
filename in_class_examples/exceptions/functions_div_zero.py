def prompt_for_int():
    while True:
        try:
            val = int(input())
            return val
        except:
            print('Invalid integer. Please try again.')

def divide():
    print('First number:')
    a = prompt_for_int()
    print('Second number:')
    b = prompt_for_int()
    print(a / b)

# def main():
#         divide()

if __name__ == '__main__':
    divide()
    #main()