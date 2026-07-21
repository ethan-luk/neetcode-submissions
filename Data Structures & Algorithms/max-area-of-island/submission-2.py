class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1)
        ]
        visited = set()
        area = 0

        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))
            res = 1

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (min(nr, nc) < 0 or \
                        nr >= ROWS or nc >= COLS or \
                        grid[nr][nc] == 0 or \
                        (nr, nc) in visited
                    ):
                        continue
                    
                    visited.add((nr, nc))
                    q.append((nr, nc))
                    res += 1
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = max(area, bfs(r, c))

        return area