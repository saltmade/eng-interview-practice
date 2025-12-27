"""
You are given two arrays of positive integers, p1 and p2, representing players
in a racing game. The two arrays are sorted, non-empty, and have the same
length, n. The i-th element of each array corresponds to where that player was
on the track at the i-th second of the race. We know that:
1. player 1 started ahead (p1[0] > p2),
2. player 2 overtook player 1 exactly once, and
3. player 2 remained ahead until the end (p1[n-1] < p2[n-1])

Assume the arrays have no duplicates, and that p1[i] != p2[i] for any index.
Return the index at which player 2 overtook player 1.

Example
   0 1 2 3 4
p1 2 4 6 8 10
p2 1 3 5 9 11
       l       
       m 
         r

ans = 3

Edges
- Overtakes at the last step

Solutions

#1 Naive
for i in range n
    if p2 of i > p1 of i
        return i

t: O(n)
s: O(1)

#2 Bin search
init l r and n

def is_before
    return p1 of i > p2 of i

while r - l > 1
    m = l + r // 2
    if is_before
        l = m
    else
        r = m
return r

t: O(log n)
s: O(1)
"""