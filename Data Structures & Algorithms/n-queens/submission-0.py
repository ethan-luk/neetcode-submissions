class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        colSet = set()
        posDiagSet = set() # r + c
        negDiagSet = set() # r - c

        res = []
        board = [['.'] * n for _ in range(n)]

        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in colSet or (r + c) in posDiagSet or (r - c) in negDiagSet:
                    continue
                
                colSet.add(c)
                posDiagSet.add(r + c)
                negDiagSet.add(r - c)
                board[r][c] = 'Q'

                dfs(r + 1)

                colSet.remove(c)
                posDiagSet.remove(r + c)
                negDiagSet.remove(r - c)
                board[r][c] = '.'
            
        dfs(0)
        return res