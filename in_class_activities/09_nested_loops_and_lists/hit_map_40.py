hit_map = [
    ['X','X',' '], 
    ['X'], 
    [' '], 
    [ ], 
    [' ',' ','X']
]

for x in hit_map:
    print(len(x), end = ' ')
print()

for sub_list in hit_map:
    print(f"Number of xs: {sub_list.count('X')}")

count_x = 0
for sub_list in hit_map:
    count_x += sub_list.count('X')
print('total number of xs:', count_x)
