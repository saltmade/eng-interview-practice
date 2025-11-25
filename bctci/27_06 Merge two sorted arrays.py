"""
2025-11-25


Given two sorted arrays of integers, arr1 and arr2, return a new array that
contains all the elements in arr1 and arr2 in sorted order, including
duplicates.

Edges
- Empty array(s)
- Uneven arrays

Example
1 3 3 5 6
i
-1 0 3 4
j

Complexity
I = len arr1
J = len arr2

#1 Brute Force
Init pointers
Move through both arrays
    Add the lowest number to the ans
    Move that pointer forward
If there's anything left in one of the arrays
    Extend the ans
Return the ans

t: O(I + J)
s: O(1)
"""

def merge(arr1, arr2):
    p1, p2 = 0, 0
    ans = []
    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] < arr2[p2]:
            ans.append(arr1[p1])
            p1 += 1
        else:
            ans.append(arr2[p2])
            p2 += 1

    if p1 < len(arr1):
        ans.extend(arr1[p1:])
    elif p2 < len(arr2):
        ans.extend(arr2[p2:])

    return ans


"""
Post Mortem

- Should have used a while loop for extending the answer, since slicing creates a new array in memory
    - Note, this is true for builtin arrays but not for NumPy arrays, which return a view
"""