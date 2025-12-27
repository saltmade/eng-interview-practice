"""
We are trying to search for a target integer, target, in a sorted array of
positive integers (duplicates allowed) that is too big to fit in memory. We can
only access the array through an API, fetch(i), which returns the value at index
i if i is within bounds or -1 otherwise. Using as few calls as possible, return
the index of the target, or -1 if it does not exist. If the target appears
multiple times, return any of the idices. There is no API to get the array's
length.

Example

3 7 45 102 950
        l
        m
            r
target = 104

Edges
- target is before array
- target is after array
- target isn't in array
- target is in multiple times
- other values appear 1M times before target
- empty array
- appears at 0 or 1

Complexity
n: len of arr

Solutions

#1 Naive
init i
while true
    val = fetch i
    if val > target
        break
    elif val == target
        return i
    else
        i += 1
return -1 

t: O(n)
s: O(1)

#2 Doubling
val0 = fetch 0
val1 = fetch 1
if val0 > target or val1 > target or val1 == -1
    return -1
elif val0 == target
    return 0
elsif val1 == target
    return 1

i = 2
while true
    val = fetch i
    if val > target or val == -1
        break
    elif val == target
        return i
    else
        i *= 2

def is_after
    val = fetch i
    return val > target or val == -1

l r = i-1 i
while r - l > 1
    m = r + l // 2
    if is_after m
        r = m
    else
        l = m

if fetch l == target
    return l
elif fetch r == target
    return r
else
    return -1

t: O(log n)
s: O(1)
"""

"""
Post Mortem
- I expected the optimal approach to require expotential growth
    - In reality a simple i *=2, aka doubling, is the opposite of log n
    - Should review what log is
- With that, the problem gets much simpler
    - No need to pre-check for 0 and 1
    r = 1
    while fetch r != -1
        r *= 2
"""