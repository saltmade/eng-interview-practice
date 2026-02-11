"""
You are provided a series of aerial-view pictures of the same coastal region,
taken a few minutes apart from each other around the time the tide rises. Each
picture consists of an nxn binary grid, wher e0 represents a part of the region
above the water, and 1 represents a part below the water.

- The tide appears from the left side and rises toward the right, so, in each
  picture, for each row, all the 1's will be before the 0's.
- Once a region is under water, it stays under water

Determine which picture shows the most even balance between regions above and
below water (i.e. where the number 1's most closely equals the number of 0's).
In the event of a tie, return the earliest picture.

Complexity
n: number of cells in a row
nxn: number of cells in a grid
k: len of pictures array

Example
0 0 0
0 0 0
0 0 0

1 0 0
1 1 0
0 0 0

1 1 0
1 1 1
1 0 0

1 1 0
1 1 1
1 1 0

Ans = 2

Edges
- No water
- All water
- Equal water/land in more than 1

Solutions

#1 Naive
init ans, delta
for idx, grid in enumerate picture
    init zeroes and ones
    for val in grid
        if zero
            zeroes += 1
        else:
            ones += 1
    new_delta = abs ones - zeroes
    if new_delta < delta
        ans = idx
        delta = new_delta
return ans

t: O(RN)
s: O(1)

#2 Guess and Check
def is_before
    return zeroes < ones

def count_grid
    zeroes, ones
    for row in grid
        for val in row
            if val
                ones += 1
            else
                zeroes += 1
    return zeroes, ones

init left and right
while r - l > 1
    mid = r + l // 2
    zeroes, ones = count_grid
    if is_before zeroes ones
        l = mid
    else
        r = mid

return left

t: O(n^2 log k)
s: O(1)
"""


def tide_aerial_view(pictures):
    def is_before(ones, zeroes):
        return zeroes <= ones

    def count_grid(grid):
        ones, zeroes = 0, 0
        for row in grid:
            for val in row:
                if val:
                    ones += 1
                else:
                    zeroes += 1

        return ones, zeroes

    l, r = 0, len(pictures) - 1
    while r - l > 1:
        mid = r + l // 2
        ones, zeroes = count_grid(pictures[mid])
        if is_before(ones, zeroes):
            l = mid
        else:
            r = mid

    return l


"""
Post Mortem
- Missed a few opportunities
  - You can also search per-row for the transition point from water to land
  - A search in each row is O(log n)
    - Getting the water count of a grid, therefore, is O(n log n)
  - So this approach overall is an O(n log n log k) complexity
- Errors
  - Water in grid 0 is already more than 50 percent
  - Water in grid -1 is less than 50 percent
  - Possibility that r or l could be the answer, not just l
    - This is an important distinction
    - The transition point in the answer is when the value hits 50 percent or more (< 0.5)
    - This works because we want to find the earliest example to define the line
    - Setting it the way I did, <= 50 percent, means the left would end up at
      the last example of 50 percent, rather than the first.
"""
