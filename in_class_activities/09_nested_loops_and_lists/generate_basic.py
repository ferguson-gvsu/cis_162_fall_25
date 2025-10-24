import string

num_rows = 3
num_cols = 4

final_list = []

for row_idx in range(num_rows):
    row = []
    for col_idx in range(num_cols):
        index = row_idx * num_cols + col_idx
        row.append(string.ascii_lowercase[index])
    final_list.append(row)
print(final_list)