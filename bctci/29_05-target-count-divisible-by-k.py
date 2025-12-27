"""
Given a sorted array of integers, arr, a target value, target, and a positive
integer, k, return whether the number of ocurrences of the target in the array
is a multiple of k.

Edges
- k = 0
- target doesn't appear in array

Example

-10 -1 -1 0 4 6
target = 4
k = 2
False

Complexity
n: len of arr

Solutions

#1 Naive
init count
for val in arr
    if val == target
        count += 1

if count % k:
    return False
return True

t: O(n)
s: O(1)

#2 Double bin search
init l and r
def is_before
    return val at i < target

while r - l > 1
    m = r + l // 2
    if is_before m
        l = m
    else
        r = m

lower = r

def is_after
    return val at i <= target

reset r and l
while r - l > 1
    m = r + l // 2
    if is_after m
        l = m
    else
        r = m

upper = l

return not (upper - lower % k)

t: O(log n)
s: O(1)
"""
def is_divisble(arr, target, k):
    if not arr or not k:
        return False
    n = len(arr)
    l, r = 0, n - 1
    def is_before(i):
        return arr[i] < target
    
    while r - l > 1:
        m = r + l // 2
        if is_before(m):