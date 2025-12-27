"""
A valley shaped array is an array of integers such that:
- it can be split into a non-empty prefix and non-empty suffix
- the prefix is sorted in decreasing order
- the suffix is sorted in increasing order
- all element are unique

Given a valley shaped array, arr, return the smallest value.

Example

0 1 2 3 4
3 2 1 4 8
  l
    r
  m

0 -2 -4 -1 3

0 2
l r

Edges
- smallest is at index 1 or -2
- len 2
- negative numbers

Complexity
n: len of arr

Solutions
#1 Naive
init smallest var
iterate over the arr
    smallest var = min val and smallest var
return smallest var

t: O(n)
s: O(1)

#2 binary search
def is_before
    val at index > val at index + 1

init l and r at 0 and n - 1
while r - l > 1
    m = l + r // 2
    if is_before m
        l = m
    else
        r = m
return arr of r

t: O(log n)
s: O(1)
"""
def valley_bottom(arr):
    def is_before(i):
        return arr[i] > arr[i + 1]

    l, r = 0, len(arr) - 1
    while r - l > 1:
        m = (r + l) // 2
        if is_before(m):
            l = m
        else:
            r = m

    return min(arr[l], arr[r])

def run_tests():
  tests = [
      # Example 1 from book
      ([6, 5, 4, 7, 9], 4),
      # Example 2 from book
      ([5, 6, 7], 5),
      # Example 3 from book
      ([7, 6, 5], 5),
      ([2, 1], 1),
      ([3, 2, 4], 2)
  ]

  for arr, want in tests:
    got = valley_bottom(arr)
    assert got == want, f"\nvalley_bottom({arr}): got: {got}, want: {want}\n"

if __name__ == "__main__":
  run_tests()

"""
Post Mortem
- I found the definition of a non-empty prefix and suffix confusing
    - Is 6 5 4 a valid array?
        - In the answer they say that it is. That the 4 is actually considered part of the suffix.
        - The answer is the arr at r
    - What about 4 5 6?
        - The answer is the arr at l
    - What about 6 5 4 7 8? Is the 4 prefix or suffix?
    - I unconsciously chose to include it in the suffix by my definition of is_before
    - This is why my choice to only return arr at l, and then arr at r is flawed
        - We must return the min of those two values
- I don't understand the need for their i == 0 optimization. 
"""