def check_answer(num):
	return num % 11 == 0 and num % 7 == 0 and num > 0

correct = False 
x = -1
while correct == False:
	x += 1
	correct = check_answer(x)
print(x)