"""
Given a sorted array of integers, arr, remove duplicates in place while
preserving the order, and return the number of unqiue elements. It doesn't
matter what remains in arr beyond the unique elements.

-10 -5 -5 -1 0 2 2 2 2 5 10
                 w
                         s

Edges
- Empty array
- All the same value

Complexity
n: len of array

Solutions

#1 Writer Seeker
init writer and seeker pointer
while the seeker is lt len of arr
    if the val at the seeker is different than seeker -1 or seeker = 0
        write the val at seeker to pointer at writer
        move writer forward
    move seeker forward

return writer

t: O(n) 
s: O(1)
"""
def remove_dupes(arr):
    w, s = 0, 0
    while s < len(arr):
        must_keep = s == 0 or arr[s] != arr[s-1]
        if must_keep:
            arr[w] = arr[s]
            w += 1
        s += 1

    return w

"""
Post Mortem
- Didn't get this one at all
- Got stuck trying to figure out how to know when to write
    - In this case the writer should be dumb. It doesn't compare. It just writes
      and then moves forward.
    - The seeker is doing the comparison.
"""