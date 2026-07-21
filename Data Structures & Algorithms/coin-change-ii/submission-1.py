class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        def dfs(i, total):
            if total == amount:
                return 1
            if total > amount or i >= len(coins):
                return 0
            if (i, total) in cache:
                return cache[(i, total)]

            # skip
            res = dfs(i+1, total)
            # use
            res += dfs(i, total + coins[i])
            cache[(i, total)] = res
            return cache[(i, total)]
        
        return dfs(0, 0)