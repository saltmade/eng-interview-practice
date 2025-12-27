"""
Given an nxn binary grid, where n > 0, a 0 denotes an empty cell, and a 1
indicates a queen. Return a binary board with the same dimensions, where a 0
denotes that a cell is safe, and a 1 denotes that cell is not safe. I.e. that
the cell cannot be reached by a queen.

Edges
- All queens
- No queens

Complexity
N: number of cells in grid (nxn)

Solutions

#1 Naive
init ans array
init directions array
Loop over grid
for each cell's row, col in grid
    for row, col in each cardinal direction
        get new row, col by adding row, col to cell's row, col
        while val isnt 1 and is in bounds
            overwrite the values in ans with 1
            add the row col 

t: O(N^2)
s: O(1)

#2 Start at the queens
init ans array as dupe of grid
init directions array
for row in grid
    for col in grid of row
        if val at grid of row col is a queen
            for drow, dcol in directions
                get newrow, newcol by adding drow, dcol to row col
                while val isn't 1 and newrow, newcol is in bounds
                    overwrite the newrow newcol value in ans with 1
                    add the drow, dcol to newrow, new col
return ans

t: O(N)
"""
def safe_cells(board):
    n = len(board)
    ans = [[0] * n for _ in range(n)]
    directions = [[1, 1] [1, -1], [-1, 1], [-1, -1], [0, 1], [1, 0], [0, -1], [-1, 0]]
    for row in range(n):
        for col in range(n):
            if board[row][col] == 1:
                ans[row][col] = 1
                for drow, dcol in directions:
                    new_row, new_col = row + drow, col + dcol
                    while is_valid(board, new_row, new_col):
                        ans[new_row][new_col] = 1
                        new_row += drow
                        new_col += dcol

    return ans

def is_valid(board, row, col):
    n = len(board)
    return board[row][col] != 1 and 0 <= row < n and 0 <= col < n