"""
Given a positive and odd integer n, return an nxn grid of integers filled as
follows: the grid should have every number from 0 to n^2-1 in spiral order,
starting by going down from the center and turning clockwise.

Edges
- n = 0?
- n = 1

Example
n = 3
4 5 6
3 0 7
2 1 8

- Center out
- End to beginning
- Counter clockwise

Complexity
n:

Solutions

#1 Start at the end
init a counterclockwise direction array
init r, c at n-1
init ans array
init direction pointer
def validation function
    inbounds and not 0

for i in range n^2-1, stopping at -1, stepping backwards by -1
    set the ans at r c to i
    add dr, dc in direction array to r c
    if next r c are valid
        set r and c to next r and c
    else
        set the direction pointer + 1 % 4
        set r, c with new direction values

t: O(n^2)
s: O(1)
"""
def spiral(n):
    directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    dp = 0
    r, c = n-1, n-1  # 2, 2
    ans = [[0] * n for _ in range(n)]

    def is_valid(r, c):
        return 0 <= r < n and 0 <= c < n and ans[r][c] == 0

    for i in range(n^2 - 1, -1, -1):
        ans[r][c] = i
        dr, dc = directions[dp]
        next_r, next_c = r + dr, c + dc
        if is_valid(next_r, next_c):
            r, c = next_r, next_c
        else:
            dp = (dp + 1) % 4
            dr, dc = directions[dp]
            r, c = dr + r, dc + c
    
    return ans
"""
Post Mortem
- Nice! Got the reverse solution on the first try
- Could have made the if...else logic slightly less verbose, but it would be the same
"""