"""
Given a rectangular RxC grid of integers, grid, and R > 0 and C > 0, return a
new grid with the same dimensions where each cell contains the maximum in the
subgrid with [r, c] in the top left corner and [R-1, C-1] in the bottom corner.

Example
-1 10  6    10 10 6
3   4  5->  5  5  5
2   1  2

Edges
- Largest number in bottom corner
- All negative
- R = C = 1

Complexity
R: # of rows in grid
C: # of cols in grid

Solutions

# 1 Naive
init ans as copy of grid size
for r in range R
    for c in C
        init highest
        for i in range r, R
            for j in range c, C
                highest = max of grid of i j, highest
        ans of r c = highest

return ans

t: O(r^2*c^2)
s: O(1)

#2 Bottom corner
init ans
def in_bounds
init R, C
init r, c = R-1, C-1
while r <= 0 and c <= 0
    for col in range c -1 -1
        down = ans r + 1 col if r+1 col in_bounds else -inf
        right = ans r col + 1 if r col + 1 in_bounds else -inf
        ans r col = max grid r col, right, down
    for row in range r -1 -1
        down
        right
        ans row c = max grid row c, down, right
    r -= 1
    c -= 1

return ans

t: O(RC)
s: O(1)
"""
import math

def subgrid_maximums(grid):
    R, C = len(grid), len(grid[0])
    ans = [[0] * C for _ in range(R)]
    for r in range(R, -1, -1):
        for c in range(C, -1, -1):
            down, right = -math.inf, -math.inf
            if r + 1 < R:
                down = ans[r + 1][c]
            if c + 1 < C:
                right = ans[r][c + 1]
            ans[r][c] = max(grid[r][c], down, right)

    return ans

"""
Post Mortem
- Recognized the opportunity of working backwards!
- Made it overly complicated by thinking I had to work on the diagonal
    - As the coded solution shows, a simple backwards walk, right to left and
    down to up, doesn't leave any calculations without the necessary precomputed
    values as I had assumed
    - I think a manual walk through of the solution in an example using a simple
      x char would have revealed this fact
"""