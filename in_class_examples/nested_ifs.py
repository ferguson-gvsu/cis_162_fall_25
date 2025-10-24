x = int(input())

if x > 10:
    print("In first if")
    x = x - 5
    if x > 20:
        print("In the nested if")
    else:
        print("In the else nested inside the if")
    print("Leaving if")
elif x > 5:
    print("In elif")
else:
    print("In else")