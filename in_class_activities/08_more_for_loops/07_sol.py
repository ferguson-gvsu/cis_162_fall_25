rows = int(input())
cols = int(input())
tile_size = int(input())

for row_idx in range(rows):
    for i in range(tile_size):
        for col_idx in range(cols):
            if (col_idx + row_idx) % 2 == 0:
                print('#' * tile_size, end = '')
            else:
                print('.' * tile_size, end = '')
        print()
