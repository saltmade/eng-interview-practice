"""
Given a binary grid, field, where:
- 1 denotes snowprints and 0 denotes no snowprints 
- each column has exactly 1 filled cell
- between consecutive columns the 1 may go up or down by one, or stay the same

Return the closest distance to the top edge, in terms of rows between it and the
highest 1. Assume the field has at least 1 row and 1 column.

Edges
- Is the field square? No

Examples
0 0 0 0 0 0
1 1 1 1 1 1
0 0 0 0 0 0

ans: 1

0 1 0 0 0 0
1 0 1 0 1 1
0 0 0 1 0 0

ans: 0

1

ans: 0

1 0 0 0 
0 1 0 0 
0 0 1 0 
0 0 0 1 

ans: 0

Complexity
n: rows in field
m: columns in field

Solutions

#1 Naive
init a lowest pos at +infinity
for r in grid
    for c in grid[0]
        if grid of r of c is 1 and r lt lowest pos
            lowest pos is r
return lowest pos

t: O(nm)
s: O(1)

#2 Steps
init lowest_r at pos inf
init r, c at 0 0
while r < len grid
    if r[0] == 1
        break
    r += 1

init next directions array 
# r and c must change
while c < len grid[0] - 1
    for dr in next row
        if val at r + dr and c + 1 is 1
            if r + dr < lowest_r
                lowest_r = r + dr
            r = r + dr
            c = c + 1

return lowest_r

t: O(n+m)
s: O(1)
"""
def snowprints(field):
    r, c = 0, 0
    while r < len(field):  # r = 1
        if r[0] == 1:
            break
        r += 1

    lowest_r = r
    nexts = [-1, 0, 1]

    def is_valid(r):
        return 0 <= r < len(field) and field[r][c] == 1

    while c < len(field[0]) - 1: # c < 3
        for dr in nexts:
            new_r, new_c = r + dr, c + 1  # 0
            if is_valid(new_r):  # 0
                if new_r < lowest_r:
                    lowest_r = new_r  # 0
                r = new_r
                c = new_c
                break

    return lowest_r

"""
0 1 0 1
1 0 1 0 
0 0 0 0 
"""
"""
Post Mortem
- Forgot that the first r should be included in the evaluation
    - Ended up fixing in the middle of implementing
- Forgot to check out of bounds above and below the grid
- Optimization for finding the first footprint:
while field[r][c] != 1
    r += 1
- Correct answer, but definitely could have been better optimized for clarity
"""