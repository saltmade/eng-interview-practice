"""
An array is two integers, [start, end], where start <= end. Both endpoints are
considered part of the interval, which may consist of a singular point if start
= end.

You are given two arrays of intervals, arr1 and arr2. For each array, the
intervals are non-overlapping and sorted from left to right.

Return a similarly non-overlapping, sorted array of intervals representing the
intersection of the intervals in arr1 and arr2. An interval shouldn't start at
the same value where another ends.

1: [0, 1]  [4, 6]  [7, 8]
p1
2: [2, 3]  [5, 9]  [10, 11]
p2

Edges
- Empty array(s)
- Overlap of multiple intervals in one and one interval in the other
- No overlap of a given interval

Approaches

#1 Two pointers
init two pointers and a res array
start, end = 0, 1
while p1 lt len of arr1 and p2 lt len of p2
    get interval1 and interval2
    if the end of interval1 is before start of interval2
        if there's an interval in res and it overlaps with interval1
            pop the last interval from res
            get the lowest start and highest end
            combine and append to res
        otherwise
            just append it
    elif the end of interval2 is before the start of interval1
        do the same as before but with interval2
        ...
    else theres an overlap
        get the lowest start and highest end of interval1 and interval2
        if theres overlap with last val in res
            combine new interval with last interval in res
            append to res
        else
            append new interval to res

if p1 or p2 is less than the len of their respective array
    cleanup by appending the rest of those values to res

return res
"""

"""
Post Mortem
- Misunderstood the problem
    - It asks for the INTERSECTION of intervals, not combined intervals
    - This actually makes the answer simpler as you no longer need to consider
      what's already in the result
- Two pointers is the right approach

|---|
  |----|
  == intersection
"""