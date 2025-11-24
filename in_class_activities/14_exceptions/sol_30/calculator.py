print('Input first number:')
# is_a_valid = False
# while not is_a_valid:
#     try:
#         a = int(input())
#         is_a_valid = True
#     except:
#         print('Invalid integer given')
#         #exit(1)
while True:
    try:
        a = int(input())
        break
    except:
        print('Invalid integer given')
print('Input second number:')
while True:
    try:
        b = int(input())
        break
    except:
        print('Invalid integer given')
print('Input operator:')
op = input()

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '//':
    if b == 0:
        print('Don\'t try to divide by zero >:U')
    else:
        print(a // b)
else:
    print('Error: Invalid expression!')
