class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        cache = [[-1] * COLS for _ in range(ROWS)]
        def dfs(i, j):

            if i >= ROWS or j >= COLS or obstacleGrid[i][j] == 1:
                return 0

            if (i == ROWS - 1 and j == COLS - 1):
                return 1
            
            if cache[i][j] != -1:
                return cache[i][j]
            
            cache[i][j] = dfs(i+1, j) + dfs(i, j+1)
            return cache[i][j]
        
        return dfs(0, 0)