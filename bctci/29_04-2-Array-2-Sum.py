"""
Given two non-empty arrays of integers, sorted_arr and unsorted_arr, find one
element from each array that together sum to 0. If you can find them, return an
array of their indices, starting with the element in sorted_arr. Otherwise,
return [-1, -1]. Use O(1) extra space and do not modify the input.

Example
   0 1 2 3 4
s -2 0 1 4 6
  l
           r
       m

u -10 4 -1 3

0
0

4 5 6
-4

Edges
- Repeat elements
- No negatives
- Two 0s

Complexity
S: len of sorted
U: len of unsorted

Solutions

#1 Naive
for each uidx, uval in enum unsorted
    for each sidx, sval in enum sorted
        if uval + sval == 0
            return sidx, uidx
return -1 -1

t: O(S*U)
s: O(1)

#2 Binary search S
s = len sorted
def bin_search
    l, r = 0, s-1

    if sorted of l == target
        return l

    while r - l > 1
        m = l + r // 2
        if sorted of m == target
            return m
        elif sorted of m < target
            l = m
        else
            r = m
    if sorted of r == target
       return r

    return -1 

for each uidx, uval in enum unsorted
    sidx = bin_search for -uval
    if sidx >= 0
        return sidx uidx

return -1 -1

t: O(U log S)
s: O(1)
"""

"""
Post Mortem
- Forgot some conditionals until I went back
    - If the target is at 0
        - Target is outside the range (technically handled this one, but didn't need to search
"""