"""
You are given an array of letters, arr, and a string, word. We know that word
appears within arr as a subsequence (its letters appear in order, though not
necessarily contiguously).

Identify the earliest occurence of the word in arr (that is, the first
subsequence from left to right that spells out word) and move all those letters,
in order, to the end of arr.

You must do this in place, using only O(1) extra space, and preserve the
relative order of both the moved letters and remaining letters.

Edges
- word and arr are the same
- word is empty

edit
 c

s e e k e r a n d w r i t e r
    w
      s

s e k e r a n w r e r e d i t

ab
c

b a c b
      w
        s
b c a b

Complexity
w = len of word
n = len of arr

Solutions

#1 Three pointers
init writer seeker and word pointers
while seeker lt len of arr
    if val at seeker is the same as val at word
        move seeker and word pointers
    else
        write val at seeker to writer pos
        move seeker and writer forward

for char in word
    write to writer pos
    move writer forward

t: O(w + n)
s: O(1)
"""

def shift_word(arr, word):
    w, s, c = 0, 0, 0

    while s < len(arr):
        if c < len(word) and arr[s] == word[c]:
            s += 1
            c += 1
        else:
            arr[w] = arr[s]
            s += 1
            w += 1

    for char in word:
        arr[w] = char
        w += 1

"""
Post Mortem
- Missed a condition where c goes past the end of the word but seeking/writing
  continues, causing a IndexError on L61
    - Rectified with the `c < len(word)` condition
"""