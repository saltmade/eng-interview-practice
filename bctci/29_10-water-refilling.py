"""
We have an empty container with a capacity of `a` gallons and another container
with a capacity of `b` gallons. Return how many times you can pour the second
container into the first one without overflowing. Assume a > b.

- Constraint: you are not allowed ot use the division operator, but you can
still divide by power of two with the right-shift operator, >>. Recall that x >>
1 is the same as x // 2.

"""
def num_refills(a, b):

  # "Can we pour 'num_pours' times?"
  def is_before(num_pours):
    return num_pours * b <= a

  # Exponential search (repeated doubling until we find an upper bound).
  k = 1
  while is_before(k * 2):
    k *= 2

  # Binary search between k and k*2
  l, r = k, k * 2
  while r-l > 1:
    gap = r - l
    half_gap = gap >> 1  # Bit shift instead of division
    mid = l + half_gap
    if is_before(mid):
      l = mid
    else:
      r = mid
  return l

"""
Post Mortem
- Note: the solution above is copied from Interviewing.io since my solution was off.
- The complexity tripped me up on this one
    - a: capacity of a
    - b: capacity of b
    - k: max number of refills, aka a//b, aka the answer
    - t: O(a/b)
    - I expected the worst case to be b=1, which meant I could leave it out
    - But we don't know that, we are provided two variables, so the complexity
      needs to be described in terms of those variables
    - 
- Also didn't know how to work the bitwise shift version of division
"""