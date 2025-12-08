"""
Reverse an array of letters, arr, in place using O(1) extra space.

c o r n u c o p i a
l
                  r

Edges
- Empty array
- ASCII? lowercase?
- Even vs odd lengths

Approaches

#1 Inward pointers
init left and right
while left is lt right
    swap left and right
    move left forward
    move right backward
"""