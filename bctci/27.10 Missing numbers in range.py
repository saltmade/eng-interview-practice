"""
Given a sorted array of integers, arr, and two values indicating a range, [low,
high], with low <= high, return a new array with all the numbers in the range
that do not appear in arr.

Edges
- Empty arr
- Low == high
- None of the values appear

-5 -3 0 1 5 10 100
      j

6 7 8 9
0
-1 0 1
   i

gt j += 1
et i += 1, j += 1
lt append, i += 1

6 9
0 0
-1 1

n = len of arr
r = len of range

Approaches
- Hashset :: for O(1) membership checks

#1 Brute Force
init ans
loop the range
    if i not in arr
        add to ans
return ans

t: O(rn)
s: O(1)

#2 Hashset
init ans
make a hashset of arr
loop range
    if i not in hashset
        add to ans
return ans

t: O(nr)
s: O(n)

#3 Separate pointers
init pa, pr at 0
init ran low, high + 1
while pr is lt len ran
    get vr, va
    if vr gt va
        move pa
    if vr et va
        move pr and pa
    if vr lt va
        append vr to ans
        move pr
return ans

t: O(n + r)
s: O(r)
"""
import math

def missing_nums(arr, low, high):
    pa, pr = 0, 0
    ran = range(low, high + 1)
    res = []

    while pr < len(ran):
        va = arr[pa] if pa < len(arr) else math.inf
        vr = ran[pr]
        if vr > va:
            pa += 1
        elif vr < va:
            res.append(vr)
            pr += 1
        else:
            pr += 1
            pa += 1

    return res
"""
1 2 3 4 5
          j
3 4 5 6
        i
"""

"""
Post Mortem
- Didn't think of how to handle ranges before or after the array
    - The book handles it via a wrap up instead of in the loop
    - Before isn't an issue because we would just fall into vr < va until the
      range ran out
- Didn't need to materialize the range
    - Could just check for i <= high
"""