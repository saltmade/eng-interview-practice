# Cheatsheet

## Process

1. Understand the problem (2m)
2. Design the algo (5-7m)
	1. Explain the solution
	2. Get buy-in
3. Code the solution (20-25m)
	- Don't forget to refactor
4. Verify the solution (5-8m)
	1. Fix bugs

## Boundaries

> [!caution]
> Make sure to establish the terms first, e.g. `s = len(string)`

- Lower, output
- Lower, task
- Upper, naive
- Upper, constraints

| Complexity   | Max         | Rounded |
| ------------ | :---------- | ------- |
| `O(n!)`      | 11          | 10      |
| `O(2^n)`     | 27          | 30      |
| `O(n^3)`     | 584         | 500     |
| `O(n^2)`     | 14,142      | 15k     |
| `O(n log n)` | 8,677,239   | 10M     |
| `O(n)`       | 200,000,000 | 200M    |
| `O(log n)`   | Super high  |         |
| `O(1)`       | Infinite    |         |

## Math

- Number of nodes in a tree
	- d :: depth
	- b :: branching factor (i.e. how many branches per node)
	- $O(b^d)$
- Factorial
	- n!
	- Product of integer and all integers below it
	- $1 * 2 * 3 * … * n$
	- Trigger :: **permutation**
- Fibonacci
	- 0, 1, 1, 2, 3, 5, 8, 13…
	- $f(n) = f(n-1) + f(n-2)$
- n choose k
    - k subarrays of an n length array
    - $O(n^k)$ (loose upper bound)


## Python

Copy a grid
`res = [[0]*n for _ in board]`

Transpose a grid
`[list(row) for row in zip(*grid)]`

Modify an immutable variable inside func, outside scope
```
def foo():
	count = 0
	res = []
	def bar():
		nonlocal count
		count += 1
		res.append(count)
```