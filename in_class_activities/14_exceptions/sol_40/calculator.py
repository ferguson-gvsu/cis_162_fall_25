# is_a_valid = False
# while not is_a_valid:
#     print('Input first number:')
#     try:
#         a = int(input())
#         is_a_valid = True
#     except:
#         print('Invalid integer!')
while True:
    print('Input first number:')
    try:
        a = int(input())
        break
    except:
        print('Invalid integer!')
while True:
    print('Input second number:')
    try:
        b = int(input())
        break
    except:
        print('Invalid integer!')
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
