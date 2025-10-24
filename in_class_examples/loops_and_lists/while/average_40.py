total = 0
count = 0

user_val = input()
while user_val != 'end' and user_val != '':
    total += int(user_val)
    count += 1
    user_val = input()
print(f"Your average is {total / count}")