def calculate_drop(grid, col):
    for row_idx in range(len(grid)):
        #print(row_idx, grid[row_idx][col])
        if grid[row_idx][col] != ' ':
            #print('hit!')
            return row_idx - 1
    return len(grid) - 1
        

if __name__ == '__main__':
    board = [
    [' ', ' ', ' ', ' ', ' ', ' ', 'Y'],
    [' ', ' ', ' ', ' ', 'R', ' ', 'R'],
    [' ', ' ', 'Y', 'Y', 'Y', ' ', 'Y'],
    [' ', ' ', 'R', 'Y', 'Y', ' ', 'R'],
    [' ', 'Y', 'R', 'R', 'Y', 'R', 'Y'],
    [' ', 'R', 'Y', 'R', 'R', 'Y', 'R']
    ]
    print(calculate_drop(board, 1))