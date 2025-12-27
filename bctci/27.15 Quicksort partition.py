"""
Given an array of integers, arr, and a number, pivot, modify arr in place using
only O(1) extra space so that (1) every element smaller than the pivot appears
before every element greater than or equal to the pivot, and (2) every element
larger than the pivot appears after every element smaller than or equal to the
pivot. The relative order of the elements smaller or greater than the pivot does
not matter.

Edges
- Empty array
- Single int
- Pivot doesn't exist in array
- Pivot does exist in array
- Uneven distribution before/after pivot

1 9 2 18 4 5
         l
         r
p = 7

1 5 2 4 18 9

1 9 2
         l
      r
1 7 2 5 18 9
    l
    r
1 5 2 7 18 9
Complexity
n: len of arr

Solutions

#1 Inward pointers
init left and right
while left is less than right
    if val at left is lte pivot
        move left forward
    elif val at right is gt pivot
        move right backward
    else
        swap the two values
        move left
        move right
reset left to 0
while left lt right
    if left is pivot
        swap with right
        move right
    move left
    
t: O(n)
s: O(1)
"""
def partition(arr, pivot):
    left, right = 0, len(arr) - 1
    while left < right:
        if arr[left] <= pivot:
            left += 1
        elif arr[right] > pivot:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    
    boundary = 0
    while boundary < len(arr) and arr[boundary] <= pivot:
        boundary += 1
    left, right = 0, boundary - 1
    while left < right:
        if arr[left] < pivot:
            left += 1
        elif arr[right] == pivot:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

"""
Post Mortem
- Missed finding the boundary because I assumed the right pointer would be the
  boundary automatically.
    - Missed this because I didn't check for even and odd lengths of array
- Missed the swap in the second loop might mean I moved a boundary value to the wrong spot
original:
while left < right:
    if left == pivot:
        swap
        right -= 1
    left += 1
- l and r would be fine
"""