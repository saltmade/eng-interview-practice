"""
A valley-shapped array is an array of integers such that:
1. it can be split into a non-empty prefix and a non-empty suffix
2. the prefix is sorted in decreasing order (duplicates allowed)
3. the suffix is sorted in increasing order (duplicates allowed)
Given a valley-shaped array, arr, return a new array with the elements sorted.

4 3 2 1 2 3 4 = 1 2 2 3 3 4 4
  i
          j
4 1 2 3 4 = 1 2 3 4 4

1 2 = 1 2
i
j

2 2 1 1 = 1 1 2 2 
      i
      j

Edges
- Center is the beginning
- Center is the end
- Empty array

#1 BF
search the array for the min
    pop at that value

t: n^3 (n + n-1 + ... 0) * pop O(n)
s: O(1)

#2 sort
t: n log n
s: O(n)

# 3 outward pointers
find the center
init two pointers at the center
while i gte 0 or j is lte len of arr
    get i and j vals
    if vi is less than vj
        decrease i
        add vi to ans
    else
        increase j
        add vj to ans
return ans

t: O(n)
s: O(1)
"""
import math

def sort_valley(arr):  # 2 2 1 1
    if not arr:
        return []

    center = arr.index(min(arr))  # 2
    left, right = center, center  # 2 4
    ans = [0] * len(arr)  # 1 1 2 2
    i = 0

    while left >= 0 or right < len(arr):
        vl = arr[left] if left >= 0 else math.inf
        vr = arr[right] if right < len(arr) else math.inf
        if vl < vr:
            left -= 1
            ans[i] = vl
        else:
            right += 1
            ans[i] = vr

        i += 1
    
    return ans

"""
Post mortem
- Could have used inward pointers to skip the center-finding step (O(n) + O(n))
- While the complexity overall would be the same O(n), it would be less code
"""