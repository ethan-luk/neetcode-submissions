class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1)
        ]

        q = deque()

        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        level = 1
        while q:
            length = len(q)
            for _ in range(length):
                row, col = q.popleft()
                visited.add((row, col))
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (
                        min(nr, nc) < 0 or \
                        nr >= ROWS or nc >= COLS or \
                        grid[nr][nc] == -1 or \
                        (nr, nc) in visited
                    ):
                        continue
                    q.append((nr, nc))
                    visited.add((nr, nc))
                    grid[nr][nc] = level
            level += 1
