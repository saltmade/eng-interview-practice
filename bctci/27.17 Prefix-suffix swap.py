"""
We are given an array of letters, arr, with a length, n, which is a multiple of
3. The goal is to modify arr in place to move the prefix of length n/3 to the
end and suffix of length 2n/3 to the beginning.

Edges
- ASCII? yes
- lowercase? yes
- empty? yes

b a d r e v i e w 
> r e v i e w b a d

b a d r e v i e w
i
      j

i e w r e v b a d

Solutions

#1 Append first 1/3 to the end, then shift back to original length
init i j to 0 and 1/3 of n
while i < 1/3 of n
    append those values to the end
reset i
while j < len of arr
    swap i and j
    move i and j forward
del backward 1/3

t: O(n)
s: O(n)

#2 Swap the first and last third, swap the first and second third
init i and j as 0 and 2/3 n
while j lt n
    swap arr at i and j
    move i and j forward
reset i to 0
reset j to 1/3 n
while j lt 2/3 n
    swap arr at i and j
    move i and j forward

t: O(n)
s: O(1)
"""

def swap_prefix_suffix(arr):
    n = len(arr)
    i, j = 0, int(2/3 * n)

    while j < n:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j += 1
    
    j = int(1/3 * n)
    i = 0

    while j < (2/3 * n):
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j += 1

def run_tests():
  tests = [
      # Example from the book
      (list("badreview"), list("reviewbad")),
      # Additional test cases
      ([], []),
      (list("abc"), list("bca")),
      (list("abcdef"), list("cdefab")),
      (list("123456789"), list("456789123")),
      (list("aaabbbccc"), list("bbbcccaaa")),
  ]
  for arr, want in tests:
    arr_copy = arr.copy()  # Make a copy since swap_prefix_suffix modifies in place
    swap_prefix_suffix(arr_copy)
    assert arr_copy == want, f"\nswap_prefix_suffix({arr}): got: {
        arr_copy}, want: {want}\n"

if __name__ == "__main__":
    run_tests()

"""
Post Mortem
- My way is one of the solutions
    - But it only works because we are guaranteed to have a prefix of length n/3
- Forgot that division would produce floats, so those need to be turned into ints
- Alternative for prefix of any length k
    1. Reverse the arr
    2. Reverse the final k letters of arr
    3. Reverse the first n - k letters of arr

    b a d r e v i e w , k = 3
    1. w e i v e r d a b
    2. w e i v e r b a d
    3. r e v i e w b a d
"""