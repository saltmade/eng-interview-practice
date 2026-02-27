"""
2026-02-12
- Search in sorted grid
  - Didn't wrap mid calculation in parens, meaning it was incorrect
    - incorrect :: l + r // 2
    - correct :: (l + r) // 2
  - Row logic was confusing
    - I chose is_before = row[0] <= target
    - This isn't technically before the turning point, but instead inclusive of it
    - A more accurate way to determine this is is_before = row[-1] < target
    - The value could still be in the first or last row, so we still need to compare rows
    - But the evaluation would be clearer
  - Took length of an int, rather than the length of a row
    - In my second search I set up the variables incorrectly
    - l, r = 0, len(row) - 1
    - Except row was actually the row index, so this didn't make sense
  - Suboptimal approach
    - This problem has a trick I forgot about: flatting the grid
    - A flattened solution is O(log rc), beating my O(log r + log c)
"""
