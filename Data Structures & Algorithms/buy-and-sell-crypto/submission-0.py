class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = float('-inf')
        l = 0

        for r in range(len(prices)):
            profit = prices[r] - prices[l]
            res = max(res, profit)
            if profit < 0:
                l = r
        
        return res
            