rows = int(input())
cols = int(input())
  
for i in range(rows): 
    if i == 0 or i == rows - 1:
        for j in range(cols):
            print("*", end="")
    else:
        #print("*", end="")
        #for j in range(cols - 2):
        #    print(" ", end="")
        #print("*", end="")
        print("*" + " " * (cols - 2) + "*", end="")
    print()