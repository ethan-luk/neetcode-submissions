class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sum_stones = sum(stones)
        target = (sum_stones + 1) // 2

        cache = {} # (i, cur_sum) -> # of ways
        def dfs(i, cur_sum):
            if cur_sum >= target or i >= len(stones):
                return abs(cur_sum - (sum_stones - cur_sum))
            if (i, cur_sum) in cache:
                return cache[(i, cur_sum)]
            cache[(i, cur_sum)] = min(dfs(i+1, cur_sum), dfs(i+1, cur_sum + stones[i]))
            return cache[(i, cur_sum)]
        return dfs(0,0)