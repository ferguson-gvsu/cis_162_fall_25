try:
    x = int(input())
    print(5 / x)
    open('fake.txt', 'r')
except ValueError:
    print('Invalid integer')
except ZeroDivisionError:
    print('Don\'t divide by zero!')
except:
    print('You broke something else!')