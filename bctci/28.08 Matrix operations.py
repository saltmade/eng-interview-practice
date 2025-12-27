"""
Implement a Matrix class with the following methods:
- transpose
- clockwise rotate
- counterclockwise rotate
- reflect horizontally
- reflect vertically

All methods should:
- take 0 params
- modify the matrix in-place
- use O(1) extra space
- return nothing

Example
1 2 3
4 5 6
7 8 9

Complexity
R len of matrix
C len of matrix 0

transpose
1 4 7
2 5 8
3 6 9
- switch the r c values of each
- need to traverse the diagonal, otherwise flip back
    init pad
    for row in range R
        for col in range pad, C
            matric r c, c r = cr, rc
        pad += 1

t: O(RC)
s: O(1)

reflect horiz
3 2 1
6 5 4
9 8 7

reflect vertical
7 8 9
4 5 6
1 2 3

clockwise
7 4 1
8 5 2
9 6 3

1. Transpose
2. reflect horiz

counterclockwise
1. reflect horiz
2. transpose

"""
class Matrix:
    def __init__(self, grid):
        self.matrix = [row.copy() for row in grid]
        self.R = len(grid)
        self.C = len(grid[0])

    def transpose(self):
        pad = 0
        mat = self.matrix
        for r in range(self.R):
            for c in range(pad, self.C):
                mat[r][c], mat[c][r] = mat[c][r], mat[r][c]
            pad += 1

    def reflect_horizontal(self):
        for row in self.matrix:
            row.reverse()

    def reflect_vertical(self):
        self.matrix.reverse()

    def clockwise(self):
        self.transpose()
        self.reflect_horizontal()

    def counterclockwise(self):
        self.reflect_horizontal()
        self.transpose()

"""
Post Mortem
- Iirc they do not jump in to help
    - Which means it's only worth it to add clarity if a) I need it or b) I
      expect them to need it later
- Nifty trick with transpose: the pad is the same as the row number
    - I.e. I could put r in instead of pad and flip the other side of the diagonal
"""