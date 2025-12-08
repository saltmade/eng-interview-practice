"""
Given three sorted arrays of integers, arr1, ar2, and arr3, return a new array with the
elements of all three arrays, in sorted order, *without duplicates*.

Edges
- Empty arrays
- Arrays of different lengths

j = len of arr1
k = len arr2
l = len arr3

2 3 3 4 5 7
3 3 9
3 3 9

#1 multiple pointers
init ans arr and 3 pointers
while any pointer is less than its arr
    get the val at each pointer
        if the val exists
        otherwise pos infinity
    get the min val
    move that pointer forward
    if the val isn't the last val in the ans
        append to the ans
return ans

t: o(j + k + l)
s: o(1)
"""
import math

def three_merge(arr1, arr2, arr3):
    ans = []
    p1, p2, p3 = 0, 0, 0

    while p1 < len(arr1) or p2 < len(arr2) or p3 < len(arr3):
        v1 = arr1[p1] if p1 < len(arr1) else math.inf  # inf
        v2 = arr2[p2] if p2 < len(arr2) else math.inf  # inf
        v3 = arr3[p3] if p3 < len(arr3) else math.inf  # inf
        va = ans[-1] if len(ans) else math.inf  # 9

        val, pointer = min([(v1, p1), (v2, p2), (v3, p3)])

        pointer += 1
        if val != va:
            ans.append(val)  # 2 3 4 5 7 9

    return ans