class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1

        while top <= bot:
            m = top + (bot - top) // 2
            if matrix[m][-1] < target:
                top = m + 1
            elif matrix[m][0] > target:
                bot = m - 1
            else:
                break
        
        good_row = top + (bot - top) // 2
        if not (0 <= good_row < ROWS):
            return False
            
        l, r = 0, COLS - 1
        while l <= r:
            m = l + (r - l) // 2
            if matrix[good_row][m] > target:
                r = m - 1
            elif matrix[good_row][m] < target:
                l = m + 1
            else:
                return True

        return False