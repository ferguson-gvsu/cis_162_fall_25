rows = int(input())
cols = int(input())


letters = 'abcdefghijklmnopqrstuvwxyz'.upper()

for row_idx in range(rows):
    row_num = row_idx + 1
    for col_idx in range(cols):
        print(f"{row_num}{letters[col_idx]}", end=" ")
    print()