total = 0
count = 0

#print("How manynums do you wnat to add?")
#nums_remaining = int(input())
user_val = input()
while user_val != 'quit' and user_val != '':
    total = total + int(user_val)
    count += 1
    user_val = input()
    #nums_remaining -= 1
print(f"Your average is {total / count}")