"""
Given a non-empty array with n positive integers, arr, and a number k with 1 <=
k <= n, the goal is to split arr into k non-empty subarrays so that the largest
sum across all subarrays is minimized. return the largest sum across all k
subarrays after making it as small as possible. Each subarray must contain at
least one value.

Example
10 5 8 9 11 k=3
17

10 4,9 8,11

1 1 1 1 1 1 12 k=3
12

1,1 1,1 1,1,12

Edges
- Outsize number

Solutions

#1 Bin packing
init k arrays
add arrays to a heap
    (sum, arr)
add values into bottom value in the heap
return sum

#2 Naive
init k arrays
try adding every value to every array
return the lowest array value seen

t: O(n^k)
s: 
"""

"""
Post Mortem
- Got hung up on the idea of bin packing and missed the fact that it's
  subarrays, i.e. they must be sequential
    - Otherwise we could move them around to fit the smallest arr
- Guess and Check
    - Unintuitive application of binary search
        - Guess the midpoint and check whether it's too high or too low
    - Range of possible answers is between the max(arr) and sum(arr)
    - Search over those values as max array value, seeing if you can get lte k
    - O(log S) for binary search of sum(arr) * O(n) for subarray fitting algo
        - O(n log S)
"""