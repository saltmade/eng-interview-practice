"""
You're given a sorted 2D grid of integers, grid, where each row is sorted and
without duplicates. The last value in each row is smaller than the first value
in the following row.

You are also given a target value, target,. if the target is in the grid, return
an array with its row and column indices. Otherwise return [-1, -1].

Example

-4 -2 -1 0
1  2  4  8
100 200 1000 1001

target 14

0  1  2
-4 1 100
   l
   m
      r

0 1 2 3
1 2 4 8 14
      l
      m
         r

Edges
- Negative numbers
- Empty grid
- Value is above or below grid

Complexity
C: len of a row, aka # of columns
R: len of grid, aka # of rows

Solutions

#1 Naive
for row in grid
    for col in row
        if grid of row of col is target
            return row, col
return -1 -1

t: O(R*C)
s: O(1)

#2 Two-way binary search
- search across the first digit in each row to find the row
- search within the row to find the target

if not grid or target < grid 0 0 or target > grid R-1 C-1
    return -1 -1

def is_before
    return val <= target

R, C = len grid, len of grid of 0
l r = 0 , R-1

while r - l > 1
    m = l + r // 2
    if is_before grid of m of 0
        l = m
    else
        r = m

row = l
l, r = 0, C - 1

while r - l > 1
    m = r + l // 2
    if is_before grid row m
        l = m
    else
        r = m

if grid row l == target
    return row l
elif grid row r == target
    return row r
else
    return -1 -1

t: O(log R + log C)
s: O(1)
"""

"""
Post Mortem
- While my two-step binary search approach works, there is a trick to make it simpler
- TRICK!
    - virtualized flattened grid
    - l, r = 0, R*C -1 (since that would be the length if we flattened it)
    - is_before will need to translate coordinates
        - r, c = i // num_cols, i % num_cols
        - Row math
            - 3 rows of 8 columns would be 24 cells
            - 0-7, 8-15, 16-23
            - Integer division, i.e. rounding down, is like saying how many rows
              of 8, to the nearest row, fit into this number?
        - Column math
            - Modulo is the remainder after dividing
            - How much is leftover after filling this number with as many rows
              of 8 as possible?
"""