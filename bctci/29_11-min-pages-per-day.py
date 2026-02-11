"""
You have upcoming interviews and have selected specific chapters from BCtCI to
read beforehand. Given an array, page_counts, where each element represents a
chapter's page count, and the number of days, days, until your interview,
determine the minimum number of pages you must read daily to finish on time.

Assume that:
    - You must read all the pages of a chapter before moving on to another one
    - If you finish a chapter on a given day, you practice for the rest of the
      day and don't start the next chapter until the next day.
    - len(page_counts) <= days

Examples

1 1 1 1 1 1
d = 6
ans = 1

1 9 12 7 5
d = 17
ans = 3

1 2 3 4 5 6 7 8 9 10 11 12
  l
  m
    r

100 50 65
d = 7
ans =

Complexity
n: len of page_counts
m: max val in page_counts
d: days

Solutions

#1 Guess and Check
init l r = 1, max of page_counts

def is_after test_val days_alotted
    days_taken = 0
    for pages in page_counts
        days_taken += math.ceil(pages / test_val)
    return days_taken < days_alotted

while r - l > 1
    pages_per_day = l + r // 2
    if is_after pages_per_day days
        r = m
    else
        l = m

return r

t: O(n log m)
s: O(1)
"""

"""
Post Mortem
- Missed the edge cases
- Didn't flesh out the time Complexity
  - O(n) for every calculation of is_after
  - O(log m) for the search over the page counts
"""
