from typing import List

def num_islands(grid: List[List[str]]) -> int:
    """
    >>> num_islands([["1","1","1"],["0","1","0"],["1","0","0"],["1","0","1"]])
    3
    >>> num_islands([["1","1","1","1","0"],["1","0","0","0","1"],["1","0","0","1","1"],["0","1","0","1","0"],["1","1","0","1","1"]])
    3
    >>> num_islands([["1","0","1","0","1"],["0","1","0","1","0"],["1","0","1","0","1"],["0","1","0","1","0"],["1","0","1","0","1"]])
    13
    """
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    islands = 0

    def dfs(r: int, c: int):
        # Out of bounds or water? Stop.
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return

        # Mark this cell as visited by turning it into water
        grid[r][c] = '0'

        # Explore all 4 directions
        dfs(r + 1, c)  # down
        dfs(r - 1, c)  # up
        dfs(r, c + 1)  # right
        dfs(r, c - 1)  # left

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                islands += 1       # found a new island
                dfs(r, c)          # mark the whole island

    return islands
