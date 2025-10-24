hit_map = [
    ['X','X',' '], 
    ['X'], 
    [' '], 
    [ ], 
    [' ',' ','X']
]

print(len(hit_map))

for x in hit_map:
    print(len(x), end = ' ')
print()

for sub_list in hit_map:
    print(f"This line has {sub_list.count('X')}")

x_count = 0
for sub_list in hit_map:
    x_count += sub_list.count('X')
print(f'We have a total of {x_count} x')