class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [0] * len(arr)
        res[-1] = -1
        curMax = arr[-1]
        for i in range(len(arr) - 2, -1, -1):
            res[i] = curMax
            curMax = max(arr[i], curMax)
        
        return res