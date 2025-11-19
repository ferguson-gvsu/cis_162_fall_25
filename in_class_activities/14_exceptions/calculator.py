print('Input first number:')
a = int(input())
print('Input second number:')
b = int(input())
print('Input operator:')
op = input()

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '//':
    print(a // b)
else:
    print('Error: Invalid expression!')
