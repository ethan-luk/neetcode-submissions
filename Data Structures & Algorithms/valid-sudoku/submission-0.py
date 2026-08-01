class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = defaultdict(set) # maps row number -> values in row
        colSet = defaultdict(set) # maps col number -> values in col
        squareSet = defaultdict(set) # maps square number -> values in square

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == '.':
                    continue
                
                if (num in rowSet[r] or num in colSet[c] or num in squareSet[(r//3, c//3)]
                    ):
                    return False
                
                rowSet[r].add(num)
                colSet[c].add(num)
                squareSet[(r//3, c//3)].add(num)
        
        return True


                
                