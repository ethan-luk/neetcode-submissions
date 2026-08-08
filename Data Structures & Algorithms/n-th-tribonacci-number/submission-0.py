class Solution:
    def tribonacci(self, n: int) -> int:
        cache = [-1] * (n + 1)
        def dfs(i):
            if i == 0:
                return 0
            elif i == 1:
                return 1
            elif i == 2:
                return 1
            elif cache[i] != -1:
                return cache[i]
            cache[i] = dfs(i - 1) + dfs(i - 2) + dfs(i - 3)
            return cache[i] 
        return dfs(n)