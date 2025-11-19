def calculate_drop(grid, col):
    for row_idx in range(len(grid)):
        if grid[row_idx][col] != ' ':
            return row_idx - 1
    return len(grid) - 1
 