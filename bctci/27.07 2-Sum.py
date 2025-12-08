"""
Given a sorted array of integers, return whether there are two distinct indices,
i and j, such arr[i] + arr[j] = 0. Do not use more than O(1) extra space.

Edges
- Empty arrays
- All positive
- All negative
- 0 0

-10 -4 0 0 1 2 4 5
     l
               r

N = len of arr

1: Inward pointers
If len of arr is < 2
    return false
init two pointers
    one at the start, one at the end
Add the values at the two points together
    If zero
        return true
    If less than 0
        Move left pointer
    If more than 0
        Move right pointer
Return false

t: O(N)
s: O(1)

2: Binary search
"""
def complement_exists(arr):
    if len(arr) < 2:
        return False

    l, r = 0, len(arr) - 1

    while l < r:
        res = arr[r] + arr[l]
        if res == 0:
            return True
        elif res > 0:
            r -= 1
        else:
            l += 1
    
    return False

"""
Post Mortem
- Check for len < 2 is redudant given the while condition
"""