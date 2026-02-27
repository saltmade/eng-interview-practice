"""
Given two sorted arrays of integers, arr1 and arr2, return a new array that
contains all the elements in arr1 and arr2 in sorted order, including
duplicates.

Edges
- Empty arrays
- Negative numbers
- Duplicates in the same array
- Duplicates in different arrays
- Arrays of different lengths

Complexity
n: length of arr1
m: length of arr2

Solutions
#1 Combine and sort
ans = arr1.extend(arr2)
ans.sort()
return ans

t: O(n+m * log nm)
s: O(1)

#2 Two pointers
init p1 and p2

ans = []
while p1 < len(arr1) and p2 < len(arr2)
  val1, val2 = arr1[p1], arr2[p2]
  if val1 < val2
    ans.append(val1)
    p1 += 1
  else
    ans.append(val2)
    p2 += 1

while p1 < len(arr1):
    ans.append(arr1[p1])
    p1 += 1

while p2 < len(arr2)
    ans.append(arr2[p2])
    p2 += 1

return ans

t: O(n+m)
s: O(1)
"""


def merge_arrays(arr1, arr2):
    p1, p2 = 0, 0
    ans = []
    while p1 < len(arr1) and p2 < len(arr2):
        val1, val2 = arr1[p1], arr2[p2]
        if val1 < val2:
            ans.append(val1)
            p1 += 1
        else:
            ans.append(val2)
            p2 += 1

    while p1 < len(arr1):
        ans.append(arr1[p1])
        p1 += 1

    while p2 < len(arr2):
        ans.append(arr2[p2])
        p2 += 1

    return ans
