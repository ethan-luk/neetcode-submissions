class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        cache = {}
        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in cache:
                return cache[(l, r)]

            even = (r - l) % 2 == 0
            left = piles[l] if even else 0
            right = piles[r] if even else 0

            cache[(l, r)] = max(dfs(l + 1, r) + left, dfs(l, r - 1) + right)
            return cache[(l, r)]
        
        return dfs(0, len(piles) - 1) > (sum(piles)) // 2