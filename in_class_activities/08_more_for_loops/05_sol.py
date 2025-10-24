rows = int(input())
cols = int(input())
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for row_idx in range(rows):
    for col_idx in range(cols):
        print(f'{row_idx + 1}{alphabet[col_idx]}', end=' ')
    print()