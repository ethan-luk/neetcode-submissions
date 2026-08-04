class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        directions = [
            (1, 0), (-1, 0), (0, -1), (0, 1)
        ]

        island = set()

        def dfs(r, c):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or (r, c) in island or grid[r][c] == 0:
                return
            
            island.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        found = False
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    dfs(r, c)
                    found = True
                    break
            if found:
                break

        res = 0
        for r, c in island:
            neighbors = 0
            for dr, dc in directions:
                if (r + dr, c + dc) in island:
                    neighbors += 1
            res += (4 - neighbors)    
        return res   
