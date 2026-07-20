class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        
        def dfs(i, total):
            if total == amount:
                return 0
            
            if i == len(coins) or total > amount:
                return float('inf')
            
            if (i, total) in cache:
                return cache[(i, total)]

            cache[(i, total)] = min(dfs(i + 1, total), 1 + dfs(i, total + coins[i]))
            return cache[(i, total)] 
            
        ans = dfs(0, 0)
        return ans if ans != float('inf') else -1