"""
Given an array consisting of letters 'R', 'W', and 'B' sort it in place to put
all the 'R' before all the 'W' and all the 'W' before the 'B'.

W W B R R B
    w
            s
R R B W W B
        w
            s
R R W W B B

R
w
s

[]

R R W W W B B
        w
      s

Complexity
n: len of arr

Solutions

#1 Writer seeker
init w and s
while s lt len of arr and w lt len of arr
    if w == R
        move w
    elif s != R
        move s
    else
        swap
        move both

set s = w
while s lt len arr and w lt len of arr
    if w == W
        move w
    elif s != W
        move s
    else
        swap
        move both

t: O(n)
s: O(1)
"""
def sort_colors(arr):
    if not arr:
        return arr

    w, s = 0, 1
    n = len(arr)
    while s < n and w < n:
        if arr[w] == 'R':
            w += 1
        elif arr[s] != 'R':
            s += 1
        else:
            arr[w], arr[s] = arr[s], arr[w]
            s += 1
            w += 1

    s = w + 1
    while s < n and w < n:
        if arr[w] == 'W':
            w += 1
        elif arr[s] != 'W':
            s += 1
        else:
            arr[w], arr[s] = arr[s], arr[w]
            s += 1
            w += 1


def run_tests():
  tests = [
      # Example from the book
      (list("RWBBWRW"), list("RRWWWBB")),
      # Additional test cases
      ([], []),
      (list("R"), list("R")),
      (list("W"), list("W")),
      (list("B"), list("B")),
      (list("RW"), list("RW")),
      (list("WR"), list("RW")),
      (list("RWB"), list("RWB")),
      (list("RRRWWBBB"), list("RRRWWBBB")),
      (list("BBBWWRRR"), list("RRRWWBBB")),
  ]
  for arr, want in tests:
    arr_copy = arr.copy()  # Make a copy since function modifies in place
    sort_colors(arr_copy)
    assert arr_copy == want, f"\nsort_colors({arr}): got: {
        arr_copy}, want: {want}\n"

if __name__ == "__main__":
  run_tests()
"""
Post Mortem
- A simpler approach, though with the same complexity, is a counter approach
    - Walk the array, counting each letter
    - Write out the letters x count into the array
- This would likely involve a hashset, but of fixed size since it's just got RWB as keys
    - Also the problem doesn't restrict the use of extra space, even if it did cost it
- The hint to use the counter was a fixed set of inputs
- Forgot to get the value out of the arr and ended up comparing the pointers to
  'W' and 'R' accidentally
- The issue with my writer/seeker approach is that the writer keeps getting ahead of the seeker
    - In order for the pattern to work that needs to stay invariant
    - This is why the inward pointers approach works better in this case
"""