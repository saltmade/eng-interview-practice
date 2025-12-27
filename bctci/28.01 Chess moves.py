"""
Given:
- board, an nxn binary grid where n > 0, a 0 denotes an empty cell, and a 1
  denotes an occupied cell
- piece, which is one of "king", "queen" or "knight"
- r and c, with 0 <= r < n and 0 <= c < n which denote an unoccupied position on the board

Return a list of all unoccupied cells in the board that can be reached by a
given piece in one move, starting from r, c. The order of output cells does not matter.

Edges
- Surrounded
- 1x1 grid
- All empty

Complexity
n = 1 side of the grid

Solutions

#1 DFS
get the directions a piece can move
init a stack and a res array
while the stack has members
    pop the coordinates off
    if it's a 0
        Add the coordinates to the res
        add the coordinates to the stack

return the res

t: O(n*n)
s: O(n*n)
"""
def get_moves(board, piece, r, c):
    knight_moves = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]
    king_moves = [[1, 1], [1, -1], [-1, 1], [-1, -1], [0, 1], [0, -1], [1, 0], [-1, 0]]
    res = []

    def is_valid(r, c):
        n = len(board)
        return board[r][c] == 0 and 0 <= r < n and 0 <= c < n

    if piece == "knight":
        directions = knight_moves
    else:
        directions = king_moves

    for dr, dc in directions:
        new_r, new_c = r + dr, c + dc
        if piece == "queen":
            while is_valid(new_r, new_c):
                res.append([new_r, new_c])
                new_r += dr
                new_c += dc
        else:
            if is_valid(new_r, new_c):
                res.append([new_r, new_c])
    return res

"""
Post Mortem
- Note: The coded solution doesn't match the described one
- Failed to recognize that a single move is just the directions list, except for
queen. But queen can only continue in one direction, not all directions from a
move.
    - This is why I reached for a stack, but we really just need to keep adding
    along a direction.
"""