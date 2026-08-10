class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        cache = [[-1] * COLS for _ in range(ROWS)]
        def dfs(r, c):
            if r == ROWS - 1 and c == COLS - 1:
                return grid[r][c]
            if r >= ROWS or c >= COLS:
                return float('inf')
            
            if cache[r][c] != -1:
                return cache[r][c]
            
            cache[r][c] = grid[r][c] + min(dfs(r+1, c), dfs(r, c+1))
            return cache[r][c]
        
        return dfs(0, 0)