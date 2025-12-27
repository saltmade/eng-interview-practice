"""
Given a 9x9 grid, board, representing a Sudoku, return true if the board does
not have any conflicts and false otherwise.

0s denote empty cells

- Row
- Col
- Subgrid

Edges
- All 0s
- All 9s
- No conflicts

    0 1 2 3 4 5 6 7 8
    
0   0 1 0 0 0 2 0 0 9
1   0 x 1 0 0 0 0 0 0
2   3 0 0 0 8 0 0 0 3
3   0 0 1 0 0 0 0 0 0
4   0 0 1 0 0 0 0 0 9
5   0 0 1 0 0 0 0 0 0
6   0 0 1 0 0 0 0 0 0
7   0 0 1 0 0 0 0 0 0
8   0 0 1 0 x 0 0 0 0

1,1 = 0, 0 -> 2, 2

8, 5 = 6,3 -> 8, 6
- Modulo?
- Precomputed?
    0, 2
        0, 2 = {}
        3, 5 = ...
        6, 8
    3, 5
        ...
    6, 8

- How to find the subgrid

Complexity
- 81
- 

Solutions
#1 Naive
init subgrids
for r in board
    for c in board[0]
        

def in_row
    return if it's in the row

def in_col
    init dr = 0
    while dr < len grid
        if grid dr c == grid r c and dr != r
            return True
        dr += 1
    return False

def in_subgrid

"""

def is_valid(board):
    return valid_rows(board) and valid_cols(board) and valid_subgrids(board)

def valid_rows(board):
    for row in board:
        seen = set()
        for val in row:
            if val in seen:
                return False
            if val != 0:
                seen.add(val)
    return True

def valid_cols(board):
    for i in range(len(board)):
        seen = set()
        for row in board:
            val = board[row][i]
            if val in seen:
                return False
            if val != 0:
                seen.add(val)
    return True

def valid_subgrids(board):
    def check_subgrid(start_r, start_c):  # 0 0
        seen = set()
        for row in range(start_r, start_r + 3):
            for col in range(start_c, start_c + 3):
                val = board[row][col]
                if val in seen:
                    return False
                if val != 0:
                    seen.add(val)
        return True

    for i in range(3):
        for j in range(3):
            if not check_subgrid(i * 3, j * 3):
                return False

    return True

"""
Post Mortem
- Note: This is the first one I couldn't figure out on my own in a while. The
  coded solution is my implementation after learning how to do it.
- I had the shape correct, with three separate functions
- But:
    - I didn't have each function checking one aspect
    - My approach imagined a single loop over the whole grid
    - The book's answer shows the power of breaking down the problem
- I also
    - didn't account for 0s
    - didn't account for the start of ranges in the subgrid
- I suspect way to puzzle this out is to write out the sequences of coordinates
  I need to check, then back into the formula for getting said coordinates.
"""