"""
Given a rectangular RxC grid of integers, grid, with R > 0 and C > 0, return a
new grid with the same dimensions where each cell [r,c] contains the sum all the
elements in the subgrid with [r, c] in the top left corner and [R-1, C-1] in the
bottom right corner.

2 1 -4
3 10 3
7 2 -2

22 10 -3
23 13 1
7  0 -2

x = grid[x] + ans of r d - ans c

Complexity
R
C

Solutions
#1 Naive
get all values of the grid from each position

t: O(r^2 c^2)
s: O(1)

#2 right down corner
init R and C
for r in range R -1 -1
    for c in range C -1 -1
        right = ans r c+1 if in bounds
        down = ans r+1 c if in bounds
        corner = ans r+1 c+1 if in bounds
        ans r c = grid r c + right + down - corner

return ans

t: O(RC)
s: O(1)
"""
def subgrid_sums(grid):
    R, C = len(grid), len(grid[0])
    ans = [row.copy() for row in grid]
    for r in range(R, -1, -1):
        for c in range(C, -1, -1):
            right = ans[r][c +1] if c + 1 < C else 0
            down = ans[r+1][c] if r + 1 < R else 0
            corner = ans[r+1][c+1] if r + 1 < R and c+1 < C else 0
            ans[r][c] = ans[r][c] + right + down - corner
    
    return ans

"""
Post Mortem
- I figured it out!
- I walked away for a sec and layed down, thinking about how to get the solution
    - It was a low pressure, more fun way to get the answer
    - In that way I saw it like a puzzle to solve
- It is challenging to describe the answer without the ability to draw
    - I used a whiteboard at home, but won't have that in an interview
- I can actually see a quiet interviewer in this case as a gift
    - Quiet as the sphinx with a riddle
- It helps that this is a variation of the previous problem
"""