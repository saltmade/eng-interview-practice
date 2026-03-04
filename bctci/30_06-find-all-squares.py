"""
Given an array of unique integers, arr, return a list with all pairs of
indices, [i, j], such that arr[i]^2 == arr[j]. You can return the pairs in any
order.

Edges
- Empty array
- No numbers are square and root
- Negative numbers squared are positive
- Zero is its own square
- One is its own square

Example
0 1   2 3 4  5 6    7
2 100 4 8 0 -1 1000 10
ans = [[0, 2] [7, 1] [4, 4]]

Complexity
n: length of arr

Solutions

#1 Naive
If the array is empty, return an empty array
Init an answer array
val, idx in enumerate arr
  Iterate over every other value in arr as j to check if it's the square of val
  If it is, add [idx, j] to the answer
Return the answer

t: O(n^2)
s: O(1)

#2 Seen values
If the array is empty, return an empty array
Init an answer array
Init a seen dict
    keys are values from arr and values are the index of that value e.g. {4: 0}
val, idx in enumerate arr
    squared = val ** 2
    root = val ** 1/2
    add val: idx to seen

    if root in seen
        add [seen[root], idx] to answer
    if squared in seen
        add [idx, seen[squared]] to answer

return answer

t: O(n)
s: O(n)

0 1   2 3 4  5 6    7
2 100 4 8 0 -1 1000 10
               i
seen 2:0 100:1 4:2 8:3 0:4 -1:5 1000:6 10:7
ans [0, 2] [4, 4] [7, 1]

Solution number 2 has the best possible time complexity O(n) and a space
complexity of O(n).
May I code it?
"""
def find_squares(arr):
    if not arr:
        return []

    answer = set()
    seen = dict()
    for idx, val in enumerate(arr):  # 3, 2
        squared = val ** 2  # 4
        root = val ** 1/2  # 1.1412
        seen[val] = idx  # 0:0 4:1 -3:2 2:3

        if root in seen:
            answer.add([seen[root]], idx)
        if squared in seen:
            answer.add([idx, seen[squared]])

    return list(answer)  # 0,0 3,1
"""
Result: FAIL
- Missed a closing ] on L76 that causes the code not to run
- Root of negative numbers would produce complex numbers, which would never be
  in seen
- Most of the issue stems from overcomplicating the implementation
  - We would already have to spend O(n) to get the solution
  - Trying to add numbers to the seen dict as we went added complexity that
    tripped me up without adding any value
- A more appropriate approach would be to do the work in two steps:
  1. Map values to indexes in a dict
  2. Reiterate over the arr to check for matching vals
"""
