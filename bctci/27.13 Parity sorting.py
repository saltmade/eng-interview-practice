"""
Given an array of integers, arr, modify it in place to put all even numbers
before all odd numbers. The relative order between even numbers does not matter.
Same with the odds.

Edges
- Empty array
- All evens or all odds

#1 Inward pointers
init left and right
while left lt right
    if left is even
        advance left
    if right is odd
        decrement right
    else
        swap them
        advance left
        decrement right
"""